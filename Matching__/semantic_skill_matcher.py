from sentence_transformers import SentenceTransformer, util
import torch
import os
from Matching__.config import EMBEDDING_MODEL, EMBEDDING_CACHE_PATH, EMBEDDING_BATCH_SIZE

class SemanticSkillMatcher:
    def __init__(self, target_skill_texts, model_name=EMBEDDING_MODEL, cache_path=EMBEDDING_CACHE_PATH, batch_size=EMBEDDING_BATCH_SIZE):
        self.model = SentenceTransformer(model_name)
        self.targets = list(dict.fromkeys(target_skill_texts))
        self.cache_path = cache_path
        self.batch_size = batch_size
        self.device = self.model.device
        self._load_or_build_embeddings()

    def _load_or_build_embeddings(self):
        if os.path.exists(self.cache_path):
            try:
                data = torch.load(self.cache_path)
                self.target_embeddings = data['embeddings'].to(self.device)
                self.targets = data['targets']
                return
            except Exception:
                pass
        all_embs = []
        for i in range(0, len(self.targets), self.batch_size):
            batch = self.targets[i:i + self.batch_size]
            embs = self.model.encode(batch, convert_to_tensor=True, device=self.device)
            all_embs.append(embs)
        if all_embs:
            self.target_embeddings = torch.cat(all_embs, dim=0)
        else:
            self.target_embeddings = self.model.encode(self.targets, convert_to_tensor=True, device=self.device)
        try:
            torch.save({'targets': self.targets, 'embeddings': self.target_embeddings.cpu()}, self.cache_path)
        except Exception:
            pass

    def match(self, user_skill_texts):
        user_embs = self.model.encode(user_skill_texts, convert_to_tensor=True, device=self.device)
        results = []
        for i, u_emb in enumerate(user_embs):
            scores = util.cos_sim(u_emb, self.target_embeddings)[0]
            best_score, best_idx = torch.max(scores, dim=0)
            best_score = float(best_score.item())
            best_idx = int(best_idx.item())
            results.append((user_skill_texts[i], self.targets[best_idx], best_score))
        return results
