skill_mapping = {
    # Programming Languages
    'javascript': 'javascript', 'js': 'javascript', 'typescript': 'typescript', 'ts': 'typescript',
    'python': 'python', 'py': 'python', 'java': 'java', 'c++': 'cpp', 'cpp': 'cpp', 'cplusplus': 'cpp',
    'c#': 'csharp', 'csharp': 'csharp', 'go': 'golang', 'golang': 'golang', 'rust': 'rust',
    'kotlin': 'kotlin', 'swift': 'swift', 'php': 'php', 'ruby': 'ruby', 'scala': 'scala',
    'r': 'r', 'matlab': 'matlab', 'perl': 'perl', 'haskell': 'haskell',
    # Web Frameworks - Frontend
    'react.js': 'react', 'reactjs': 'react', 'react': 'react', 'vue.js': 'vue', 'vuejs': 'vue',
    'vue': 'vue', 'angular': 'angular', 'angular.js': 'angular', 'angularjs': 'angular',
    'svelte': 'svelte', 'next.js': 'next', 'nextjs': 'next', 'next': 'next', 'nuxt.js': 'nuxt',
    'nuxtjs': 'nuxt', 'nuxt': 'nuxt', 'gatsby': 'gatsby',
    # Web Frameworks - Backend
    'node.js': 'node', 'nodejs': 'node', 'node': 'node', 'express.js': 'express', 'expressjs': 'express',
    'express': 'express', 'django': 'django', 'django framework': 'django', 'flask': 'flask',
    'fastapi': 'fastapi', 'spring': 'spring', 'spring boot': 'spring', 'spring framework': 'spring',
    'laravel': 'laravel', 'ruby on rails': 'rails', 'rails': 'rails', 'asp.net': 'aspnet', 'aspnet': 'aspnet',
    # Mobile Frameworks
    'react native': 'react native', 'react-native': 'react native', 'flutter': 'flutter',
    'ionic': 'ionic', 'xamarin': 'xamarin',
    # CSS Frameworks & Styling
    'tailwind css': 'tailwind', 'tailwind': 'tailwind', 'bootstrap': 'bootstrap',
    'material-ui': 'material ui', 'material ui': 'material ui', 'mui': 'material ui',
    'sass': 'sass', 'scss': 'sass', 'less': 'less', 'styled components': 'styled components',
    'styled-components': 'styled components', 'css': 'css', 'css3': 'css', 'html': 'html', 'html5': 'html',
    # Databases
    'postgresql': 'sql', 'postgres': 'sql', 'mysql': 'sql', 'mariadb': 'sql', 'sql server': 'sql',
    'microsoft sql server': 'sql', 'oracle': 'sql', 'sqlite': 'sql', 'mongodb': 'nosql',
    'cassandra': 'nosql', 'redis': 'nosql', 'elasticsearch': 'nosql', 'dynamodb': 'nosql',
    'firebase': 'nosql', 'firestore': 'nosql',
    # Cloud Platforms
    'aws': 'cloud', 'amazon web services': 'cloud', 'azure': 'cloud', 'microsoft azure': 'cloud',
    'google cloud': 'cloud', 'gcp': 'cloud', 'google cloud platform': 'cloud', 'ibm cloud': 'cloud',
    'oracle cloud': 'cloud', 'digital ocean': 'cloud', 'digitalocean': 'cloud', 'heroku': 'cloud',
    # Cloud Services
    'aws ec2': 'cloud computing', 'aws lambda': 'serverless', 'lambda': 'serverless',
    'azure functions': 'serverless', 'google cloud functions': 'serverless', 'docker': 'containerization',
    'kubernetes': 'containerization', 'k8s': 'containerization', 'terraform': 'iac',
    'infrastructure as code': 'iac', 'cloudformation': 'iac',
    # DevOps & Tools
    'git': 'version control', 'github': 'version control', 'gitlab': 'version control',
    'bitbucket': 'version control', 'jenkins': 'ci/cd', 'ci/cd': 'ci/cd', 'continuous integration': 'ci/cd',
    'continuous deployment': 'ci/cd', 'github actions': 'ci/cd', 'gitlab ci': 'ci/cd',
    'circleci': 'ci/cd', 'travis ci': 'ci/cd',
    # API & Web Services
    'rest api': 'api', 'restful api': 'api', 'rest': 'api', 'graphql': 'api', 'soap': 'api',
    'api development': 'api', 'web services': 'api', 'microservices': 'microservices',
    'microservice architecture': 'microservices',
    # Testing
    'jest': 'testing', 'mocha': 'testing', 'chai': 'testing', 'cypress': 'testing', 'selenium': 'testing',
    'junit': 'testing', 'pytest': 'testing', 'unit testing': 'testing', 'integration testing': 'testing',
    'test automation': 'testing',
    # Methodologies & Processes
    'agile': 'agile', 'agile methodology': 'agile', 'agile development': 'agile', 'scrum': 'agile',
    'kanban': 'agile', 'waterfall': 'waterfall', 'devops': 'devops', 'devsecops': 'devops',
    # AI/ML
    'machine learning': 'machine learning', 'ml': 'machine learning', 'deep learning': 'deep learning',
    'neural networks': 'deep learning', 'natural language processing': 'nlp', 'nlp': 'nlp',
    'computer vision': 'computer vision', 'tensorflow': 'tensorflow', 'pytorch': 'pytorch',
    'keras': 'keras', 'scikit-learn': 'scikit learn', 'scikit learn': 'scikit learn',
    # Data Science
    'data analysis': 'data analysis', 'data visualization': 'data visualization', 'tableau': 'data visualization',
    'power bi': 'data visualization', 'pandas': 'pandas', 'numpy': 'numpy', 'jupyter': 'jupyter',
    # Mobile Development
    'android development': 'android', 'ios development': 'ios', 'mobile development': 'mobile',
    'swiftui': 'ios', 'jetpack compose': 'android',
    # Desktop Development
    'electron': 'electron', 'qt': 'qt', 'wxwidgets': 'gui',
    # Game Development
    'unity': 'unity', 'unreal engine': 'unreal', 'game development': 'game dev',
    # Security
    'cybersecurity': 'security', 'information security': 'security', 'network security': 'security',
    'application security': 'security', 'penetration testing': 'security', 'ethical hacking': 'security',
    'cryptography': 'security',
    # Networking
    'tcp/ip': 'networking', 'http': 'networking', 'https': 'networking', 'dns': 'networking',
    'ssl': 'networking', 'tls': 'networking', 'cdn': 'networking',
    # Operating Systems
    'linux': 'linux', 'unix': 'linux', 'windows': 'windows', 'macos': 'macos', 'ubuntu': 'linux',
    'centos': 'linux', 'red hat': 'linux',
    # Soft Skills
    'communication': 'communication', 'communication skills': 'communication', 'verbal communication': 'communication',
    'written communication': 'communication', 'teamwork': 'teamwork', 'collaboration': 'teamwork',
    'leadership': 'leadership', 'project management': 'project management', 'time management': 'time management',
    'problem solving': 'problem solving', 'critical thinking': 'critical thinking', 'creativity': 'creativity',
    'adaptability': 'adaptability', 'attention to detail': 'attention to detail',
    # Business Skills
    'product management': 'product management', 'business analysis': 'business analysis',
    'stakeholder management': 'stakeholder management', 'requirements gathering': 'requirements gathering',
    'user stories': 'user stories',
    # Design
    'ui design': 'ui/ux', 'ux design': 'ui/ux', 'user interface': 'ui/ux', 'user experience': 'ui/ux',
    'figma': 'ui/ux', 'adobe xd': 'ui/ux', 'sketch': 'ui/ux', 'wireframing': 'ui/ux', 'prototyping': 'ui/ux',
    # Content Management
    'wordpress': 'cms', 'contentful': 'cms', 'sanity': 'cms', 'strapi': 'cms',
    # E-commerce
    'shopify': 'ecommerce', 'woocommerce': 'ecommerce', 'magento': 'ecommerce',
    # Monitoring & Analytics
    'grafana': 'monitoring', 'prometheus': 'monitoring', 'splunk': 'monitoring', 'datadog': 'monitoring',
    'google analytics': 'analytics',
    # Message Brokers
    'kafka': 'message broker', 'rabbitmq': 'message broker', 'activemq': 'message broker',
    # Version Control Advanced
    'git flow': 'git workflow', 'git branching': 'git workflow', 'merge conflicts': 'git workflow',
    # Documentation
    'technical writing': 'documentation', 'documentation': 'documentation', 'api documentation': 'documentation',
    # Performance
    'performance optimization': 'performance', 'code optimization': 'performance', 'load testing': 'performance',
    # Architecture
    'system design': 'system design', 'software architecture': 'software architecture',
    'design patterns': 'design patterns', 'clean architecture': 'software architecture',
    # Quality Assurance
    'qa': 'quality assurance', 'quality assurance': 'quality assurance', 'software testing': 'quality assurance',
}
