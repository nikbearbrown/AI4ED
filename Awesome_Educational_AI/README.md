# Educational AI

## Software for Chatbots
- **[ManyChat](https://manychat.com/)**: Primarily focuses on creating chatbots for Facebook Messenger, offering a user-friendly interface without the need for coding. 
- **[Freshchat](https://www.freshworks.com/live-chat-software/)**: A versatile tool from Freshworks that supports chatbots on various platforms, including web and mobile, with a focus on customer engagement. 
- **[Drift](https://www.drift.com/)**: Offers a combination of live chat and automated chatbots, targeting businesses looking to use chat for sales and marketing. 
- **[Chatfuel](https://chatfuel.com/)**: A platform for building chatbots for Facebook and Instagram without requiring coding skills, used by both small businesses and large enterprises. 
- **[HubSpot Chatbot Builder](https://www.hubspot.com/products/marketing/chatbot-builder)**: Part of HubSpot’s CRM platform, this tool allows users to create chatbots to qualify leads, book meetings, and more, integrating seamlessly with HubSpot’s suite of marketing tools. 

## Algorithms for Chatbots
Chatbot development involves a range of algorithms and techniques designed to process, understand, and generate human-like text responses. The complexity of these algorithms varies widely, from simple rule-based systems to advanced machine learning and artificial intelligence models. Here's an overview of the key algorithms used in chatbot development:

**1. Rule-Based Approaches**
- **Pattern Matching**: These chatbots operate on predefined patterns or rules. When a user's input matches a rule, the chatbot responds with the associated answer. AIML (Artificial Intelligence Markup Language) is a common example of a technology used for creating pattern-matching chatbots.

**2. Natural Language Processing (NLP)**
- **Tokenization and Parsing**: Break down user input into tokens (words or phrases) and analyze the grammatical structure to understand the intent.
- **Named Entity Recognition (NER)**: Identifies and classifies key information in the text, such as names, locations, dates, and more, helping the chatbot understand the context.
- **Sentiment Analysis**: Determines the user's sentiment (positive, negative, neutral) towards a topic, which can influence the chatbot's response tone.

**3. Machine Learning Algorithms**
- **Decision Trees**: Used for classification and regression, helping chatbots make decisions based on user input.
- **Naïve Bayes Classifier**: A probabilistic classifier that applies Bayes' theorem, useful for text classification tasks like spam detection or topic classification.
- **Support Vector Machines (SVM)**: Another classification technique that finds the hyperplane which best separates different classes in the input feature space.
- **Recurrent Neural Networks (RNN) and Long Short-Term Memory (LSTM)**: Specialized in processing sequences of data, making them ideal for understanding the context and generating coherent responses in chatbots.

**4. Deep Learning**
- **Convolutional Neural Networks (CNNs)**: Though primarily used for image processing, CNNs can also be applied to NLP tasks for feature extraction from text.
- **Transformer Models**: Including BERT (Bidirectional Encoder Representations from Transformers) and GPT (Generative Pretrained Transformer), these models have revolutionized chatbot development by enabling a deeper understanding of language context and generating human-like text.

**5. Reinforcement Learning**
- In this approach, chatbots learn to make decisions by receiving rewards for positive outcomes. It's particularly useful for developing chatbots that can improve through interactions with users over time.

Each of these algorithms has its strengths and is suitable for different aspects of chatbot development. Rule-based systems are straightforward and easy to implement but lack flexibility. NLP and machine learning algorithms offer more nuanced understanding and response generation, suitable for a wide range of applications. Deep learning and reinforcement learning take it a step further by enabling chatbots to understand and generate human-like responses, learn from interactions, and improve over time. In practice, modern chatbots often combine several of these techniques to leverage the strengths of each, providing a more effective and engaging user experience.

## State-of-the-Art LLMs
- **[GPT-4](https://spotintelligence.com)**: Continues the legacy of its predecessors by OpenAI, improving on GPT-3.5 with capabilities to understand and generate both natural language and code, though specific technical details like model size remain undisclosed. 

- **[Claude v1](https://beebom.com)**: Developed by Anthropic and backed by Google, Claude aims to be helpful, honest, and harmless. It has shown promising results in benchmarks, even outperforming PaLM 2 in certain tests and offering the largest context window of 100k tokens. 

- **[Cohere](https://beebom.com)**: Founded by former Google Brain team members, focuses on generative AI use cases for enterprises, boasting models ranging from 6B to 52B parameters. Its accuracy and robustness, particularly in the Cohere Command model, have been highly praised. 

- **[Falcon](https://beebom.com)**: Stands out as the first open-source LLM mentioned, developed by the Technology Innovation Institute (TII) in the UAE, offering models trained on 40B and 7B parameters and supporting multiple languages. 

- **[LLaMA](https://beebom.com)**: Released by Meta in various sizes, from 7B to 65B parameters, LLaMA models have shown to outperform GPT-3 in efficiency and are significant for the open-source community, though they are intended for research use only. 

- **[XGen-7B](https://www.datacamp.com)**: Salesforce's entry into the LLM space, designed to support longer context windows and prioritizes efficiency with only 7B parameters. It aims to provide high-quality outputs with relatively smaller model sizes. 

- **[GPT-NeoX and GPT-J](https://www.datacamp.com)**: Open-source alternatives to GPT, developed by EleutherAI, featuring 20B and 6B parameters respectively. These models are recognized for their high accuracy across various NLP tasks without the need for RLHF training. 

- **[Vicuna 13-B](https://www.datacamp.com)**: An open-source conversational model that has shown impressive performance in evaluations, making it suitable for a wide range of industries including customer service, healthcare, and education. 

## Ethics in Chatbots
- **Privacy and Data Protection**: Chatbots often collect personal data from users to provide personalized responses and improve their service. Ethical considerations include ensuring that this data is collected, stored, and processed securely and in compliance with data protection laws such as GDPR in Europe. Users should be clearly informed about what data is being collected and for what purpose, along with having control over their data.

- **Transparency and Explainability**: There's a growing demand for transparency in how chatbots and AI systems make decisions, especially when they impact users significantly. Ethical development involves creating systems that can explain their decision-making processes in understandable terms. This transparency helps build trust with users and allows for the scrutiny of the AI's decisions.

- **Accountability**: When chatbots fail or cause harm, it's crucial to have clear accountability mechanisms in place. This involves determining who is responsible for the chatbot's actions - the developers, the company deploying it, or even the AI itself. Implementing ethical guidelines and standards can help ensure that there are protocols for addressing any issues that arise.

- **Bias and Fairness**: AI systems, including chatbots, can inherit biases present in their training data, leading to unfair or discriminatory outcomes. Ethical chatbot development requires actively working to identify and mitigate these biases. This might involve diverse datasets for training, regular audits of chatbot interactions, and mechanisms for users to report biased or inappropriate responses.

- **Impact on Employment**: The automation potential of chatbots raises concerns about their impact on employment, particularly in sectors heavily reliant on human interaction like customer service. Ethically deploying chatbots involves considering the potential displacement of workers and exploring ways to mitigate these effects, such as retraining programs.

- **Engagement in Sensitive Topics**: Chatbots increasingly engage in sensitive areas, such as mental health support. Ethical considerations here include ensuring that chatbots handle such interactions with care, respect, and an understanding of their limitations. Clear guidelines and the involvement of human professionals when necessary are crucial.

## Personalization of Chatbots
- **User Data Utilization**: Utilizing user data effectively is fundamental for personalization. By analyzing user profiles and past interactions, chatbots can tailor conversations to individual preferences, such as names, interests, and purchase history. Behavioral analysis further enables predictive personalization, allowing chatbots to anticipate future needs and offer relevant recommendations.

- **Natural Language Processing (NLP)**: NLP plays a crucial role in parsing user inputs to understand context and sentiment. This enables chatbots to discern the intent behind messages, allowing for responses that align with the user's emotional state or needs. NLP facilitates nuanced, human-like interactions, significantly improving the overall user experience.

- **Machine Learning for Personalization**: Machine learning algorithms empower chatbots to learn from each interaction and adapt over time. This adaptive learning process ensures continuous improvement in engaging users effectively. Predictive analysis further enhances personalization, enabling chatbots to proactively address user inquiries and needs, creating a more engaging dialogue.

- **Integration with CRM and Other Systems**: Personalization benefits greatly from integrating chatbots with CRM systems and external data sources. CRM integration provides access to detailed customer profiles and histories, enriching the foundation for personalized interactions. External data integration allows chatbots to incorporate relevant contextual information, making conversations more engaging.

- **Customization Options for Users**: Allowing users to customize their chatbot interactions, including language, tone, and interests, enhances personalization. Feedback mechanisms offer insights into user satisfaction, enabling ongoing refinement of the chatbot experience based on user preferences.

- **Context-Aware Conversations**: Maintaining conversation context across sessions is crucial for coherence and relevance. Chatbots that remember previous interactions can provide continuous, contextually appropriate dialogue. Dynamic content delivery, adjusted based on factors like time of day or user location, further personalizes the experience.

- **Personalized Recommendations**: Tailored recommendations based on user data and interaction history make chatbot conversations more engaging. Adapting response strategies to individual user preferences ensures that chatbots deliver content that resonates with users, enhancing engagement.

## Chatbots in Education
- **Jill Watson at the University of Georgia:** A chatbot designed for a computer science course, increasing student engagement and showing promise for broader educational use.

- **KNUSTbot in Ghana:** Implemented in Kwame Nkrumah University of Science and Technology to provide personalized support and address high student-to-instructor ratios, improving student motivation and interaction.

- **Georgia Tech's TA Chatbot:** Developed to assist in a knowledge-based AI course, answering student queries effectively, which led to high satisfaction rates among students.

- **Duolingo's Chatbots:** Offer language learners simulated conversation experiences to practice new languages in a stress-free environment, enhancing language acquisition skills.

- **LEO at the University of Sydney:** A virtual assistant used to guide students through university services and resources, improving access to information and student satisfaction.

## Best LLMs for Chatbots
- **Advanced Language Understanding and Generation**: 
  - **GPT-4**: Ideal for complex conversational AI with capabilities in natural language and code.
  - **Claude v1**: Known for its large context window and being user-friendly.

- **Enterprise Use Cases**: 
  - **Cohere**: Offers accuracy and robustness for business applications.

- **Open-Source Solutions**: 
  - **Falcon & LLaMA**: Great for developers seeking efficient models without commercial restrictions.
  - **GPT-NeoX & GPT-J**: High accuracy across NLP tasks, suitable for various applications.

- **Efficiency and Context Management**: 
  - **XGen-7B**: Designed for long context windows, optimizing performance.

- **Versatile Applications**: 
  - **Vicuna 13-B**: Demonstrates wide applicability across industries like customer service and education.

## Vector Databases

Vector databases are specialized databases designed to handle vector data, arrays of numbers representing data in high-dimensional space. These databases excel in operations like similarity search, crucial for AI and machine learning applications, including chatbots, due to several reasons:

## Reasons Why Vector Databases are Important in Chatbot Development

- **Semantic Search**: Vector databases enable semantic search in chatbots, allowing for more effective natural language query processing. By converting text into vectors, chatbots can find the most relevant answers by measuring similarity between query vectors and database vectors.

- **Improved User Interaction**: They contribute to more engaging and intuitive user interactions. Understanding queries more accurately allows for personalized and relevant responses, enhancing the user experience.

- **Scalability**: Designed for large data volumes, vector databases support chatbots' scalability, ensuring fast and accurate responses as user numbers and queries grow.

- **Efficiency in Data Retrieval**: Unlike traditional keyword matching, vector databases use distance metrics for efficient semantic matching, crucial for chatbots aiming to understand intent and meaning.

- **Support for Multiple Languages**: Vector databases facilitate multilingual chatbot support. Since vectors can represent meaning across languages, chatbots can respond to queries in various languages with appropriate training.

- **Continuous Learning and Improvement**: Chatbots can continuously learn and improve by analyzing query vectors and response effectiveness, refining their models for better future answers.

- **Integration with Advanced AI Models**: The compatibility of vector databases with advanced AI models, including deep learning, enables chatbots to leverage the latest in AI research for natural language processing and generation.

## LangChain
LangChain is a framework and toolkit designed to streamline the development and deployment of applications that utilize language models, such as those by OpenAI. It aims to simplify the integration of complex natural language processing (NLP) capabilities into various applications, with a particular focus on chatbots. LangChain provides a modular architecture, facilitating the creation of sophisticated systems that combine language models with databases, APIs, and custom logic.

LangChain enables developers to build applications capable of understanding, processing, and generating human-like text. It offers a versatile modular architecture, allowing for the integration of various components. This framework includes utilities for chaining language models with services, managing interaction states, and handling decision logic for the use of different components.

**Relevance to Chatbots**

LangChain's significance in chatbot development is multifaceted:

- **Simplified Integration**: It eases the integration of language models into chatbots, enabling advanced NLP features for understanding queries and generating responses.

- **Enhanced Capabilities**: LangChain allows chatbots to incorporate advanced features such as context management, multi-turn conversation handling, and external data and API integration, leading to more accurate and engaging interactions.

- **Customizability and Flexibility**: The framework's modular design lets developers customize chatbot behaviors to meet specific requirements, offering the ability to modify components, experiment with language models, and adjust conversational logic.

- **Scalability**: Designed for scalability, LangChain supports the development of chatbots that can handle increasing complexity and user numbers, ensuring consistent performance.

- **Rapid Prototyping and Development**: LangChain provides tools and abstractions for common development tasks, facilitating faster prototyping, testing, and deployment of chatbots.

 **Community and Support**: Supported by a community of developers and AI practitioners, LangChain benefits from collective expertise, support, and best practices sharing, enhancing the quality of chatbots developed with the framework.


## Fine-tuning LLMs
**1. Define Your Objectives and Requirements**

- **Identify the Purpose**: Define the primary goal of your chatbot, whether it's for customer support, personal assistance, entertainment, or education.
- **Understand Your Audience**: Know the demographics and expectations of your chatbot's users.
- **Set Performance Metrics**: Establish metrics to measure the chatbot's success, such as user satisfaction, resolution rate, or engagement level.

**2. Choose the Right Language Model**

- **Select a Pre-trained Model**: Opt for a pre-trained language model like GPT (OpenAI), BERT (Google), or similar, as a starting point.
- **Consider Model Size**: Find a balance between the model's complexity and the available computational resources.

**3. Prepare Your Training Data**

- **Collect Domain-Specific Data**: Accumulate text data relevant to your chatbot's domain, including conversation logs, domain texts, FAQs, etc.
- **Format the Data**: Structure your data into pairs of inputs (user queries) and outputs (chatbot responses) for training.
- **Augment and Annotate**: Enhance your dataset with synthetic data if needed and annotate it for training purposes.

**4. Fine-Tune the Model**

- **Split Your Data**: Divide your dataset into training, validation, and test sets to ensure effective learning and to prevent overfitting.
- **Customize Training Parameters**: Adjust learning rate, batch size, and epoch number based on your requirements.
- **Monitor the Training Process**: Use validation data to track the model's learning progress, focusing on metrics like loss and accuracy.

**5. Evaluate and Iterate**

- **Test the Model**: Evaluate the fine-tuned model with your test set to gauge its real-world performance.
- **Gather Feedback**: Deploy your chatbot in a controlled setting to collect user feedback.
- **Iterate**: Refine your model and chatbot based on user feedback and performance analysis.

**6. Deployment and Monitoring**

- **Deploy Your Chatbot**: Launch your chatbot in the intended environment.
- **Monitor Performance**: Continuously assess its performance and user interactions, adjusting as necessary based on feedback and observed needs.

**Best Practices**

- **Ethical Considerations**: Respect privacy and ethical guidelines in your data collection and usage.
- **Bias Mitigation**: Actively seek and mitigate biases in your training data and model responses.
- **Continuous Learning**: Enable your chatbot to learn from ongoing interactions and adapt over time.


## Apps

- [QuickGPT](https://sindresorhus.gumroad.com/l/quickgpt) - Access the ChatGPT web UI from the menu bar, Dock, or using a keyboard shortcut on macOS.
- [MacGPT](https://www.macgpt.com) - Native macOS app with a global prompt and also a web UI wrapper.
- [Chatterbox](https://manuelkehl.gumroad.com/l/chatterbox) - Native macOS app that can be shown with a keyboard shortcut.
- [WriteMage](https://writemage.com) - Native macOS app to use ChatGPT in any app. ($)
- [PaletteBrain](https://palettebrain.com) - Native macOS app to use ChatGPT in any app. ($)
- [Machato](https://untimelyunicorn.gumroad.com/l/machato) - Native macOS app. ($)
- [wonderGPT](https://wondergpt.co) - Native macOS app with a focus on simplicity.
- [Petey](https://apps.apple.com/app/id6446047813) - Native iOS and watchOS app. ($)
- [IntelliBar](https://intellibar.app) - macOS app that can be shown with a keyboard shortcut. ($ · Electron)
- [Ask AI](https://sindresorhus.com/ask-ai) - Native watchOS app. ($)
- [Chat Answer](https://github.com/bapaws/answer) - Native iOS and Android app.
- [Chat AI Desktop App](https://github.com/sonnylazuardi/chat-ai-desktop) - Cross-platform web UI wrapper.
- [ChatGPT Desktop Application](https://github.com/lencx/ChatGPT) - Cross-platform web UI wrapper. (Electron)
- [ChatGPT Android](https://github.com/skydoves/chatgpt-android) - Native Android app.
- [ChatARKit](https://github.com/trzy/ChatARKit) - iOS app for creating AR experiences with natural language.
- [Delphi ChatGPT](https://github.com/HemulGM/ChatGPT) - Native cross-platform app.
- [Chatbox](https://github.com/Bin-Huang/chatbox) - Cross-platform app.
- [Short Circuit](https://apps.apple.com/app/id1638522784) - Native iOS and macOS app with support for Siri, Shortcuts, and more. ($)
- [ChatBoost](https://play.google.com/store/apps/details?id=studio.muggle.chatboost) - Native Android app with support for Azure voice, custom prompts, and more. ($)
- [Developer Duck](https://apps.apple.com/app/id1662283032) - Native developer-focused macOS app with Xcode plugin and command line support. ($)
- [Hello History](https://hellohistory.ai) - Chat with historical figures on iOS and Android. ($)
- [Actions](https://github.com/sindresorhus/Actions) - Use ChatGPT from the Shortcuts app on iOS and macOS.
- [EasyChat AI](https://easychat-ai.app) - Native Windows app using the latest Windows 11 design lanquage.
- [pgMagic](https://pgmagic.app) - macOS app that lets you query your PostgreSQL database using natural language. ($)
- [Atua](https://atua.app) - macOS app to use ChatGPT in any app. ($)

## Web apps

### Hosted and self-hosted

- [ShareGPT](https://github.com/domeccleston/sharegpt) - Share permanent links to ChatGPT conversations.
- [Anse](https://github.com/anse-app/anse) - Alternative ChatGPT web UI.
- [chatbot-ui](https://github.com/mckaywrigley/chatbot-ui) - Alternative ChatGPT web UI.
- [ChatGPT Next Web](https://github.com/Yidadaa/ChatGPT-Next-Web) - Alternative ChatGPT web UI.
- [roomGPT](https://github.com/Nutlope/roomGPT) - Generate your dream room.
- [DocsGPT](https://github.com/arc53/DocsGPT) - Documentation assistant.
- [promptsandbox](https://github.com/eg9y/promptsandbox.io) - Visual programming tool for experimenting with ChatGPT.
- [Adrenaline](https://github.com/shobrook/adrenaline/) - Talk to your codebase.
- [DeepWrite AI](https://github.com/simplysabir/AI-Writing-Assistant) - Blog post generator.
- [Chat with GPT](https://github.com/cogentapps/chat-with-gpt) - Open-source ChatGPT web app with a voice.
- [FastChat](https://github.com/lm-sys/FastChat) - An open platform for training, serving, and evaluating large language model based chatbots.
- [kindle-gpt](https://github.com/mckaywrigley/kindle-gpt) - Search and chat on your Kindle highlights.
- [eslint-gpt](https://github.com/ycjcl868/eslint-gpt) - Generate ESLint rules from example code.
- [chatgpt-i18n](https://github.com/ObservedObserver/chatgpt-i18n) - Localize your websites.
- [AgentGPT](https://github.com/reworkd/AgentGPT) - Autonomous AI agents in your browser.
- [OP Vault ChatGPT](https://github.com/pashpashpash/vault-ai) - Give ChatGPT long-term memory using the OP Stack (OpenAI + Pinecone Vector Database).
- [chatgpt-demo](https://github.com/anse-app/chatgpt-demo) - Minimal web UI for ChatGPT.
- [pdfGPT](https://github.com/bhaskatripathi/pdfGPT) - Interactive conversations with the contents of PDF files.
- [Chat Chat](https://github.com/okisdev/ChatChat) - Your own unified AI interface.
- [VLog](https://github.com/showlab/VLog) - Convert videos to documents.
- [Ask-Anything](https://github.com/OpenGVLab/Ask-Anything) - ChatGPT with video understanding and communication.
- [TaskMatrix](https://github.com/microsoft/TaskMatrix) - Combines ChatGPT with Visual Models for enhanced image-chat interactions.
- [OpenChat](https://github.com/openchatai/OpenChat) - Personalized ChatGPT chatbot.
- [gpt-code-ui](https://github.com/ricklamers/gpt-code-ui) - Code interpreter integrated with ChatGPT.
- [ai-chatbot](https://github.com/vercel-labs/ai-chatbot) - Personalized ChatGPT AI chatbot.
- [Open Interpreter](https://github.com/KillianLucas/open-interpreter) - Code interpreter with ChatGPT.
- [Web3-GPT](https://github.com/Markeljan/Web3GPT) - Deploy smart contracts with ChatGPT.
- [CometLLM](https://github.com/comet-ml/comet-llm) - Open-source UI to log, visualize, and search your prompts, chains, and prompt variables.
- [OpenAgents](https://github.com/xlang-ai/OpenAgents) - Open-source replicate of ChatGPT Plus products including code interpreter, plugins and web browsing.

### Hosted

- [TypingMind](https://www.typingmind.com) - Alternative web UI.
- [ChatKit](https://chatkit.app) - Refined ChatGPT UI with support for plugins and accessing external resources.
- [Humata.ai](https://www.humata.ai) - Ask anything about your files.
- [Epic Music Quiz](https://epicmusicquiz.com) - Create your own custom music video quiz.
- [FlexGPT](https://flexgpt.io) - Like ChatGPT but for pros, with long-term memory, internet access, unlimited GPT-4, and no subscription.
- [LearnGPT](https://learngpt.art) - Title-based book creation. ($)
- [Wielded](https://wielded.com) - Web UI that works for OpenAI, Azure, Anthropic, and AWS Bedrock. Free for individuals.

### Self-hosted

- [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) - An experimental open-source attempt to make GPT-4 fully autonomous.
- [ChatGPT-Paper-Reader](https://github.com/talkingwallace/ChatGPT-Paper-Reader) - Read and summarize academic papers.
- [Sidekick](https://github.com/ai-sidekick/sidekick) - Connect external data to ChatGPT APIs through a dashboard.
- [twitterbio](https://github.com/Nutlope/twitterbio) - Generate your Twitter bio.
- [Beelzebub](https://github.com/mariocandela/beelzebub) - Secure honeypot framework.

### Examples

- [ChatGPT-Python-Applications](https://github.com/xiaowuc2/ChatGPT-Python-Applications) - A collection of Python web apps.

## Browser extensions

- [ChatGPT for Google](https://chatgpt4google.com) - Display ChatGPT response alongside search engine results.
- [ChatGPT Prompt Genius](https://github.com/benf2004/ChatGPT-Prompt-Genius) - Discover, share, import, and use the best prompts for ChatGPT.
- [ChatGPT Box](https://github.com/josStorer/chatGPTBox) - Deep ChatGPT integrations in your browser.
- [ChatGPT Export and Share](https://github.com/liady/ChatGPT-pdf) - Download your ChatGPT history to PNG, PDF or a sharable link.
- [Superpower ChatGPT](https://chrome.google.com/webstore/detail/superpower-chatgpt/amhmeenmapldpjdedekalnfifgnpfnkc) - Enhance the ChatGPT web UI with search history, create folders, export all chats, pin messages, and access thousands of prompts.
- [chatgpt-google-summary-extension](https://github.com/sparticleinc/chatgpt-google-summary-extension) - Display ChatGPT summaries alongside Google search results, YouTube videos, etc.
- [FancyGPT](https://chrome.google.com/webstore/detail/fancygpt/meonalmakdjaojaoipfhahcfccoecegk) - Save and share beautiful ChatGPT snippets as images, PDFs, and text files.
- [WritingMate.ai](https://chrome.google.com/webstore/detail/writingmateai-1-chatgpt-a/iihamopomflffiecicbgelncanmfionp) - Writing assistant.
- [Summarize](https://github.com/clmnin/summarize.site) - Summarize websites.
- [WebChatGPT](https://github.com/qunash/chatgpt-advanced/) - Enable web access in ChatGPT.
- [ChatGPT for Chrome & YouTube Summary](https://chrome.google.com/webstore/detail/chatgpt-for-chrome-youtub/cdjifpfganmhoojfclednjdnnpooaojb) - Access ChatGPT from the Chrome toolbar, see transcripts of YouTube videos, and summarize YouTube videos.
- [ChatGPT Enhancement Extension](https://github.com/sailist/chatgpt-enhancement-extension) - Enhancements to the ChatGPT web UI.
- [ChassistantGPT](https://github.com/idosal/assistant-chat-gpt) - Chrome browser extension that embeds ChatGPT as a hands-free voice assistant.
- [Talk-to-ChatGPT](https://github.com/C-Nedelcu/talk-to-chatgpt) - Talk with ChatGPT using your voice and listen to answers.
- [ChatGPT for Google Colab](https://github.com/ali-h-kudeir/ChatGPT-Google-Colab) - Embed ChatGPT inside Google Colab.
- [codereview.gpt](https://github.com/sturdy-dev/codereview.gpt) - Reviews your pull requests.
- [GPT2Markdown](https://github.com/0xreeko/gpt2markdown) - Export your ChatGPT conversations to Markdown.
- [ChatGPT Widescreen Mode](https://github.com/adamlui/chatgpt-widescreen) - Adds widescreen and fullscreen mode to ChatGPT.
- [ChatGPT Infinity](https://github.com/adamlui/chatgpt-infinity) - Makes ChatGPT automatically answer random questions to increase your knowledge.
- [Meeper](https://github.com/pas1ko/meeper) - Transcriptions, summary and more using ChatGPT and Whisper AI for meetings and any browser tab.
- [YouTube Summary by TubeSum](https://chromewebstore.google.com/detail/tubesum/hkhihfjmjgledkdhmlohldmpnolcoabm) - Summarize YouTube videos.

**User scripts**

- [ChatGPT Exporter](https://github.com/pionxzh/chatgpt-exporter) - Export and share ChatGPT conversation history.
- [KeepChatGPT](https://github.com/xcanwin/KeepChatGPT/blob/main/README_EN.md) - Fixes common networks errors and problems with ChatGPT.
- [ChatGPT Widescreen Mode](https://github.com/adamlui/chatgpt-widescreen) - Adds widescreen and fullscreen mode to ChatGPT.
- [Autoclear ChatGPT History](https://github.com/adamlui/autoclear-chatgpt-history) - Auto-clear ChatGPT conversation history for increased privacy.
- [ChatGPT Auto Refresh](https://github.com/adamlui/chatgpt-auto-refresh) - Keeps ChatGPT sessions fresh to avoid network errors and Cloudflare checks.
- [DuckDuckGPT](https://github.com/kudoai/duckduckgpt) - Brings the magic of ChatGPT to search results.
- [ChatGPT Infinity](https://github.com/adamlui/chatgpt-infinity) - Makes ChatGPT automatically answer random questions to increase your knowledge.
- [ChatGPT Auto-Continue](https://github.com/adamlui/chatgpt-auto-continue) - Automatically clicks "Continue generating" when responses are cut off.

**Bookmarklets**

- [Conversation Saving](https://github.com/jcubic/chat-gpt) - Save your ChatGPT conversation.
- [ChatGPT Export](https://github.com/yaph/chatgpt-export) - Export ChatGPT conversations to Markdown files.

## CLI tools

- [Assistant CLI](https://github.com/diciaup/assistant-cli) - Use ChatGPT from the command-line.
- [SearchGPT](https://github.com/tobiasbueschel/search-gpt) - Connect ChatGPT with the Internet.
- [chatgpt-conversation](https://github.com/platelminto/chatgpt-conversation) - Have a conversation with ChatGPT.
- [CLI for ChatGPT](https://github.com/j178/chatgpt) - Interactive interface for ChatGPT.
- [chat-gpt-ppt](https://github.com/williamfzc/chat-gpt-ppt) - Automatically generate PowerPoint presentations.
- [StackExplain](https://github.com/shobrook/stackexplain) - Have your error messages explained in plain English.
- [clevercli](https://github.com/clevercli/clevercli) - ChatGPT-powered command-line utilities.
- [README-AI](https://github.com/eli64s/README-AI) - Automatically generate README files.
- [aicommits](https://github.com/Nutlope/aicommits) - Automatically generate Git commit messages.
- [happycommit](https://github.com/jackbackes/happycommit) - Automatically generate Git commit messages.
- [commit-assist](https://github.com/dejorrit/commit-assist) - Automatically generate Git commit messages.
- [cz-git](https://github.com/Zhengqbbb/cz-git) - Automatically generate Git commit messages.
- [ai-commit](https://github.com/guanguans/ai-commit) - Automatically generate conventional Git commit messages.
- [gptcommit](https://github.com/zurawiki/gptcommit) - Git hook for authoring commit messages.
- [autodoc](https://github.com/context-labs/autodoc) - Automatically generate codebase documentation.
- [GPT3 WordPress Post Generator](https://github.com/nicolaballotta/gpt3-wordpress-post-generator) - Generate WordPress blog posts.
- [aiac](https://github.com/gofireflyio/aiac) - Infrastructure-as-Code generator.
- [tenere](https://github.com/pythops/tenere) - Terminal interface (TUI) for ChatGPT written in Rust.
- [shellChatGPT](https://github.com/mountaineerbr/shellChatGPT) - Use ChatGPT from the command-line.
- [Shell Genie](https://github.com/dylanjcastillo/shell-genie) - Interact with the terminal in plain English.
- [ShellGPT](https://github.com/TheR1D/shell_gpt) - Use ChatGPT from the command-line.
- [chatGPT-shell-cli](https://github.com/0xacx/chatGPT-shell-cli) - Use ChatGPT from the command-line. Shell script.
- [aifiles](https://github.com/jjuliano/aifiles) - Organize and manage your files using AI.

## Bots

- [chatgpt-twitter-bot](https://github.com/transitive-bullshit/chatgpt-twitter-bot) - Twitter bot.
- [chatgpt-telegram-bot-serverless](https://github.com/franalgaba/chatgpt-telegram-bot-serverless) - Telegram bot.
- [chatgpt-telegram](https://github.com/m1guelpf/chatgpt-telegram) - Telegram bot.
- [myGPTReader](https://github.com/madawei2699/myGPTReader) - Slack bot.
- [ChatGPTSlackBot](https://github.com/pedrorito/ChatGPTSlackBot) - Slack bot.
- [ChatGPT Discord Bot](https://github.com/Zero6992/chatGPT-discord-bot) - Discord bot.
- [chatgpt-discord](https://github.com/m1guelpf/chatgpt-discord) - Discord bot.
- [kubernetes-chatgpt-bot](https://github.com/robusta-dev/kubernetes-chatgpt-bot) - Kubernetes bot.
- [CodeReview Bot](https://github.com/anc95/ChatGPT-CodeReview) - GitHub Actions bot.
- [openai-pr-reviewer](https://github.com/fluxninja/openai-pr-reviewer) - GitHub Actions bot.
- [chatgpt-create-unit-tests](https://github.com/zebroc/chatgpt-create-unit-tests) - GitHub Actions bot that analyses a pull request and adds unit tests if necessary.
- [gpt4-pdf-chatbot-langchain](https://github.com/mayooear/gpt4-pdf-chatbot-langchain) - Chatbot for large PDF files.
- [wechat-chatgpt](https://github.com/fuergaosi233/wechat-chatgpt) - Wechat bot.
- [Chat Bling](https://chatbling.net) - WhatsApp bot.
- [chatgpt-telegram-bot](https://github.com/karfly/chatgpt_telegram_bot) - Telegram bot that supports voice messages.
- [DuckDuckGPT](https://github.com/kudoai/duckduckgpt) - DuckDuckGo bot.
- [BraveGPT](https://github.com/kudoai/bravegpt) - Brave Search bot.

## Integrations

- [chatgpt-raycast](https://github.com/abielzulio/chatgpt-raycast) - Raycast extension.
- [mpociot/chatgpt-vscode](https://github.com/mpociot/chatgpt-vscode) - VSCode extension.
- [gencay/vscode-chatgpt](https://github.com/gencay/vscode-chatgpt) - VSCode extension.
- [org-ai](https://github.com/rksm/org-ai) - Emacs org-mode.
- [vim-chatgpt](https://github.com/CoderCookE/vim-chatgpt) - Vim plugin.
- [ChatGPT.nvim](https://github.com/jackMort/ChatGPT.nvim) - Neovim plugin.
- [ChatGPT Jetbrains](https://github.com/dromara/ChatGPT) - Jetbrains plugin.
- [DocGPT](https://workspace.google.com/u/0/marketplace/app/docgpt_ai_writer_for_docs/466607203252) - Writing assistant for Google Docs.
- [docGPT](https://github.com/cesarhuret/docGPT) - Use ChatGPT in Google Docs.
- [SlidesAI](https:/www.slidesai.io) - Create AI-powered presentations in Google Slides.
- [WordGPT](https://github.com/filippofinke/WordGPT) - Use ChatGPT in Microsoft Word.
- [Add ChatGPT to Microsoft Word](https://github.com/analyticsinmotion/add-chatgpt-to-microsoft-word) - How to integrate ChatGPT with Microsoft Word.
- [Open Assistant Helper](https://github.com/AnotiaWang/open-assistant-helper) - Improve Open Assistant with ChatGPT.
- [ChatGPTWizard](https://github.com/AliDehbansiahkarbon/ChatGPTWizard) - Embarcadero RAD Studio (Delphi & C++ Builder) plugin.
- [AICommand](https://github.com/keijiro/AICommand) - ChatGPT integration with Unity Editor.
- [AI Shader](https://github.com/keijiro/AIShader) - ChatGPT-powered shader generator for Unity.
- [Translate GPT](https://github.com/ftp27/fastlane-plugin-translate_gpt) - A fastlane plugin that provides an action to translate localizable strings using ChatGPT.
- [PandasAI](https://github.com/gventuri/pandas-ai) - Integrate ChatGPT capabilities into Pandas.
- [Plus AI for Google Slides](https://www.plusdocs.com/plus-ai-for-google-slides) - Create AI-powered presentations in Google Slides.
- [Scikit-LLM](https://github.com/iryna-kondr/scikit-llm) - Integrate ChatGPT capabilities into scikit-learn.
- [ChatGPT-MD](https://github.com/bramses/chatgpt-md) - ChatGPT integration with Obsidian note-taking software.
- [Chapyter](https://github.com/chapyter/chapyter) - Integrate ChatGPT capabilities into Jupyter Notebook.
- [I Don't Care About Commit Message](https://github.com/mefengl/vscode-i-dont-care-about-commit-message) - Auto-generate commit messages and push actions in VS Code.

## Packages

### API clients

- [Swift](https://github.com/MacPaw/OpenAI)
- [Node.js](https://github.com/transitive-bullshit/chatgpt-api)
- [Go](https://github.com/AlmazDelDiablo/gpt3-5-turbo-go)
- [Delphi](https://github.com/HemulGM/DelphiOpenAI)
- [PHP](https://github.com/openai-php/client)
- [Ruby](https://github.com/alexrudall/ruby-openai)

### JavaScript

- [chatgpt.js](https://github.com/kudoai/chatgpt.js) - Easy interaction with the ChatGPT DOM.
- [Vercel AI SDK](https://github.com/vercel-labs/ai) - An open source library for building AI-powered user interfaces.

### Python

- [GPTCache](https://github.com/zilliztech/GPTCache) - Semantic cache to store responses from LLM queries.
- [knowledge-gpt](https://github.com/geeks-of-data/knowledge-gpt) - Extract knowledge from information sources.


## Open Source Projects

- [spaCy](https://pypi.org/project/spacy/) - Python library for advanced natural language processing.

- [Botkit](https://github.com/howdyai/botkit) - Open Source bot building blocks for Slack, Facebook Messenger, Twilio, Microsoft with [Botkit Studio](https://studio.botkit.ai/) - a hosted development environment

- [Claudia Bot Builder](https://github.com/claudiajs/claudia-bot-builder) - Open Source library to create chat bots for FB, Slack, Skype and Telegram and deploy to AWS Lambda

- [AIVA](https://github.com/kengz/aiva) -General-purpose virtual assistant for developers.

- [Bottr](https://github.com/Bottr-js/Bottr) - Open Source bot framework (nodejs).

- [RedBot](http://red-bot.io) - A Node-RED plugin to create multi-platform bots visually (nodejs).

- [Botman](https://botman.io/) - an open-source framework in PHP

- [BotPress](https://botpress.io/) - Botpress is an on-prem, open-source bot building platform for businesses

- [Bottender](https://bottender.js.org/) - an open-source chatbot framework in NodeJS

- [Rasa Talk](https://github.com/jackdh/RasaTalk) - GUI supported open-source chatbot framework built over Rasa.

## Services

### Chatbot design

- [Botsociety](https://botsociety.io) - Design and preview your chabot before actually building it.

### Chatbot builder

- [Botfront](https://botfront.io) - An open source platform to visually and intuitively build chatbots with Rasa.

- [BotStar](https://wwww.botstar.com) - Design and Develop Chatbots for Messenger & Website. Visually.

- [Flow XO](https://flowxo.com) - Bot + human messaging platform

- [Gupshup](https://www.gupshup.io) - Comprehensive Platform to build Bots and use messaging Services

- [Pandorabots](https://pandorabots.com/) - Web service for building and deploying chatbots

- [DialogFlow](https://dialogflow.com/) - Conversational User Experience platform

- [reply.ai](https://www.reply.ai/) - Platform to build & manage conversation chatbots

- [Chatfuel](https://chatfuel.com/) - Build a Facebook bot without coding

- [m.io](https://m.io) - Enterprise bots for Slack, HipChat and Skype

- [TuringRobot](http://www.tuling123.com/) - Platform for AI robots and AI robot OS

### Messaging services

- [msg.ai](http://msg.ai/) - AI for Conversational Commerce

- [wit.ai](https://wit.ai/) - Natural Language for Developers

- [Google NLP](https://cloud.google.com/natural-language/) - Cloud Natural Language API (up to 5K free analyses/month)

## Analytics

- [Dashbot](https://www.dashbot.io/) - Bot Analytics

- [ChatBase](https://chatbase.com/welcome) - Analyze and optimize bots more easily

## Payments & Subscriptions

- [Paypal](https://developer.paypal.com/)

- [Stripe](https://stripe.com/)

- [Braintree](https://www.braintreepayments.com/)

## Example projects 

- [Facebook Messenger DevKit](https://github.com/olegakbarov/facebook-messenger-devkit) - Node.js setup for rapid development for Facebook Messenger Platform

## Chatbot Platforms and Channels

- [Facebook messenger](https://developers.facebook.com/docs/messenger-platform)

- [Wechat](https://admin.wechat.com/)

- [Slack](https://api.slack.com/bot-users)

- [Telegram](https://core.telegram.org/)

- [Microsoft Bot Framework](https://dev.botframework.com/)

- SMS - Short Messaging System, e.g. over [Twilio](https://www.twilio.com)

- Twitter

- Hipchat

- Skype

- Kik

- Line

- [IBM Bot Asset Exchange](https://developer.ibm.com/code/exchanges/bots/)

## Personal Assistants

- [Apple Siri](https://www.apple.com/ios/siri/)

- [Google Assistant](https://assistant.google.com/)

- [Amazon Alexa](https://developer.amazon.com/alexa)

- [Cortana](https://developer.microsoft.com/en-us/cortana)

- [Viv](http://viv.ai/) - Promising artificial intelligence platform

- [Magic](https://getmagic.com/) - Text to get anything ondemand

- [Sensay](https://www.sensay.it/) - Instantly connect with a real human whenever you need advice or inspiration.

## Chatbots

- [Botlist](https://botlist.co/) - An App Store For Bots

- [A. L. I. C. E.](https://alice.pandorabots.com/)

- [Mitsuku](https://pandorabots.com/mitsuku/) - Won most humanlike AI in Loebner Price

- [Microsoft XiaoIce in Chinese ](http://www.msxiaoice.com/)

- [Microsoft Tay](https://twitter.com/tayandyou)

- [Cleverbot](http://www.cleverbot.com/)

- [BotList.net](https://botlist.net/) - A list of bots for Discord, Slack, Telegram and more

## Resources

- [Beginner’s Guide To Chatbots](https://chatbotsmagazine.com/the-complete-beginner-s-guide-to-chatbots-8280b7b906ca) - Good introduction

- [Chatbots Magazine](https://chatbotsmagazine.com/) - A good place to Learn About Chatbots

- [Bot Weekly](http://botweekly.com/issues) - Weekly round up of the most interesting chatbot and AI news

- [Bot Wiki](https://botwiki.org/) - Catalog of online bots, tools and tutorials

### Tutorials

- [How To Develop A Chat Bot With Node.js](https://www.smashingmagazine.com/2016/10/how-to-develop-a-chat-bot-with-node-js/) - Tutorial for Claudia Bot Builder

- [Handling Permissions with DialogFlow and Actions On Google](https://medium.com/google-developer-experts/handling-permissions-with-dialogflow-and-actions-on-google-b08c8f228c00) - Tutorial for the Google Assistant & DialogFlow

- [Build multi-lingual Actions for the Google Assistant](https://medium.com/google-developer-experts/build-multi-lingual-actions-for-the-google-assistant-106d2b94aa1a) - Tutorial for the Google Assistant & DialogFlow

- [Mastering follow-up intents with DialogFlow](https://medium.com/google-developer-experts/mastering-follow-up-intents-with-dialogflow-851b75b83f5a) - Tutorial for the Google Assistant & DialogFlow


## Courses
* [CS50’s Intro to Artificial Intelligence](https://cs50.harvard.edu/ai/2020) - This course explores the concepts and algorithms at the foundation of modern artificial intelligence
* [MIT: Intro to Deep Learning](https://introtodeeplearning.com) - A seven day bootcamp designed in MIT to introduce deep learning methods and applications
* [Deep Blueberry: Deep Learning book](https://mithi.github.io/deep-blueberry) - A free five-weekend plan to self-learners to learn the basics of deep-learning architectures like CNNs, LSTMs, RNNs, VAEs, GANs, DQN, A3C and more
* [Spinning Up in Deep Reinforcement Learning](https://spinningup.openai.com/) - A free deep reinforcement learning course by OpenAI
* [MIT Artificial Intelligence Videos](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/lecture-videos) - MIT AI Course
* [Grokking Deep Learning in Motion](https://www.manning.com/livevideo/grokking-deep-learning-in-motion?a_aid=algmotion&a_bid=5d7bc0ba) - Beginner's course to learn deep learning and neural networks without frameworks.
* [Intro to Artificial Intelligence](https://www.udacity.com/course/cs271) - Learn the Fundamentals of AI. Course run by Peter Norvig
* [EdX Artificial Intelligence](https://www.edx.org/course/artificial-intelligence-uc-berkeleyx-cs188-1x-0#.VMeIsmSsVkg) - The course will introduce the basic ideas and techniques underlying the design of intelligent computer systems
* [Artificial Intelligence For Robotics](https://www.class-central.com/mooc/319/udacity-artificial-intelligence-for-robotics) - This class will teach you basic methods in Artificial Intelligence, including: probabilistic inference, planning and search, localization, tracking and control, all with a focus on robotics
* [Machine Learning](https://class.coursera.org/ml-008) - Basic machine learning algorithms for supervised and unsupervised learning
* [Deep Learning](https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187) - An Introductory course to the world of Deep Learning using TensorFlow. 
* [Stanford Statistical Learning](http://online.stanford.edu/course/statistical-learning-winter-2014) - Introductory course on machine learning focusing on: linear and polynomial regression, logistic regression and linear discriminant analysis; cross-validation and the bootstrap, model selection and regularization methods (ridge and lasso); nonlinear models, splines and generalized additive models; tree-based methods, random forests and boosting; support-vector machines.
* [Knowledge Based Artificial Intelligence](https://www.udacity.com/course/knowledge-based-ai-cognitive-systems--ud409) - Georgia Tech's course on Artificial Intelligence focussing on Symbolic AI.
* [Deep RL Bootcamp Lectures](https://sites.google.com/view/deep-rl-bootcamp/lectures) - Deep Reinforcement Bootcamp Lectures - August 2017
* [Machine Learning Crash Course By Google](https://developers.google.com/machine-learning/crash-course/ml-intro) Machine Learning Crash Course features a series of lessons with video lectures, real-world case studies, and hands-on practice exercises.
* [Python Class By Google](https://developers.google.com/edu/python/) This is a free class for people with a little bit of programming experience who want to learn Python. The class includes written materials, lecture videos, and lots of code exercises to practice Python coding.
* [Deep Learning Crash Course](https://www.manning.com/livevideo/deep-learning-crash-course) In this liveVideo course, machine learning expert Oliver Zeigermann teaches you the basics of deep learning.
* [Artificial Intelligence: A Modern Approach](http://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597) - Stuart Russell & Peter Norvig
  * Also consider browsing the [list of recommended reading](http://aima.cs.berkeley.edu/books.html), divided by each chapter in "Artificial Intelligence: A Modern Approach".
* [Paradigms Of Artificial Intelligence Programming: Case Studies in Common Lisp](http://www.amazon.com/exec/obidos/ASIN/1558601910) - Paradigms of AI Programming is the first text to teach advanced Common Lisp techniques in the context of building major AI systems
* [Reinforcement Learning: An Introduction](http://www.freetechbooks.com/reinforcement-learning-an-introduction-second-edition-draft-t1282.html) - This introductory textbook on reinforcement learning is targeted toward engineers and scientists in artificial intelligence, operations research, neural networks, and control systems, and we hope it will also be of interest to psychologists and neuroscientists.
* [The Cambridge Handbook Of Artificial Intelligence](http://www.amazon.com/Cambridge-Handbook-Artificial-Intelligence/dp/0521691915) - Written for non-specialists, it covers the discipline's foundations, major theories, and principal research areas, plus related topics such as artificial life
* [The Emotion Machine: Commonsense Thinking, Artificial Intelligence, and the Future of the Human Mind ](http://www.amazon.com/gp/product/0743276647) - In this mind-expanding book, scientific pioneer Marvin Minsky continues his groundbreaking research, offering a fascinating new model for how our minds work
* [Artificial Intelligence: A New Synthesis](http://www.amazon.com/Artificial-Intelligence-Synthesis-Nils-Nilsson/dp/1558604677) - Beginning with elementary reactive agents, Nilsson gradually increases their cognitive horsepower to illustrate the most important and lasting ideas in AI
* [On Intelligence](http://www.amazon.com/Jeff-Hawkins/e/B001KHNZ7C/ref=sr_ntt_srch_lnk_11?qid=1435480927&sr=8-11) - Hawkins develops a powerful theory of how the human brain works, explaining why computers are not intelligent and how, based on this new theory, we can finally build intelligent machines. Also audio version available from audible.com
* [How To Create A Mind](http://www.amazon.com/How-Create-Mind-Thought-Revealed/dp/0143124048/ref=pd_sim_14_3?ie=UTF8&refRID=0QY72H7NGRYH79R7S3K7) - Kurzweil discusses how the brain works, how the mind emerges, brain-computer interfaces, and the implications of vastly increasing the powers of our intelligence to address the world’s problems
* [Deep Learning](http://www.deeplearningbook.org/) - Goodfellow, Bengio and Courville's introduction to a broad range of topics in deep learning, covering mathematical and conceptual background, deep learning techniques used in industry, and research perspectives. 
* [The Elements of Statistical Learning: Data Mining, Inference, and Prediction](https://web.stanford.edu/~hastie/ElemStatLearn/) - Hastie and Tibshirani cover a broad range of topics, from supervised learning (prediction) to unsupervised learning including neural networks, support vector machines, classification trees and boosting---the first comprehensive treatment of this topic in any book.
* [Deep Learning and the Game of Go](https://www.manning.com/books/deep-learning-and-the-game-of-go) - Deep Learning and the Game of Go teaches you how to apply the power of deep learning to complex human-flavored reasoning tasks by building a Go-playing AI. After exposing you to the foundations of machine and deep learning, you'll use Python to build a bot and then teach it the rules of the game.
* [Deep Learning for Search](https://www.manning.com/books/deep-learning-for-search) -  Deep Learning for Search teaches you how to leverage neural networks, NLP, and deep learning techniques to improve search performance.
* [Deep Learning with PyTorch](https://www.manning.com/books/deep-learning-with-pytorch) -  PyTorch puts these superpowers in your hands, providing a comfortable Python experience that gets you started quickly and then grows with you as you—and your deep learning skills—become more sophisticated. Deep Learning with PyTorch will make that journey engaging and fun.
* [Deep Reinforcement Learning in Action](https://www.manning.com/books/deep-reinforcement-learning-in-action) -  Deep Reinforcement Learning in Action teaches you the fundamental concepts and terminology of deep reinforcement learning, along with the practical skills and techniques you’ll need to implement it into your own projects.
* [Grokking Deep Reinforcement Learning](https://www.manning.com/books/grokking-deep-reinforcement-learning) -  Grokking Deep Reinforcement Learning introduces this powerful machine learning approach, using examples, illustrations, exercises, and crystal-clear teaching. 
* [Fusion in Action](https://www.manning.com/books/fusion-in-action) -  Fusion in Action teaches you to build a full-featured data analytics pipeline, including document and data search and distributed data clustering.
* [Real-World Natural Language Processing](https://www.manning.com/books/real-world-natural-language-processing) - Early access book on how to create practical NLP applications using Python. 
* [Grokking Machine Learning](https://www.manning.com/books/grokking-machine-learning) - Early access book that introduces the most valuable machine learning techniques.
* [Succeeding with AI](https://www.manning.com/books/succeeding-with-ai) - An introduction to managing successful AI projects and applying AI to real-life situations.
* [Elements of AI (Part 1) - Reaktor/University of Helsinki](https://www.elementsofai.com/) - An Introduction to AI is a free online course for everyone interested in learning what AI is, what is possible (and not possible) with AI, and how it affects our lives – with no complicated math or programming required.
* [Essential Natural Language Processing](https://www.manning.com/books/essential-natural-language-processing) - A hands-on guide to NLP with practical techniques, numerous Python-based examples and real-world case studies.
* [Kaggle's micro courses](https://www.kaggle.com/learn/overview) - A series of micro courses by offering practical and hands-on knowledge ranging from Python to Deep Learning.
* [Transfer Learning for Natural Language Processing](https://www.manning.com/books/transfer-learning-for-natural-language-processing?utm_source=github&utm_medium=organic&utm_campaign=book_azunre_transfer_3_10_20) - A book that gets you up to speed with the relevant ML concepts and then dives into transfer learning for NLP.
* * [Stanford Deep Learning Series](https://www.youtube.com/playlist?list=PLoROMvodv4rOABXSygHTsbvUz4G_YQhOb]
* [Amazon Machine Learning Developer Guide](https://docs.aws.amazon.com/machine-learning/latest/dg/machinelearning-dg.pdf) - A book for ML developers which introduces the ML concepts & strategies with lots of practical usages.
* [Machine Learning for Humans](https://medium.com/machine-learning-for-humans/why-machine-learning-matters-6164faf1df12) - A series of simple, plain-English explanations accompanied by math, code, and real-world examples.


## Books

* [Machine Learning for Mortals (Mere and Otherwise)](https://www.manning.com/books/machine-learning-for-mortals-mere-and-otherwise) - Early access book that provides basics of machine learning and using R programming language.
* [How Machine Learning Works](https://livebook.manning.com/book/how-machine-learning-works/welcome/v-5) - Mostafa Samir. Early access book that introduces machine learning from both practical and theoretical aspects in a non-threating way. 
* [MachineLearningWithTensorFlow2ed](https://www.manning.com/books/machine-learning-with-tensorflow-second-edition) - a book on general purpose machine learning techniques regression, classification, unsupervised clustering, reinforcement learning, auto encoders, convolutional neural networks, RNNs, LSTMs, using TensorFlow 1.14.1.
* [Serverless Machine Learning](https://www.manning.com/books/serverless-machine-learning-in-action) - a book for machine learning engineers on how to train and deploy machine learning systems on public clouds like AWS, Azure, and GCP, using a code-oriented approach.
* [The Hundred-Page Machine Learning Book](http://themlbook.com/) - all you need to know about Machine Learning in a hundred pages, supervised and unsupervised learning, SVM, neural networks, ensemble methods, gradient descent, cluster analysis and dimensionality reduction, autoencoders and transfer learning, feature engineering and hyperparameter tuning.
* [Trust in Machine Learning](https://www.manning.com/books/trust-in-machine-learning) - a book for experienced data scientists and machine learning engineers on how to make your AI a trustworthy partner. Build machine learning systems that are explainable, robust, transparent, and optimized for fairness.


## Programming

* [Prolog Programming For Artificial Intelligence](http://www.amazon.com/Programming-Artificial-Intelligence-International-Computer/dp/0321417461) - This best-selling guide to Prolog and Artificial Intelligence concentrates on the art of using the basic mechanisms of Prolog to solve interesting AI problems.
* [AI Algorithms, Data Structures and Idioms in Prolog, Lisp and Java](http://www.amazon.co.uk/Algorithms-Data-Structures-Idioms-Prolog/dp/0136070477) - [PDF here](https://pdfs.semanticscholar.org/f5c3/d7dbe4c47e310569a14d2338d0cb3d70a1bb.pdf)
* [Python Tools for Machine Learning](https://www.cbinsights.com/blog/python-tools-machine-learning/)
* [Python for Artificial Intelligence](https://wiki.python.org/moin/PythonForArtificialIntelligence)


## Philosophy

* [Super Intelligence](http://www.audible.co.uk/pd/Non-fiction/Superintelligence-Audiobook/B00LPMA33G) - Superintelligence asks the questions: What happens when machines surpass humans in general intelligence. A really great book.
* [Our Final Invention: Artificial Intelligence And The End Of The Human Era](http://www.audible.co.uk/pd/Non-fiction/Our-Final-Invention-Audiobook/B00KLJMDH8) - Our Final Invention explores the perils of the heedless pursuit of advanced AI. Until now, human intelligence has had no rival. Can we coexist with beings whose intelligence dwarfs our own? And will they allow us to?
* [How to Create a Mind: The Secret of Human Thought Revealed](http://www.audible.com/pd/Science-Technology/How-to-Create-a-Mind-Audiobook/B009S7OKJS/ref=a_search_c4_1_1_srTtl?qid=1422483493&sr=1-1) - Ray Kurzweil, director of engineering at Google, explored the process of reverse-engineering the brain to understand precisely how it works, then applies that knowledge to create vastly intelligent machines.
* [Minds, Brains, And Programs](http://cogprints.org/7150/1/10.1.1.83.5248.pdf) - The 1980 paper by philosopher John Searle that contains the famous 'Chinese Room' thought experiment. Probably the most famous attack on the notion of a Strong AI possessing a 'mind' or a 'consciousness', and interesting reading for those interested in the intersection of AI and philosophy of mind.
* [Gödel, Escher, Bach: An Eternal Golden Braid](http://www.amazon.com/G%C3%B6del-Escher-Bach-Eternal-Golden/dp/0465026567) - Written by Douglas Hofstadter and taglined "a metaphorical fugue on minds and machines in the spirit of Lewis Carroll", this wonderful journey into the the fundamental concepts of mathematics,symmetry and intelligence won a Pulitzer Prize for Non-Fiction in 1979. A major theme throughout is the emergence of meaning from seemingly 'meaningless' elements, like 1's and 0's, arranged in special patterns.
* [Life 3.0: Being Human in the Age of Artificial Intelligence](https://www.goodreads.com/book/show/34272565-life-3-0) - Max Tegmark, professor of Physics at MIT, discusses how Artificial Intelligence may affect crime, war, justice, jobs, society and our very sense of being human both in the near and far future.


## Free Content

* [Foundations Of Computational Agents](http://artint.info/html/ArtInt.html) - This book is published by Cambridge University Press, 2010
* [The Quest For Artificial Intelligence](http://ai.stanford.edu/~nilsson/QAI/qai.pdf) - This book traces the history of the subject, from the early dreams of eighteenth-century (and earlier) pioneers to the more successful work of today's AI engineers.
* [Stanford CS229 - Machine Learning](https://see.stanford.edu/Course/CS229) - This course provides a broad introduction to machine learning and statistical pattern recognition.
* [Computers and Thought: A practical Introduction to Artificial Intelligence](http://www.cs.bham.ac.uk/research/projects/poplog/computers-and-thought/) - The book covers computer simulation of human activities, such as problem solving and natural language understanding; computer vision; AI tools and techniques; an introduction to AI programming; symbolic and neural network models of cognition; the nature of mind and intelligence; and the social implications of AI and cognitive science.
* [Society of Mind](http://aurellem.org/society-of-mind/index.html) - Marvin Minsky's seminal work on how our mind works. Lot of Symbolic AI concepts have been derived from this basis.
* [Artificial Intelligence and Molecular Biology](https://web.archive.org/web/20060627060706/http://www.biosino.org/mirror/www.aaai.org/Press/Books/Hunter/hunter-contents.html) - The current volume is an effort to bridge that range of exploration, from nucleotide to abstract concept, in contemporary AI/MB research.
* [Brief Introduction To Educational Implications Of Artificial Intelligence](http://pages.uoregon.edu/moursund/Books/AIBook/index.htm) - This book is designed to help preservice and inservice teachers learn about some of the educational implications of current uses of Artificial Intelligence as an aid to solving problems and accomplishing tasks.
* [Encyclopedia: Computational intelligence](http://www.scholarpedia.org/article/Encyclopedia:Computational_intelligence) - Scholarpedia is a peer-reviewed open-access encyclopedia written and maintained by scholarly experts from around the world.
* [Ethical Artificial Intelligence](http://arxiv.org/abs/1411.1373) - a book by Bill Hibbard that combines several peer reviewed papers and new material to analyze the issues of ethical artificial intelligence.
* [Golden Artificial Intelligence](https://golden.com/wiki/Cluster%3A_Artificial_intelligence) - a cluster of pages on artificial intelligence and machine learning.
* [R2D3](http://www.r2d3.us/) - A website with explanations on topics from Machine Learning to Statistics. All helped with beautiful animated infographics and real life examples. Available in various languages.
* [Modeling Agents with Probabilistic Programs](https://agentmodels.org/) - This book describes and implements models of rational agents for (PO)MDPs and Reinforcement Learning.


## Code

* [ExplainX](https://github.com/explainX/explainx)- ExplainX is a fast, light-weight, and scalable explainable AI framework for data scientists to explain any black-box model to business stakeholders.
* [AIMACode](https://github.com/aimacode) - Source code for "Artificial Intelligence: A Modern Approach" in Common Lisp, Java, Python. More to come.
* [FANN](http://leenissen.dk/fann/wp/) - Fast Artificial Neural Network Library, native for C
* [FARGonautica](https://github.com/Alex-Linhares/FARGonautica) - Source code of Douglas Hosftadter's Fluid Concepts and Creative Analogies Ph.D. projects.


## Videos

* [A tutorial on Deep Learning](http://videolectures.net/jul09_hinton_deeplearn)
* [Basics of Computational Reinforcement Learning](http://videolectures.net/rldm2015_littman_computational_reinforcement)
* [Deep Reinforcement Learning](http://videolectures.net/rldm2015_silver_reinforcement_learning)
* [Intelligent agents and paradigms for AI](https://youtu.be/7o2GzSj86e8?t=3457)
* [The Unreasonable Effectiveness Of Deep Learning](https://www.youtube.com/watch?v=sc-KbuZqGkI) - The Director of Facebook's AI Research, Dr. Yann LeCun gives a talk on deep convolutional neural networks and their applications to machine learning and computer vision
* [AWS Machine Learning in Motion](https://www.manning.com/livevideo/aws-machine-learning-in-motion)- This interactive liveVideo course gives you a crash course in using AWS for machine learning, teaching you how to build a fully-working predictive algorithm.
* [Deep Learning with R in Motion](https://www.manning.com/livevideo/deep-learning-with-r-in-motion)-Deep Learning with R in Motion teaches you to apply deep learning to text and images using the powerful Keras library and its R language interface.
* [Grokking Deep Learning in Motion](https://www.manning.com/livevideo/grokking-deep-learning-in-motion)-Grokking Deep Learning in Motion will not just teach you how to use a single library or framework, you’ll actually discover how to build these algorithms completely from scratch!
* [Reinforcement Learning in Motion](https://www.manning.com/livevideo/reinforcement-learning-in-motion) - This liveVideo breaks down key concepts like how RL systems learn, how to sense and process environmental data, and how to build and train AI agents. 


## Learning

* [Deep Learning. Methods And Applications](http://research.microsoft.com/pubs/209355/DeepLearning-NowPublishing-Vol7-SIG-039.pdf) Free book from Microsoft Research
* [Neural Networks And Deep Learning](http://neuralnetworksanddeeplearning.com) - Neural networks and deep learning currently provide the best solutions to many problems in image recognition, speech recognition, and natural language processing. This book will teach you the core concepts behind neural networks and deep learning
* [Machine Learning: A Probabilistic Perspective](http://www.amazon.com/Machine-Learning-Probabilistic-Perspective-Computation/dp/0262018020) - This textbook offers a comprehensive and self-contained introduction to the field of machine learning, based on a unified, probabilistic approach
* [Deep Learning](https://www.deeplearningbook.org) - Yoshua Bengio, Ian Goodfellow and Aaron Courville put together this currently free (and draft version) book on deep learning.  The book is kept up-to-date and covers a wide range of topics in depth (up to and including sequence-to-sequence learning).
* [Getting Started with Deep Learning and Python](http://www.pyimagesearch.com/2014/09/22/getting-started-deep-learning-python/)
* [Machine Learning Mastery](http://machinelearningmastery.com/)
* [Deep Learning.net](https://web.archive.org/web/20201114013453/http://deeplearning.net/) - Aggregation site for DL resources
* [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning) - Like this Github, but ML-focused
* [FastML](http://fastml.com/)
* [Awesome Deep Learning Resources](https://github.com/guillaume-chevalier/awesome-deep-learning-resources) - Rough list of learning resources for Deep Learning
* [Professional and In-Depth Machine Learning Video Courses](https://freecoursesite.com/?s=Machine+Learning+Data+Science) - A collection of free professional and in depth Machine Learning and Data Science video tutorials and courses
* [Professional and In-Depth Artificial Intelligence Video Courses](https://freecoursesite.com/?s=Artificial+Intelligence) - A collection of free professional and in depth Artificial Intelligence video tutorials and courses
* [Professional and In-Depth Deep Learning Video Courses](https://freecoursesite.com/?s=Deep+Learning) - A collection of free professional and in depth Deep Learning video tutorials and courses
* [Introduction to Machine Learning](https://developers.google.com/machine-learning/crash-course/ml-intro) - Introductory level machine learning crash course
* [Awesome Graph Classification](https://github.com/benedekrozemberczki/awesome-graph-classification) - Learning from graph structured data
* [Awesome Community Detection](https://github.com/benedekrozemberczki/awesome-community-detection) - Clustering graph structured data
* [Awesome Decision Tree Papers](https://github.com/benedekrozemberczki/awesome-decision-tree-papers) - Decision tree papers from machine learning conferences
* [Awesome Gradient Boosting Papers](https://github.com/benedekrozemberczki/awesome-gradient-boosting-papers) - Gradient boosting papers from machine learning conferences
* [Awesome Fraud Detection Papers](https://github.com/benedekrozemberczki/awesome-fraud-detection-papers) - Fraud detection papers from machine learning conferences
* [Awesome Neural Art](https://github.com/crypdick/awesome-neural-art) - Creating art and manipulating images using deep neural networks.


## Organizations

* [IEEE Computational Intelligence Society](http://cis.ieee.org/)
* [Machine Intelligence Research Institute](https://intelligence.org/research-guide/)
* [OpenAI](https://openai.com/about/)
* [Association For The Advancement of Artificial Intelligence](http://www.aaai.org/home.html)
* [Google DeepMind Research](https://deepmind.com/research/)
* [Nvidia Deep Learning](https://developer.nvidia.com/deep-learning)
* [AI Google](https://ai.google/)
* [Facebook AI](https://ai.facebook.com)
* [IBM Research](https://www.research.ibm.com/artificial-intelligence)
* [Microsoft Research](https://www.microsoft.com/en-us/research/research-area/artificial-intelligence/)


## Journals

* [AI & Society](http://www.springer.com/journal/146)
* [AI Communications](http://iospress.metapress.com/openurl.asp?genre=journal&issn=0921-7126)
* [AI Magazine](http://www.aaai.org/Magazine/magazine.php)
* [Annals of Mathematics and Artificial Intelligence](http://www.springer.com/journal/10472)
* [Applicable Algebra in Engineering, Communication and Computing](http://www.springer.com/journal/200)
* [Applied Artificial Intelligence](https://www.tandfonline.com/toc/uaai20/current)
* [Applied Intelligence](http://www.springer.com/journal/10489)
* [Artificial Intelligence for Engineering Design, Analysis and Manufacturing](http://journals.cambridge.org/action/displayJournal?jid=AIE)
* [Artificial Intelligence Review](http://www.springer.com/journal/10462)
* [Artificial Intelligence](http://www.elsevier.com/locate/artint)
* [Automated Software Engineering](http://www.springer.com/journal/10515)
* [Autonomous Agents and Multi-Agent Systems](http://www.springer.com/journal/10458)
* [Computational and Mathematical Organization Theory ](http://www.springer.com/journal/10588)
* [Computational Intelligence](http://www.blackwellpublishing.com/content/BPL_Images/New_Journal_Samples/coin0824-7935~17~4/C.PDF)
* [Electronic Transactions on Artificial Intelligence](https://dblp.org/db/journals/etai/index.html)
* [Evolutionary Intelligence](http://www.springer.com/journal/12065)
* [EXPERT—IEEE Intelligent Systems](http://ieeexplore.ieee.org/servlet/opac?punumber=9670)
* [IEEE Transactions Automation Science and Engineering](http://www.ieee-ras.org/publications/t-ase)
* [Intelligent Industrial Systems](http://www.springer.com/engineering/robotics/journal/40903)
* [International Journal of Intelligent Systems](https://onlinelibrary.wiley.com/journal/1098111x)
* [International Journal on Artificial Intelligence Tools](https://www.worldscientific.com/worldscinet/ijait)
* [Journal of Artificial Intelligence Research](http://www.cs.washington.edu/research/)
* [Journal of Automated Reasoning](http://www.springer.com/journal/10817)
* [Journal of Experimental and Theoretical Artificial Intelligence ](https://www.tandfonline.com/toc/teta20/current)
* [Journal of Intelligent Information Systems ](http://www.springer.com/journal/10844)
* [Journal on Data Semantics ](http://www.springer.com/journal/13740)
* [Knowledge Engineering Review](http://journals.cambridge.org/action/displayJournal?jid=KER)
* [Minds and Machines](http://www.springer.com/journal/11023)
* [Progress in Artificial Intelligence ](http://www.springer.com/journal/13748)




## Courses & Articles

* [AI & ML Events](https://aiml.events) - Discover the best upcoming hand-picked events in the field of artificial intelligence and machine learning
* [Machine Learning](https://www.coursera.org/learn/machine-learning) - *Stanford University* This course provides a broad introduction to machine learning, datamining, and statistical pattern recognition. *Taught by:  Andrew Ng*
* [MIT Artifical Intelligence Videos](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/lecture-videos) - *MIT* This course includes interactive demonstrations which are intended to stimulate interest and to help students gain intuition about how artificial intelligence methods work under a variety of circumstances.
* [Machine Learning](https://class.coursera.org/ml-008) - Basic machine learning algorithms for supervised and unsupervised learning
* [Deep Learning for Natural Language Processing](https://github.com/oxford-cs-deepnlp-2017/) - *University of Oxford* This is an applied course focussing on recent advances in analysing and generating speech and text using recurrent neural networks. 
* [Deep Learning for Natural Language Processing](http://cs224d.stanford.edu/) -*Stanford University* Natural language processing (NLP) is one of the most important technologies of the information age. Understanding complex language utterances is also a crucial part of artificial intelligence. Applications of NLP are everywhere because people communicate most everything in language: web search, advertisement, emails, customer service, language translation, radiology reports, etc. 
- [Machine Learning](http://www.cs.cornell.edu/courses/CS4780/2014fa/) - *Cornell University* This course will introduce you to technologies for building data-centric information systems on the World Wide Web, show the practical applications of such systems, and discuss their design and their social and policy context by examining cross-cutting issues such as citizen science, data journalism and open government. Course work involves lectures and readings as well as weekly homework assignments, and a semester-long project in which the students demonstrate their expertise in building data-centric Web information systems.
- [Deep Learning Explained](https://www.edx.org/course/deep-learning-explained-microsoft-dat236x?source=aw&awc=6798_1500594071_04df88310f6261258691c4c3ccbb0481&utm_source=aw&utm_medium=affiliate_partner&utm_content=text-link) - *Microsoft* This course provides the level of detail needed to enable engineers / data scientists / technology managers to develop an intuitive understanding of the key concepts behind this game changing technology.
- [Machine Learning: Regression](https://www.coursera.org/learn/ml-regression?siteID=SAyYsTvLiGQ-V25BzL1BXFeL3qQswDR1PA&utm_content=10&utm_medium=partners&utm_source=linkshare&utm_campaign=SAyYsTvLiGQ) - *University of Washington* In our first case study, predicting house prices, you will create models that predict a continuous value (price) from input features (square footage, number of bedrooms and bathrooms,...). This is just one of the many places where regression can be applied.
- [Machine Learning: Clustering & Retrieval](https://www.coursera.org/learn/ml-clustering-and-retrieval?siteID=SAyYsTvLiGQ-aGMQm0rxwGdJOGehXlBV7g&utm_content=10&utm_medium=partners&utm_source=linkshare&utm_campaign=SAyYsTvLiGQ) - *University of Washington* A reader is interested in a specific news article and you want to find similar articles to recommend.  What is the right notion of similarity?  Moreover, what if there are millions of other documents?  Each time you want to a retrieve a new document, do you need to search through all other documents?  How do you group similar documents together?  How do you discover new, emerging topics that the documents cover?   
- [Neural Networks for Machine Learning](https://www.coursera.org/lecture/neural-networks-deep-learning/geoffrey-hinton-interview-dcm5r) -*University of Toronto  with Geoffrey Hinton*  Learn about artificial neural networks and how they're being used for machine learning, as applied to speech and object recognition, image segmentation, modeling language and human motion, etc. We'll emphasize both the basic algorithms and the practical tricks needed to get them to work well.
- [Machine Learning With Big Data](https://www.coursera.org/learn/big-data-machine-learning?siteID=SAyYsTvLiGQ-Y0tPwdcrYUE2YMb20wl5ww&utm_content=10&utm_medium=partners&utm_source=linkshare&utm_campaign=SAyYsTvLiGQ) -*University of California, San Diego* Need to incorporate data-driven decisions into your process? This course provides an overview of machine learning techniques to explore, analyze, and leverage data. You will be introduced to tools and algorithms you can use to create machine learning models that learn from data, and to scale those models up to big data problems.


### Artificial Intelligence

- [Introduction to Artificial Intelligence](http://ai.berkeley.edu/home.html) -*UC Berkeley* This course will introduce the basic ideas and techniques underlying the design of intelligent computer systems. A specific emphasis will be on the statistical and decision-theoretic modeling paradigm.
- [Advanced Artificial Intelligence](http://www.cs.cornell.edu/courses/CS6700/2013sp/) -*Cornell University* The design of systems that are among top 10 performers in the world (human, computer, or hybrid human-computer).
- [Artificial Intelligence (AI)](https://www.edx.org/course/artificial-intelligence-ai-columbiax-csmm-101x-1?source=aw&awc=6798_1500601821_fb8bf9bc2174fde1ff3f4738d2e41363&utm_source=aw&utm_medium=affiliate_partner&utm_content=text-link) - *Columbia University  with Professor Ansaf Salleb-Aouissi* This course will provide a broad understanding of the basic techniques for building intelligent computer systems and an understanding of how AI is applied to problems.


### Generative Adversarial Networks (GANs)

- [A Beginner's Guide to Generative Adversarial Networks (GANs)](https://skymind.ai/wiki/generative-adversarial-network-gan) - Generative adversarial networks (GANs) are deep neural net architectures comprised of two nets, pitting one against the other.

- [GAN - What is Generative Adversary Networks GAN?](https://medium.com/@jonathan_hui/gan-whats-generative-adversarial-networks-and-its-application-f39ed278ef09) - GAN is about creating, like drawing a portrait or composing a symphony. This is hard compared to other deep learning fields..


### Robotics


* [Artificial Intelligence for Robotics](https://www.udacity.com/course/artificial-intelligence-for-robotics--cs373) - *Georgia Tech*  Artificial Intelligence for Robotics by Sebastian Thrun 
- [Advanced Robotics](http://www.cs.berkeley.edu/~pabbeel/cs287-fa13/) -*UC Berkeley* The course introduces the math and algorithms underneath state-of-the-art robotic systems. The majority of these techniques are heavily based on probabilistic reasoning and optimization---two areas with wide applicability in modern Artificial Intelligence.

## Artificial Intelligence Company & Research Institute


### Business Intelligence & Analytics

* [Arago/HIRO](https://www.arago.co/hiro/) - optimise and autonomously IT and business operations
* [Arimo](https://arimo.com/) - solution to help predict customer activity and fraud
* [Ayasdi](https://www.ayasdi.com/) - a suite of intelligent applications for enterprise
* [DataRobot](https://www.datarobot.com/) - a range of products to improve enterprise products
* [Dataminr](https://www.dataminr.com/) - discovers events and breaking information before the news
* [Einstein](https://www.salesforce.com/au/products/einstein/overview/) - a smarter Salesforce
* [Fuzzy AI](https://fuzzy.ai/) - adds intelligent decision making to web and mobile apps
* [Logit.io](http://logit.io/) - visualise and manage logs and metrics with hosted ELK, Grafana & Open Distro
* [Logz.io](http://logz.io/) - helps you index, search, visualise and analyse your data
* [NXT AI](https://nxt.ai) - is a framework for temporal pattern recognition and prediction
* [Paxata](http://www.paxata.com/)] - to transform raw data into useful information automatically
* [Poweredby.ai](https://poweredby.ai/) - helps you monitor server bugs
* [Sundown](https://www.sundown.ai/home/) - automates repetitive tasks within your business
* [UBIX](http://ubix.ai/#dynamic) - making complex data science easy for enterprise
* [Student Voice](https://www.studentvoice.ai)-automatic free-text labelling for education


### Machine Learning

* [Geometric Intelligence ](https://geometricintelligence.com/) - Geometric Intelligence apart of the Uber AI Labs 
* [kaggle](https://www.kaggle.com/) - a platform for predictive modelling and analytics competitions in which companies and researchers post data and statisticians and data miners compete to produce the best models for predicting and describing the data


### Robotics
* [Boston Dynamics](https://www.bostondynamics.com) -  an engineering and robotics design company that is best known for the development of BigDog
* [iRobot](http://www.irobot.com/) - manufacturer of the famous robotic vacuum cleaner
* [DJI](http://www.dji.com/) - industry leader in drones for both commerical and industrial needs.
* [Fetch Robotics](http://www.fetchrobotics.com/) - The future of e-commerce fulfillment and R&D robots.
* [ABB Robotics](http://new.abb.com/products/robotics) - the largest manufacturer of industrial robots
* [Aldebaran Robotics](https://www.aldebaran.com/en) - creator of the [NAO robot
* [FANUC](http://www.fanucamerica.com/) - industrial robots manufacturer with the biggest install base
* [Rethink Robotics](http://www.rethinkrobotics.com/) - creator of the collaborative robot [Baxter]


### Conversational Interfaces & Chatbots
* [API.ai](https://api.ai/) - advanced tools needed to build conversational user interfaces
* [Broken Bear](https://brokenbear.com/) — a teddy bear AI for you to vent to for free, online, and anonymously.
* [Chatfuel](https://chatfuel.com/) - build a Facebook chatbot without coding
* [ChatGenius](https://chatgenius.one/) —unlock the power of Multilingual Communication
* [Comm.ai](http://comm.ai/) - add voice and chat API to websites and apps
* [Conversica](https://www.conversica.com/) - conversational interfaces to help get more sales
* [EDDI](http://eddi.labs.ai/) - create, test and deploy chatbots
* [FPT AI Platform](https://fpt.ai/) - automated interaction with end-users
* [Golem.ai](https://golem.ai) - natural language interpretation tool for developers
* [Gong](https://www.gong.io/) - analyses and improves sales conversations and discovery calls
* [Kasisto](http://kasisto.com/) - conversational AI platform for the finance industry
* [KITT.AI](http://kitt.ai/) - create conversational agents using a visual interface
* [Maluuba](http://www.maluuba.com/) - teaching machines to think, reason and communicate
* [Massively](http://massively.ai/) - build chatbots for business
* [Meya](https://meya.ai/) - build, train and host bots in one platform
* [MindMeld](https://www.mindmeld.com/) - improved version of Siri
* [Motion AI](https://www.motion.ai/) - chat bots made easy
* [msg.ai](http://txt.ai/index.html#home) - chatbot with management dashboard
* [Octane AI](https://octaneai.com/) - marketing automation for messaging
* [OpenAI Gym](https://gym.openai.com/) - open source interface to reinforcement learning tasks
* [Orbit](https://orbit.ai) - tools to help to help automate conversational AI
* [PageLines](https://www.pagelines.com?ref=hades217)-AI Agents to Enhance Your Website
* [Pool](https://pool.ai/) - personal assistant that helps you get more work done
* [Recast](https://recast.ai/) - collaborative platform to build, train, deploy intelligent bots
* [Reply.ai](https://www.reply.ai/) - platform to build and manage your conversational strategy
* [Semantic Machines](http://www.semanticmachines.com/) - conversational AI for work, travel, shop and play
* [Snips](https://snips.ai/) - add a voice Assistant to your connected product
* [Servo](http://servo.ai/) - full spectrum bot and voice which integrates with existing systems
* [UNU.ai](http://unu.ai/) - using the Swarm Intelligence (group brainpower) for chatbots
* [Unify](http://www.unify.ai/) - e-commerce chatbot
* [uTu](https://utu.ai/) - multi-channel bot analytics and data management
* [Voilà](https://www.getvoila.ai/) - AI-powered browser assistant to help you with everyday tasks
* [Wechaty](https://github.com/Chatie/wechaty) - Wechaty is a Bot Framework for Wechat Personal Account which can help you create a bot
* [Wit.ai](https://wit.ai/) - easily create text or voice based bots for preferred platform
* [Wysh](https://wysh.ai/) - enterprise scale chatbot with payment methods
* [Zero AI](http://zero.ai/) - voice interface that understands meaning, intent and context


### Data Science
* [Arize](https://arize.com/) - machine learning observability
* [BigML](https://bigml.com/) - single platform for all predictive use cases
* [CrowdFlower](https://www.crowdflower.com/) - helps with sentiment analysis, search relevance, and more
* [Dataiku](http://www.dataiku.com/) - data science platform for prototype, deploy, and run at scale
* [DataScience](https://www.datascience.com) - enterprise data science platform for R&D and production
* [Domino Data Lab](https://www.dominodatalab.com/) - platform for collaborating, building and deploying
* [Kaggle](https://www.kaggle.com/) - helps you learn, work, and play with machine learning models
* [Katonic.ai](https://katonic.ai/) - Automate your cycle of Intelligence with Katonic MLOps Platform.
* [Phoenix](https://phoenix.arize.com/) - open source library; LLM observability in a notebook
* [RapidMiner](https://rapidminer.com/) - makes data science teams more productive
* [Seldon](http://www.seldon.io/) - helps DS teams put machine learning models into production
* [Spark](http://www.sparkbeyond.com/) - research engine, capable of discovering complex patterns in data
* [Tamr](http://www.tamr.com/) - makes data unification of data silos possible
* [Trifacta](https://www.trifacta.com/) - helps put data into useful structures for analysis
* [Yhat](https://www.trifacta.com/) - allows data scientists to deploy and update predictive models rapidly
* [Yseop](https://yseop.com/) - automate the writing of reports, websites, emails, articles and more


### Development
* [AnOdot](http://www.anodot.com/) - detects business incidents
* [Bonsai](https://bons.ai/) - develop more adaptive, trusted and programmable AI models
* [Deckard.ai](http://deckard.ai/) - helps predict project timelines
* [Fuzzy.ai](http://fuzzy.ai/) - adds intelligent decision making to web and mobile apps
* [IBM Watson](http://www.ibm.com/watson/) - AI platform for business
* [Gigster](https://gigster.com/) - connecting projects with the right team
* [Kite](https://kite.com/) - augments your coding environment with web available knowledge
* [Layer 6 AI](http://layer6.ai/) - deep learning platform for prediction and personalisation
* [Morp](https://morph.ai/)h - makes developing chatbots for your business easy
* [Ozz](http://ozz.ai/) - make your bot smarter, by helping it self learn
* [RainforestQA](https://www.rainforestqa.com/) - rapidly web and mobile app testing
* [SignifAI](https://www.signifai.io/) - increase server uptime and predict downtime
* [Turtle](https://turtle.ai/) - project management and chat software that’s easy for teams
* [Neural Network](https://nnabla.org/) - Libraries by Sony. Sony demonstrates its interest in deep learning by releasing their own open source deep learning framework.
* [TensorFlow neural network playground](http://playground.tensorflow.org/) - Play with neural networks visually in your browser to get a feel for what they are and what they do.

### Vehicle
* [Vinli](https://www.vin.li/) - turns any car into a smart car
* [Apollo](http://apollo.auto/) - by Baidu. Newly launched source platform for building autonomous vehicles.


### Insurance / Legal
* [Docubot](http://aux.ai/) - can advise you on legal issues
* [Driveway](http://www.driveway.ai/) - tracks and rewards safe drivers

## Artificial Intelligence Tools


### Personal Tools

* [Amazon Echo / Alexa](https://www.amazon.com/Amazon-Echo-Bluetooth-Speaker-with-WiFi-Alexa/dp/B00X4WHP5E) - everyday personal assistant for in-home
* [Apple Siri](http://www.apple.com/ios/siri/) - everyday personal assistant on iPhone and Mac
* [Brin](https://brin.ai/) - helps you make smarter business decisions
* [Chatfuel](https://chatfuel.com/) - create a Facebook chatbot in 7 minutes
* [Findo](https://findo.com/) — smart search assistant across email, files and personal cloud.
* [Fembot](http://fembot.ai/) — your AI girlfriend
* [Fin](https://www.fin.com/) - a powerful personal assistant
* [Gatebox](http://gatebox.ai/) - a holographic anime assistant in an espresso machine
* [Google Assistant](https://assistant.google.com/) - everyday personal assistant
* [Howdy](https://howdy.ai/) - a friendly, trainable bot that helps Slack teams with work
* [Hound](http://hound.ai/) - everyday personal assistant
* [Julie Desk](https://www.juliedesk.com/) - meeting scheduling assistant (aimed at C-Suite)
* [Kono](http://kono.ai/) - meeting scheduling assistant
* [Lifos](http://simples.ai/) - dynamic independent entities that interact with the web and social
* [Ling](http://ling.ai/en/) - similar to Amazon Echo
* [Luka](https://luka.ai/) - chatbot messenger for people and other chatbots
* [Lyra](https://lyr.ai) - monitor analyse your carbon emissions
* [Magic](https://getmagic.com/) - Magic is a special phone number you text to get anything you want, hassle free
* [Microsoft Cortana](https://www.microsoft.com/en/mobile/experiences/cortana/) - Cortana is a voice-controlled virtual assistant for Microsoft Windows Phone 8.1. Comparable to Siri, the intelligent assistant enabled on Apple devices, Microsoft's Cortana will use the Bing search engine and data stored on the user's smartphone by to make personalized recommendations
* [MyWave](https://mywave.me/) - Melbourne-based which makes a personal call
* [Meeco](http://meeco.me) - Sydney-based, a robot lawyer
* Mimetic - meeting scheduling assistant
* My Ally - handles meeting scheduling and manages calendar
* [Mycroft](https://mycroft.ai/) - is the world’s first open source voice assistant
* myWave - chatbot to help you throughout your daily life
* [Remi](http://remi.ai/)— like Siri with an interface
* Replika— your AI friend that you raise through text conversations
* [Safurai](https://www.safurai.com/) - Safurai is the AI Code Assistant that saves you time in changing, optimizing, and searching code.
* SkipFlag - automatically discover and organise your work
* [Spoken](http://spoken.ai/) - virtual assistant with an interface
* Vesper - virtual assistant aimed at C-Suite
* [Viv](http://viv.ai/) - like Siri but 10x better
* [x.ai](https://x.ai/) — x.ai is a personal assistant who schedules meetings for you
* Zoom.ai - personal assistant to help you at work
* [AIHelperBot](https://aihelperbot.com/) - Build SQL queries using AI
* [ZZZ Code AI](https://zzzcode.ai/) - Get any programming question answered / code generated online


### Education Tools

* [Thirdleap](http://thirdleap.ai/) - helps children to learn maths
* [Woogie](https://woogie.ai/) - the conversational AI robot that makes learning and discovery fun for children
* [XiaoJing Bot](http://jiangren.com.au) - XiaoJing Bot to support management of wechat groups and remove members of wechat group
* [CodeKidz](https://codekidz.ai) — the first AI-powered programming learning platform for kids, featuring AI teachers to teach Python basics, problem-solving, and creativity with human-like responses


### Writing Tools

* [RightBlogger](https://rightblogger.com/) - AI-Powered Content Creation Tools for Bloggers
* [Jasperi AI](https://www.jasper.ai/) - AI writer for marketing and content teams
* [Writesonic](https://writesonic.com/) - AI writer that creates SEO-friendly content
* [Taskade AI](https://www.taskade.com) — AI outlining and mind mapping tool with collaborative editing
* [Clap](https://chatlikea.pro) — AI Writing Partner for a Distraction-Free, Seamless Typing Experience
* [Myriad](https://www.namepepper.com/free-tools/ai-content-prompt-tool) — AI prompts for writing any kind of content, like ads, scripts, webpages, email, and social


### Health / Medical Tools

* [Abi](https://abi.ai/) - your virtual health assistant
* [Ada](https://ada.com/) - can help if you’re feeling unwell
* [Airi](http://airi.ai/) - personal health coach
* [Alz.ai](https://alz.ai/) - helps you care for loved ones with Alzheimer’s
* [Bitesnap](https://getbitesnap.com/) - food recognition from meal photos to help count calories
* [doc.ai](http://doc.ai/) - makes lab results easy to understand
* [Gyan](http://gyant.com/english/) - helps you go from symptoms to likely conditions
* [Joy](http://www.hellojoy.ai/) - helps you track and improve your mental health
* Kiwi - helps you to reduce and quit smoking
* [Tess by X2AI](https://x2.ai/) — therapist in your pocket
* Sleep.ai - diagnose snoring and tooth grinding


### Travel AI Tools

* [Ada](http://fido.ai/) - chatbot that helps you navigate and make decisions
* [Emma](http://ema.ai/) — automatically calculates and adds meeting travel time
* [ETA](https://www.eta.ai/) - helps you manage travel itineraries and meetings
* [Mezi](http://mezi.com/) —helps with booking flights, hotels, restaurant reservations and more
* [Nexar](https://www.getnexar.com/) - dash cam app that helps you drive safer
* [Ready](http://ready.ai/) - traffic forecaster and travel time prediction
* [Spatial](http://spatial.ai/) - reveal the social layer of cities


### Finance AI Tools

* [Morpher AI](https://www.morpher.com/ai) - Morpher AI is a comprehensive tool for financial market analysis that acts as your personal investment analyst.
* [Abe](https://www.abe.ai/) - fast answers about your finances
* [Andy](http://andy.ai/) - a personal Tax Accountant
* [Ara](https://ara.ai/) - helps you budget
* [Bond](http://bond.ai/) - helps you achieve your financial goals
* [Mylo](https://mylo.ai/) - rounds up your everyday purchases and invest the spare change
* [Olivia]() - helps you manage your finances
* [Responsive](https://www.responsive.ai/) — institutional-grade active portfolio management
* [Roger](https://www.roger.ai/) - helps you pay bills easily
* [Xoe.ai](http://xoe.ai/) - AI lending chatbot


### Language / Translation AI Tools

* [Microsoft Translator](https://translator.microsoft.com/neural/) - language translator powered by neural networks
* [Watson.ai](http://watson.ai/) - legal, academic and financial translations


### IoT / IIoT
* [Aerial](http://www.aerial.ai/) - home activity, movement and identity sensor
* [Bridge.ai](http://bridge.ai/) - smart-home platform focused on speech and sound
* [Cubic](http://cubic.ai/) - one place to connect your smart home devices
* [Grojo](http://grow.ai/) - grow room controller and monitoring system
* [Home](http://home.ai/) - autonomous home operations with connected devices
* [Hello](http://hello.ai/) - helps you monitor and improve your sleep
* [Josh](https://www.josh.ai/) - whole house voice control
* [Mycroft](https://mycroft.ai/) - is the world’s first open source voice assistant
* [Nanit](https://www.nanit.com/) - baby monitor that measures sleep and caregiver interactions
* [Nest](https://nest.com/) - a range of in-home devices such as Thermostat, security and alarms


### Research

* [Apollo](https://apollo.ai) - breaks down articles and PDF’s into quick, readable dot points
* [Ferret.ai](http://ferret.ai/) - helps you research by summarising articles and search ability
* [Iris](http://research.ai/) - helps you research and visualise concepts in research papers


### Tools

[CaptionBot](https://www.captionbot.ai/) - Microsoft describes any photo
[Crowdfunding.ai](https://crowdfunding.ai/) — crowdfunding platform for AI projects
[Fieldguide](https://fieldguide.net/) - universal field guide that suggests possible matches

## Books

* [Reinforcement Learning: An Introduction](https://webdocs.cs.ualberta.ca/~sutton/book/the-book.html) - This introductory textbook on reinforcement learning is targeted toward engineers and scientists in artificial intelligence, operations research, neural networks, and control systems, and we hope it will also be of interest to psychologists and neuroscientists.


### Blogs, Papers, and Articles
* [Deep learning reading list](http://deeplearning.net/reading-list/) - A thorough list of academic survey papers on the subjects of reinforcement learning, computer vision, NLP & speech, disentangling factors, transfer learning, practical tricks, sparse coding, foundation theory, feedforward networks, large scale deep learning, recurrent networks, hyper parameters, optimization, and unsupervised feature learning.
* [Deep Learning in a Nutshell] - (https://devblogs.nvidia.com/parallelforall/deep-learning-nutshell-core-concepts/) - by Tim Dettmers, via NVidia (2015). These articles are digestible and do not rely heavily on math. There are 3 parts: Part 1(A gentle introduction to deep learning that covers core concepts and vocabulary). Part2 ( History of deep learning and methods of training deep learning architectures quickly and efficiently) Part 3 (Sequence learning with a focus on natural language processing)
* [TensorFlow](http://download.tensorflow.org/paper/whitepaper2015.pdf) - Large-Scale Machine Learning on Heterogeneous Distributed Systems by Google Research (2015). How TensorFlow works.


## Development

* [Caffe](http://caffe.berkeleyvision.org/) - Deep learning framework.


### Bot Development

* [Alexa Skill Kit](https://github.com/stojanovic/alexa-skill-kit) - Library for effortless Alexa Skill development with AWS Lambda
* [Facebook Messenger chatbot boilerplate](https://github.com/christophrumpel/chatbot-php-boilerplate) - PHP Facebook Messenger chatbot boilerplate
* [Facebook Messenger wit.ai node.js boilerplate](https://github.com/SimplyTechnologies/messenger-bot-wit-boilerplate) -Facebook Messenger wit.ai node.js boilerplate
* [Telegram Bot API PHP SDK](https://github.com/irazasyed/telegram-bot-sdk) - Telegram Bot API PHP SDK. Supports Laravel out of the box
* [Wechaty](https://github.com/wechaty/wechaty) - Wechaty is a Bot Framework for Wechat Personal Account which can help you create a bot
* [Node.js Messenger Bot](https://github.com/remixz/messenger-bot) - A Node client for the Facebook Messenger Platform
* [BootBot](https://github.com/Charca/bootbot) - Facebook Messenger Bot Framework for Node.js
* [Ruby Telegram bot boilerplate](https://github.com/MaximAbramchuck/ruby-telegram-bot-starter-kit)
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - This library provides a pure Python interface for the Telegram Bot API


### Haskell


### C++


### Java


### Julia


### Javascript

* [Twitter-text](https://github.com/twitter/twitter-text) - Twitter's text processing library
* [natural](https://github.com/NaturalNode/natural) - General natural language facilities for node
* [Clustering.js](https://github.com/emilbayes/clustering.js) - Clustering algorithms implemented for Node.js and the browser
* [Kmeans.js](https://github.com/emilbayes/kMeans.js) - Implementation of the k-means algorithm, for node.js and the browser
* [sylvester](https://github.com/jcoglan/sylvester) - Vector and Matrix math for JavaScript.
* [DN2A](https://github.com/dn2a/dn2a-javascript) - Digital Neural Networks Architecture
* [Knwl.js](https://github.com/loadfive/Knwl.js) - A Natural Language Processor in JS
* [NLP Compromise](https://github.com/nlp-compromise/compromise) - Natural Language processing in the browser
* [science.js](https://github.com/jasondavies/science.js/) - Scientific and statistical computing in JavaScript.
* [Machine Learning](http://joonku.com/project/machine_learning) - Machine learning library for Node.js
* [machineJS](https://github.com/ClimbsRocks/machineJS) - Automated machine learning, data formatting, ensembling, and hyperparameter optimization for competitions and exploration.
* [Node-fann](https://github.com/rlidwka/node-fann) - FANN (Fast Artificial Neural Network Library) bindings for Node.js
* [brain.js](https://github.com/harthur-org/brain.js) - Neural Networks
* [Synaptic](https://github.com/cazala/synaptic) - Neural Networks
* [Natural](https://github.com/NaturalNode/natural) - Natural Language Processing
* [ConvNetJS](http://cs.stanford.edu/people/karpathy/convnetjs/) - Convolutional Neural Networks
* [mljs](https://github.com/mljs) - A set of sub-libraries with a variety of functions
* [Neataptic](http://dnn%20execution%20framework%20o/) - Neural Networks
* [Webdnn](https://github.com/mil-tokyo/webdnn) - Deep Learning


### Python

* [Lasagne](https://github.com/Lasagne/Lasagne) - Lightweight Python library for deep learning (built on Theano).
* [LLM App](https://github.com/pathwaycom/llm-app) | Open-source Python library to build your real-time LLM-enabled data pipeline.



[conversational AI](#conversational-ai) - [All-in-one tools](#all-in-one-tools) - [AI Search Engine](#ai-search-engine) - [writing tools](#writing-tools) - [video tools](#video-tools) - [audio tools](#audio-tools) - [images tools](#images-tools) - [commerce & marketing tools](#commerce--marketing-tools) - [design tools](#design-tools) - [Coding tools](#coding-tools) - [color tools](#color-tools) - [miscellaneous](#miscellaneous)
## conversational AI
| Awesome | Description |
| --- | --- |
|[ChatGPT](https://chat.openai.com/?ref=awe50meAI) |  |
|[Poe](https://poe.com/?ref=awe50meAI) | Fast, Helpful AI Chat |
|[Chat D-ID](https://chat.d-id.com/?ref=awe50meAI) |  |
|[Dialogflow](https://cloud.google.com/dialogflow/?ref=awe50meAI) |  |
|[Watson Assistant](https://www.ibm.com/products/watson-assistant/?ref=awe50meAI) |  |
|[Microsoft Bot Framework](https://dev.botframework.com/?ref=awe50meAI) |  |
|[Rasa](https://rasa.com/?ref=awe50meAI) |     Conversational AI Platform | Superior Customer Experiences Start Here  |
|[botpress](https://botpress.com/?ref=awe50meAI) |  |
|[TARS](https://hellotars.com/?ref=awe50meAI) |  |
|[Landbot AI](https://landbot.io/ai/?ref=awe50meAI) |  |
|[SnatchBot](https://snatchbot.me/?ref=awe50meAI) |  |
|[Botstar](https://www.botstar.com/?ref=awe50meAI) |  |
|[Ask Your PDF](https://askyourpdf.com/?ref=awe50meAI) |  |
|[perplexity](https://www.perplexity.ai/?ref=awe50meAI) | Where knowledge begins |
|[Hints](https://hints.so/?ref=awe50meAI) |     AI Assistant that integrates with any software to perform tasks on your behalf  |
|[ChatSpot](https://chatspot.ai/?ref=awe50meAI) |     ChatSpot = ChatGPT + the power of HubSpot CRM  |
|[AskThee?](https://askthee.vercel.app/?ref=awe50meAI) |     Ever wanted to ask a question to a big thinker, artist or scientist? now is your chance.  |
|[Ai Chat from User.com](https://www.user.com/en/ai-chat/?ref=awe50meAI) |     Automate your customer support instantly with AI  |
|[ChatPDF](https://www.chatpdf.com/?ref=awe50meAI) |     Chat with any PDF!  |
|[Chatbase](https://www.chatbase.co/?ref=awe50meAI) |     Train ChatGPT on your data and add it to your website  |
|[Huberman AI](https://huberman.rile.yt/?ref=awe50meAI) |     Use AI to explore the wisdom of The Huberman Lab.  |
|[ai intern](https://aiintern.io/?ref=awe50meAI) |     With AI Intern skip the grind and focus on the big picture.  |
|[Chatbot UI](https://www.chatbotui.com/?ref=awe50meAI) |     Chatbot UI is an open source clone of OpenAI's ChatGPT UI.  |
|[Channel](https://www.usechannel.com/?ref=awe50meAI) |     Ask any data question, in plain English.  |
|[wonderchat](https://wonderchat.io/?ref=awe50meAI) |     Instantly build an AI chatbot with your knowledge base  |
|[Monica](https://monica.im/?ref=awe50meAI) |     YOUR CHATGPT POWERED AI ASSISTANT ON ALL WEBSITES  |
|[alicent](https://alicent.ai/?ref=awe50meAI) |     A Gorgeous Extension for ChatGPT  |
|[godmode](https://godmode.space/?ref=awe50meAI) |   |
|[PageLines](https://www.pagelines.com/?ref=awe50meAI) | AI Agents to Enhance Your Website |

## All-in-one tools
| Awesome | Description |
| --- | --- |
|[airOps](https://www.airops.com/?ref=awe50meAI) |     Deploy task-specific AI where you need it most with AirOps Apps. Install and configure in minutes, scalable, and available everywhere.  |
|[Hugging Face](https://huggingface.co/?ref=awe50meAI) |     The AI community building the future.  |
|[fotor](https://www.fotor.com/?ref=awe50meAI) |     Online photo editor for everyone  |
|[Kittl](https://www.kittl.com/?ref=awe50meAI) |     Speed up your workflows with Kittl's AI-powered design tools and gain instant access to a ton of stunning illustrations, fonts, photos, icons, and textures.  |
|[clipdrop](https://clipdrop.co/?ref=awe50meAI) |     Create stunning visuals in seconds  |
|[Replicate](https://replicate.com/?ref=awe50meAI) | Machine learning doesn’t need to be so hard. |

## AI Search Engine
| Awesome | Description |
| --- | --- |
|[phind](https://www.phind.com/?ref=awe50meAI) |     The AI search engine for developers.  |
|[you](https://you.com/?ref=awe50meAI) |     The AI Search Engine You Control  |
|[iAsk.AI](https://iask.ai/?ref=awe50meAI) |     Ask AI Questions – Free AI Search Engine  |
|[komo](https://komo.ai/?ref=awe50meAI) |     Komo search - Ai Search & Explore  |
|[Andi](https://andisearch.com/?ref=awe50meAI) |     Welcome to the next generation of search using the power of AI  |

## writing tools
| Awesome | Description |
| --- | --- |
|[Jounce](https://www.jounce.ai/?ref=awe50meAI) |     Free AI copywriting and artwork for marketers  |
|[writerly](https://writerly.ai/?ref=awe50meAI) |     Writerly artificial intelligence (AI) |    helps the most innovative businesses, teams, and creators produce hyper-relevant, SEO optimized content in seconds.  |
|[Cohesive](https://cohesive.so/?ref=awe50meAI) |     Create magical content with the most powerful AI editor  |
|[grammarly](https://www.grammarly.com/?ref=awe50meAI) |     Compose bold, clear, mistake-free writing with Grammarly’s AI-powered writing assistant.  |
|[copy ai](https://www.copy.ai/?ref=awe50meAI) |     Write better marketing copy and content with AI  |
|[jasper AI](https://www.jasper.ai/?ref=awe50meAI) |     Jasper - AI Copywriting & Content Generation for Teams  |
|[markcopy ai](https://www.markcopy.ai/?ref=awe50meAI) |     Write Content 10x Faster  |
|[rytr](https://rytr.me/?ref=awe50meAI) |     Rytr - Best AI Writer, Content Generator & Writing Assistant  |
|[simplified ai-writer](https://simplified.com/ai-writer/?ref=awe50meAI) |     Write Instant Marketing Copy with the Free AI Copywriting Generator  |
|[frase](https://www.frase.io/?ref=awe50meAI) |     Frase | Best SEO Content Optimization Tool & AI Writer  |
|[requstory](https://requstory.com/?ref=awe50meAI) |     WRITE BETTER USER STORIES.  |
|[marketmuse](https://www.marketmuse.com/?ref=awe50meAI) |     AI Content Planning and Optimization Software  |
|[wordtune](https://www.wordtune.com/?ref=awe50meAI) |     Your thoughts in words  |
|[inferkit](https://inferkit.com/?ref=awe50meAI) |     InferKit offers a web interface and API for AI–based text generators. Whether you're a novelist looking for inspiration, or an app developer, there's something for you.  |
|[goose ai](https://goose.ai/?ref=awe50meAI) |     Fully managed NLP-as-a-Service delivered via API, at 30% the cost. It's time to migrate.  |
|[writesonic](https://writesonic.com/?ref=awe50meAI) |     Writesonic - Best AI Writer, Copywriting & Paraphrasing Tool  |
|[textcortex](https://textcortex.com/?ref=awe50meAI) |     One AI Tool To Write All Your Content  |
|[ideas AI](https://ideasai.com/?ref=awe50meAI) |     Ideas on this page are 100% generated by OpenAI's GPT-3, an artifically intelligent deep learning model, without human involvement, and trained by you and 1,399,670+ other people who liked or disliked ideas.  |
|[sudowrite](https://www.sudowrite.com/?ref=awe50meAI) |     Bust writer’s block with our magical writing AI.  |
|[GhostWrite](https://www.ghostwrite.rip/?ref=awe50meAI) |     More time for the conversations that matter to you.  |
|[nichesss](https://nichesss.com/?ref=awe50meAI) |     Write anything 10x faster.  |
|[flowrite](https://www.flowrite.com/?ref=awe50meAI) |     Flowrite helps you write your daily emails and messages 5x faster across Google Chrome.  |
|[chibi ai](https://chibi.ai/?ref=awe50meAI) |     Now anyone can have a writing assistant.  |
|[copysmith](https://copysmith.ai/?ref=awe50meAI) |     Copysmith is the AI content creation solution for Enterprise & eCommerce  |
|[copymatic ai](https://copymatic.ai/?ref=awe50meAI) |     Generate Content & Copy In Seconds with AI  |
|[hypotenuse](https://www.hypotenuse.ai/?ref=awe50meAI) |     Let AI write your content in seconds. Without writer’s block.  |
|[longshot ai](https://www.longshot.ai/?ref=awe50meAI) |     Create blogs that humans and search engines love using Artificial Intelligence  |
|[unbounce smart copy](https://unbounce.com/product/smart-copy/?ref=awe50meAI) |     Wherever You Type, Smart Copy Writes  |
|[scalenut](https://www.scalenut.com/?ref=awe50meAI) |     Tell Better Stories at Scale  |
|[NeuralText](https://www.neuraltext.com/?ref=awe50meAI) |     NeuralText - AI Writing Assistant and tools for SEO  |
|[closerscopy](https://www.closerscopy.com/?ref=awe50meAI) |     AI Copywriting Robot - ClosersCopy  |
|[inkforall](https://inkforall.com/?ref=awe50meAI) |     INK – World’s Best AI Content Assistant for Marketing & SEO  |
|[peppertype](https://www.peppertype.ai/?ref=awe50meAI) |     Create Quality Content Faster  |
|[ai-writer](https://ai-writer.com/?ref=awe50meAI) |     AI-Writer is the most accurate content generation platform, using state-of-the-art AI writing models to generate articles from just a headline.  |
|[GetGenie](https://getgenie.ai/?ref=awe50meAI) |     The WordPress AI SuperApp for Content & SEO | GetGenie  |
|[Article Forge](https://www.articleforge.com/?ref=awe50meAI) |     High quality, AI content generator - Article Forge  |
|[ProWritingAid](https://prowritingaid.com/?ref=awe50meAI) |     ProWritingAid: AI Writing Assistant Software  |
|[QuillBot](https://quillbot.com/?ref=awe50meAI) |     QuillBot's AI-powered paraphrasing tool will enhance your writing  |
|[WriterZen](https://writerzen.net/?ref=awe50meAI) |     Proficient SEO Content Workflow Software  |
|[Writecream](https://www.writecream.com/?ref=awe50meAI) |     Writecream - Best AI Writer & Content Generator - Writecream  |
|[outranking](https://www.outranking.io/?ref=awe50meAI) |     Outranking helps content teams achieve predictable content success with AI assistance.  |
|[lately](https://www.lately.ai/?ref=awe50meAI) |     Spend 84% Less Time Writing Content  |
|[wordai](https://wordai.com/?ref=awe50meAI) |     10x Your Content Output With AI.  |
|[craftly](https://www.craftly.ai/?ref=awe50meAI) |     Changing the way the world writes.  |
|[SEO AI](https://seo.ai/?ref=awe50meAI) |     The #1 AI Writer For SEO  |
|[content at scale](https://contentatscale.ai/?ref=awe50meAI) |     AI Content Generator for Quality SEO Long Form Blog Posts  |
|[jenni](https://jenni.ai/?ref=awe50meAI) |     Supercharge your writing with jenni AI  |
|[Taskade](https://taskade.com/?ref=awe50meAI) |     AI outlining and mind mapping tool for teams with real-time editing and chat.  |
|[wordkraft](https://wordkraft.ai/?ref=awe50meAI) |     Create High-Quality Content Instantly With AI  |
|[merlin](https://merlin.foyer.work/?ref=awe50meAI) |     Open AI’s GPT powered extension to use anywhere!  |
|[kickresume](https://www.kickresume.com/en/?ref=awe50meAI) |     Let artificial intelligence write your resume.  |
|[AISEO](https://aiseo.ai/?ref=awe50meAI) |     AISEO - AI writing assistant, Copywriting & Paraphrasing Tool  |
|[yaara.ai](https://yaara.ai/?ref=awe50meAI) |     The Future Of Writing is Finally Here  |
|[ChatGPT Writer](https://chatgptwriter.ai/?ref=Awe50meAI) |     Free Chrome extension to generate entire emails and messages using ChatGPT AI. All sites are supported and enhanced support for Gmail.  |
|[FocusFlow](https://focusflow.ai/?ref=awe50meAI) |     Track your daily progress, highlights, and improvements in just 20 seconds.  |
|[NovelAI](https://novelai.net/?ref=awe50meAI) |     The AI Storyteller  |
|[narrato](https://narrato.io/?ref=awe50meAI) |     AI Content Creation and Collaboration Platform  |
|[WriteMe](https://writeme.ai/?ref=awe50meAI) |     WriteMe.ai - Ai Writer - Content Writing Assistant & Creator  |
|[Magical AI](https://www.getmagical.com/ai?ref=awe50meAI) |     Call on Magical AI to do all the work stuff you hate doing. Create messages from scratch, update forms instantly, and automate annoying tasks—anywhere, anytime.  |
|[Bearly](https://bearly.ai/?ref=awe50meAI) |     Bearly makes you 10x faster by adding the state of the art AI to your workflow. Reading, writing, and content creation all one shortcut away.  |
|[StealthGPT](https://www.stealthgpt.ai/?ref=awe50meAI) |     Write Using AI, Get Human Written Results  |
|[resume worded](https://resumeworded.com/?ref=awe50meAI) |     Improve your resume and LinkedIn profile  |
|[detangle](https://detangle.ai/?ref=awe50meAI) |     Summarize any video, audio or text  |
|[melville](https://usemelville.com/?ref=awe50meAI) |     Create amazing show notes 10x faster with AI.  |
|[Swell AI](https://www.swellai.com/?ref=awe50meAI) |     Automate writing podcast show notes, articles, social posts and more.  |
|[Scalenut](https://www.scalenut.com/?ref=awe50meAI) |     Scalenut: AI powered SEO and Content Marketing Platform  |
|[Sheet+](https://sheetplus.ai/) |     Write Google Sheets & Excel formulas 10x faster with AI  |
|[FinalScout](https://finalscout.com/?ref=awe50meAI) |     ChatGPT-Powered Email Finding & Outreach at Scale  |
|[HyperWrite](https://www.hyperwriteai.com/?ref=awe50meAI) |     Your personal AI writing assistant  |
|[maker.ai](https://maker.ai/?ref=awe50meAI) |     Generate written & visual content in seconds through cutting-edge artificial intelligence. Make magical conten  |
|[Thundercontent](https://thundercontent.com/?ref=awe50meAI) |     Create any content with Artificial Intelligence in minutes  |
|[Autowrite app](https://autowrite.app/?ref=awe50meAI) |    Create Human-like Search Engine Optimized Articles|
|[postGenius](https://www.postgeniusapp.com/?ref=awe50meAI) |    Generate your next post using chatGPT  |
|[postwise](https://postwise.ai/?ref=awe50meAI) |  Write Viral Tweets in Seconds |
|[WriteSparkle](https://writesparkle.ai/?ref=awe50meAI) |  Discover AI-Driven Brilliance, streamline your content creation process by seamlessly integrating Writesparkle with your favorite tools and platforms.  |
|[flawlessly ai](https://flawlessly.ai/?ref=awe50meAI) |  Flawlessly.Ai transforms your spelling, grammar, tone, and style into professional text in seconds. |
|[PDFPeer](https://pdfpeer.com/) |  Engage with your PDFs: summarize, ask questions, and simplify tasks! |

## video tools
| Awesome | Description |
| --- | --- |
|[Deepbrain ai - ai studios](https://www.deepbrain.io/aistudios?ref=awe50meAI) |     Create AI-generated videos using basic text instantly  |
|[Supercreator.ai](https://www.supercreator.ai/?ref=awe50meAI) |     Create short form videos 10x faster using artificial intelligence  |
|[veed io](https://www.veed.io/?ref=awe50meAI) |     VEED - Edit, Record & Livestream Video - Online  |
|[runway](https://runwayml.com/?ref=awe50meAI) |     Everything you need to make content, fast.  |
|[Fliki](https://fliki.ai/?ref=awe50meAI) |     Turn text into videos with AI voices  |
|[synthesia](https://www.synthesia.io/?ref=awe50meAI) |     Create videos from plain text in minutes  |
|[descript](https://www.descript.com/?ref=awe50meAI) |     All-in-one video & audio editing, as easy as a doc.  |
|[typecast ai](https://typecast.ai/?ref=awe50meAI) |     Video creation made simple with AI voices and avatars  |
|[bhuman ai](https://www.bhuman.ai/?ref=awe50meAI) |     Produce a single video and personalize it for thousands of recipients. Deliver over any channel and measure results instantly.  |
|[Jellysmack](https://jellysmack.com/?ref=awe50meAI) |     Creator Content Amplification & Solutions | Jellysmack  |
|[plask](https://plask.ai/?ref=awe50meAI) |     AI-powered Mocap Animation Tool  |
|[Rokoko video](https://www.rokoko.com/products/video/?ref=awe50meAI) |     Rokoko Video Free AI motion capture  |
|[Topaz Video AI](https://www.topazlabs.com/topaz-video-ai/?ref=awe50meAI) |     Production-grade AI models for professional use cases  |
|[Steve AI](https://www.steve.ai/?ref=awe50meAI) |     Free AI Video Maker App | Online Video Making Software Tool  |
|[elai](https://elai.io/?ref=awe50meAI) |     Create AI videos from just text.  |
|[pictory](https://pictory.ai/?ref=awe50meAI) |     Video Marketing Made EASY  |
|[Lumen5](https://lumen5.com/?ref=awe50meAI) |     Lumen5 - Video Maker | Create Videos Online in Minutes  |
|[wisecut](https://www.wisecut.video/?ref=awe50meAI) |     Wisecut | Automatic Video Editor  |
|[synths video](https://synths.video/?ref=awe50meAI) |     Convert articles into video in 1-click  |
|[invideo](https://invideo.io/?ref=awe50meAI) |     Create publish-worthy videos on day one  |
|[GliaCloud](https://www.gliacloud.com/en/?ref=awe50meAI) |     Generate videos from news content, social posts, live sport events, and statistical data in minutes!  |
|[synthesys](https://synthesys.io/ai-video/?ref=awe50meAI) |     Transform Your Text to a Realistic Virtual Video  |
|[beey](https://www.beey.io/en/?ref=awe50meAI) |     Beey.io – Beey automatically converts your audio and video files to text.  |
|[papercup](https://www.papercup.com/?ref=awe50meAI) |     AI Powered Dubbing  |
|[Friday](https://www.heyfriday.ai/home/?ref=awe50meAI) |     Less Writing, More Inspiration.  |
|[Movio](https://www.movio.la/?ref=awe50meAI) |     Create Engaging Videos 10x Faster with AI  |
|[clip.fm](https://www.clip.fm/?ref=awe50meAI) |     Turn podcasts into viral clips with one click.  |
|[D-ID](https://www.d-id.com/?ref=awe50meAI) |     Digital People Text-to-Video  |
|[vidyo.ai](https://vidyo.ai/?ref=awe50meAI) |     Make short videos from long ones instantly  |
|[Rephrase Studio](https://www.rephrase.ai/studio/?ref=awe50meAI) |     Rephrase Studio is a self-serve text-to-video generation platform that eliminates the complexity of video production, enabling you to create professional-looking videos at scale.  |
|[Genmo](https://alpha.genmo.ai/?ref=awe50meAI) |     Go beyond 2D. Create videos from text with AI.  |
|[riverside](https://riverside.fm/?ref=awe50meAI) |     Automatically transcribe your audio and video recordings in seconds with our AI-powered technology. It's accurate, reliable, and supports more than 100 languages.  |
|[Zoomscape.ai](https://zoomscape.ai/?ref=awe50meAI) |     Create stunning Zoom backgrounds with AI  |
|[Morise.ai](https://morise.ai/?ref=awe50meAI) |     You make the videos, AI will make them go viral  |
|[Rask](https://www.rask.ai/?ref=awe50meAI) |     Localize videos. Fast. Fun. With AI  |
|[HeyGen](https://www.heygen.com/) |     CREATE ENGAGING VIDEOS 10X FASTER WITH AI  |
|[2short.ai](https://2short.ai/?ref=awe50meAI) |     Elevate your YT content with AI generated shorts |
|[Eightify](https://eightify.app/?ref=awe50meAI) |  YouTube summaries powered by ChatGPT |

## audio tools
| Awesome | Description |
| --- | --- |
|[Adobe Podcast](https://podcast.adobe.com/?ref=awe50meAI) |     AI-powered audio recording and editing, all on the web  |
|[play ht](https://play.ht/?ref=awe50meAI) |     AI powered text to voice generator  |
|[Murf AI](https://murf.ai/?ref=awe50meAI) |     AI Voice Generator: Versatile Text to Speech Software | Murf AI  |
|[resemble ai](https://www.resemble.ai/?ref=awe50meAI) |     Your Complete Generative Voice AI Toolkit  |
|[wellsaid](https://wellsaidlabs.com/?ref=awe50meAI) |     Convert text to voice in real time  |
|[voicemod](https://www.voicemod.net/?ref=awe50meAI) |     Free Real-Time Voice Changer  |
|[assemblyai](https://www.assemblyai.com/?ref=awe50meAI) |     Transcribe and understand audio with a single AI-powered API  |
|[songdonkey](https://songdonkey.ai/?ref=awe50meAI) |     Extract vocals and instruments with artificial intelligence  |
|[krisp ai](https://krisp.ai/?ref=awe50meAI) |     Krisp’s AI removes background voices, noises and echo from all your calls, giving you peace of mind.  |
|[aloud](https://aloud.area120.google.com/?ref=awe50meAI) |     Aloud - dubbing for everyone  |
|[listnr](https://www.listnr.tech/?ref=awe50meAI) |     Generate realistic Text to Speech (TTS) audio using our AI Voice Generator with the best synthetic voices.   |
|[lovo](https://www.lovo.ai/?ref=awe50meAI) |     LOVO AI | Free Text to Speech Online with Natural Voices  |
|[speechelo](https://speechelo.com/?ref=awe50meAI) |     Instantly Generate Voice from Text 100% Human-Sounding voiceover with only 3 clicks!  |
|[bigspeak](https://bigspeak.ai/?ref=awe50meAI) |     Generate English speech from text  |
|[speechify](https://speechify.com/?ref=awe50meAI) |     Power through docs, articles, PDFs, email — anything you read — by listening with our leading text-to-speech reader.  |
|[sonix ai](https://sonix.ai/?ref=awe50meAI) |     Automatically convert audio and video to text: Fast, Accurate, & Affordable | Sonix  |
|[speak ai](https://speakai.co/?ref=awe50meAI) |     Get transcription, research, data analysis and NLP software from Speak Ai  |
|[rev com](https://www.rev.com/?ref=awe50meAI) |     Transcribe Speech to Text  |
|[scribie](https://scribie.com/?ref=awe50meAI) |     Audio/Video Transcription | 99% Accuracy, 12-HR Turnaround  |
|[verbit](https://verbit.ai/?ref=awe50meAI) |     Captioning & Transcription That’s Built for Business  |
|[fireflies](https://fireflies.ai/?ref=awe50meAI) |     Automatically record and transcribe meetings  |
|[otter](https://otter.ai/?ref=awe50meAI) |     Capture and share insights from your meetings  |
|[voicera](https://www.voicera.co/?ref=awe50meAI) |     Give voice to your articles and blogs.  |
|[revoicer](https://revoicer.com/?ref=awe50meAI) |     The most realistic AI Text To Speech online  |
|[elevenlabs](https://beta.elevenlabs.io/?ref=awe50meAI) |     The most realistic and versatile AI speech software, ever. Eleven brings the most compelling, rich and lifelike voices to creators and publishers seeking the ultimate tools for storytelling.  |
|[soundraw](https://soundraw.io/?ref=awe50meAI) |     AI Music Generator  |
|[VoicePen](https://voicepen.ai/?ref=awe50meAI) |     Audio to Blog Post, in minutes  |
|[podcastle](https://podcastle.ai/?ref=awe50meAI) |     The One-Stop Shop for Broadcast Storytelling  |
|[beatoven.ai](https://www.beatoven.ai/?ref=awe50meAI) |     Create customisable royalty free music that elevates your story  |
|[altered](https://www.altered.ai/?ref=awe50meAI) |     Professional Ai Voice Changer Software and Services | Altered  |
|[Mubert](https://mubert.com/?ref=awe50meAI) |     Human AI Generative Music For your video content, podcasts and apps  |
|[listener.fm](https://www.listener.fm/?ref=awe50meAI) |     Elevate Your Podcast Post-Production Process with AI-Generated Titles, Descriptions, and Show Notes  |
|[Shownotes](https://www.shownotes.io/?ref=awe50meAI) |     Summarize a podcast episode with help from chatGPT.  |
|[Mood](https://usemood.us/?ref=awe50meAI) |     Amplify your podcast to 1 billion audiences with generative AI.  |
|[Cleanvoice](https://cleanvoice.ai/?ref=awe50meAI) |     Cleanvoice is an artificial intelligence which removes filler sounds, stuttering and mouth sounds from your podcast or audio recording  |
|[snipd - AI Podcast Summaries](https://www.snipd.com/ai-podcast-summaries/?ref=awe50meAI) |     Introducing Snipd's AI-generated Podcast  Summaries  |
|[koolio.ai](https://www.koolio.ai/?ref=awe50meAI) |     the future of podcast creation.  |
|[sumly.ai](https://www.sumly.ai/?ref=awe50meAI) |     AI-generated podcast summaries delivered straight to your inbox.  |
|[podsqueeze](https://podsqueeze.com/?ref=awe50meAI) |     Generate shownotes, timestamps, newsletters and more for your podcast with one click!  |
|[Dubb](https://www.dubb.media/?ref=awe50meAI) |     An automated, easy-to-use assistant that generates marketing content for your podcast. Dubb turns your podcast episodes into show notes, social media posts, newsletter content, transcripts, and more.  |
|[deciphr](https://www.deciphr.ai/?ref=awe50meAI) |     Powered by deep AI, Deciphr timestamps and summarizes your entire podcast transcript for you. In less time than it takes to make coffee. And it's completely free.  |
|[type studio](https://www.typestudio.co/?ref=awe50meAI) |     Type Studio is a fast, simple, and joyful way to edit and grow your podcasts, streams, and interviews.  |
|[steosvoice](https://cybervoice.io/en/?ref=awe50meAI) |     Your High-Quality Neural Voice AI  |
|[fathom](https://hello.fathom.fm/?ref=awe50meAI) |     Discover podcasts at the speed of thought with mind-blowing AI-powered Search, Transcripts, Chapters, Clipping, and Highlights.  |
|[wavtool](https://wavtool.com/?ref=awe50meAI) | AI-accelerated music production. Make high-quality music with an AI assistant. In the browser, for free. |
|[decoherence](https://www.decoherence.co/?ref=awe50meAI) | Make AI Music Videos |

## images tools
| Awesome | Description |
| --- | --- |
|[letsenhance](https://letsenhance.io/?ref=awe50meAI) |     Automatic AI editor to increase image resolution without losing quality  |
|[facet ai](https://facet.ai/?ref=awe50meAI) |     Facet is the first AI-powered image editor, empowering artists to do what they do best: create.  |
|[remove bg](https://www.remove.bg/?ref=awe50meAI) |     Remove backgrounds 100% automatically in 5 seconds with one click  |
|[ProPhotos](https://prophotos.ai/?ref=awe50meAI) | Upgrade your professional image with AI-powered headshots. |
|[remini ai](https://remini.ai/?ref=awe50meAI) |     The only photo enhancer you'll ever need  |
|[avatar ai](https://avatarai.me/?ref=awe50meAI) |     Create your own photorealistic AI Avatars  |
|[photosonic](https://photosonic.writesonic.com/?ref=awe50meAI) |     The AI that paints your dreams with pixels - for FREE.  |
|[ai picasso](https://aipicasso.studio.site/?ref=awe50meAI) |     Create Art with Powerful AI  |
|[upscale](https://www.upscale.media/?ref=awe50meAI) |     Upscale and Enhance Your Images for FREE  |
|[ai image enlarger](https://imglarger.com/?ref=awe50meAI) |     All-in-one AI toolkits help you enhance and upscale images. Increases image resolution without losing quality  |
|[DeOldify](https://github.com/jantic/DeOldify/?ref=awe50meAI) |     A Deep Learning based project for colorizing and restoring old images (and video!)   |
|[imagecolorizer](https://imagecolorizer.com/?ref=awe50meAI) |     We use AI technology to restore old photos automatically  |
|[evoto](https://www.evoto.ai/?ref=awe50meAI) |     EVOTO, AI-powered Image Editor  |
|[imagineme](https://imagineme.app/ref/3/?ref=awe50meAI) |     Personal AI Art Generator  |
|[restorephotos.io](https://www.restorephotos.io/?ref=awe50meAI) |     Restoring old photos using AI for everyone.  |
|[booth ai](https://www.booth.ai/?ref=awe50meAI) |     Create pro quality product photography with AI  |
|[phosus](https://phosus.com/?ref=awe50meAI) |     AI-Powered Image Enhancement Tools and API Provider | Phosus  |
|[Vance.AI](https://vance.ai/?ref=awe50meAI) |     Upscale Image with AI  |
|[Image Creator from Microsoft Bing](https://www.bing.com/images/create/?ref=awe50meAI) |     Create images from words with AI  |
|[BlueWillow](https://www.bluewillow.ai/?ref=awe50meAI) |     BlueWillow | Free AI Art Generator  |
|[Nero AI](https://ai.nero.com/?ref=awe50meAI) |     Enlarge your images without losing quality, automatically detect thousands of images and categorize your albums.  |
|[removal.ai](https://removal.ai/?ref=awe50meAI) |     Remove Background From Image for Free Using Artificial Intelligence  |
|[ZMO.AI](https://www.zmo.ai/background-ai/?ref=awe50meAI) |     Background Generator & Remover | Background AI  |
|[Stable Diffusion](https://stablediffusionweb.com/?ref=awe50meAI) |     Stable Diffusion is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input, cultivates autonomous freedom to produce incredible imagery, empowers billions of people to create stunning art within seconds.  |
|[Playground AI](https://playgroundai.com/?ref=awe50meAI) | Create any image from your imagination |
|[VectorArt.ai](https://vectorart.ai/?ref=awe50meAI) | Create vector images with AI |

## commerce & marketing tools
| Awesome | Description |
| --- | --- |
|[syte ai](https://www.syte.ai/?ref=awe50meAI) |     The World's #1 Product Discovery Platform for eCommerce  |
|[nureply](https://nureply.com/?ref=awe50meAI) |     Get 2.4x More Replies and Revenue with Cold Emails Powered by Advanced AI  |
|[zia by zoho](https://www.zoho.com/zia/?ref=awe50meAI) |     Meet Zia, the AI-powered assistant for your business  |
|[Adzis app](https://app.adzis.com/?ref=awe50meAI) |     AI Content Generator App for eCommerce - Adzis  |
|[ocaya](https://www.ocoya.com/?ref=awe50meAI) |     Become a Social Media Genius  |
|[On-Page.ai](https://on-page.ai/?ref=awe50meAI) |     On-Page SEO Optimization Tool Helps You Rank - On-Page.ai  |
|[sapling](https://sapling.ai/?ref=awe50meAI) |     AI messaging assistant for customer-facing teams. Respond twice as fast.  |
|[heyday](https://heyday.hootsuite.com/?ref=awe50meAI) |     Drive more e-commerce sales and deliver five-star customer service at scale with our conversational AI chatbot.  |
|[linkfluence](https://www.linkfluence.com/?ref=awe50meAI) |     Enterprise Social Intelligence at Scale  |
|[phrasee](https://phrasee.co/?ref=awe50meAI) |     Get more clicks, conversions, and customers with AI-optimized content  |
|[human marketing](https://ai.human.marketing/?ref=awe50meAI) |     AI Marketing Software That Gets Predictably Better Results  |
|[acrolinx](https://www.acrolinx.com/?ref=awe50meAI) |     The road to happy customers is paved with amazing content  |
|[marketmuse](https://www.marketmuse.com/?ref=awe50meAI) |     Most content strategies are built on generic data and opinions.  |
|[liveperson](https://www.liveperson.com/?ref=awe50meAI) |     Conversational AI that’s anything but artificial  |
|[albert](https://albert.ai/?ref=awe50meAI) |     albert is your self-learning digital marketing ally  |
|[clickable](https://www.clickable.so/?ref=awe50meAI) |     Generate ads in seconds with AI  |
|[Robin](https://www.hellorobin.ai/?ref=awe50meAI) |     The Future of Sales Automation.  |
|[cody](https://www.meetcody.ai/?ref=awe50meAI) |     Cody is an intelligent AI assistant like ChatGPT – with the added benefit of being able to train it on your business, your team, your processes, and your clients with your own knowledge base. Use Cody to support your team, answer questions, help with creative work, troubleshoot issues, and brainstorm ideas.  |
|[Tugan.ai](https://www.tugan.ai/?ref=awe50meAI) |     Enter a URL or TOPIC To Generate Your Marketing Emails Instantly With AI  |
|[Marketing Co-pilot AI](https://marketingcopilotai.com/?ref=awe50meAI) | The Better Way to Do Marketing |
|[Domains GPT](https://oneword.domains/domains-gpt/?ref=awe50meAI) | Generate brandable & memorable domain names using AI. Powered by OpenAI and Vercel Edge Functions. |

## design tools
| Awesome | Description |
| --- | --- |
|[PhotoRoom](https://www.photoroom.com/?ref=awe50meAI) |     PhotoRoom - Remove Background and Create Product Pictures  |
|[IconifyAI.com](https://www.iconifyai.com/?ref=awe50meAI) |     Create an Icon that truly represents your app with AI  |
|[beautiful ai](https://www.beautiful.ai/?ref=awe50meAI) |     Presentation software that designs for you.  |
|[avatarai](https://avatarai.me/?ref=awe50meAI) |     Create your own AI-generated avatars  |
|[profilepicture](https://www.profilepicture.ai/?ref=awe50meAI) |  |
|[picofme](https://picofme.io/?ref=awe50meAI) |     Just AI profile picture maker  |
|[withpoly](https://withpoly.com/?ref=awe50meAI) |     Generate 3D Design Assets in Seconds with AI  |
|[craiyon](https://www.craiyon.com/?ref=awe50meAI) |     Free online AI image generator from text  |
|[neural love](https://neural.love/?ref=awe50meAI) |     Online video, images and audio enhancement powered by AI | neural.love  |
|[Imagen AI](https://imagen-ai.com/?ref=awe50meAI) |     Imagen - Personalized Photo Editing Assistant  |
|[nightcafe studio](https://nightcafe.studio/?ref=awe50meAI) |     AI Art Generator  |
|[autodraw](https://www.autodraw.com/?ref=awe50meAI) |     AutoDraw is a new kind of drawing tool. It pairs machine learning with drawings from talented artists to help everyone create anything visual, fast.  |
|[ai draw](https://ai-draw.tokyo/en/?ref=awe50meAI) |     Convert your photo into line drawing.  |
|[hotpot ai](https://hotpot.ai/?ref=awe50meAI) |     Hotpot helps you create amazing graphics, pictures, and text.  |
|[pixray text to image / pixel art](https://pixray.gob.io/?ref=awe50meAI) |  |
|[designs ai](https://designs.ai/?ref=awe50meAI) |     Create logos, videos, banners, mockups with A.I. in 2 minutes  |
|[durable website builder](https://durable.co/ai-website-builder/?ref=awe50meAI) |     Build a website in 30 seconds using artificial intelligence  |
|[makelogo ai](https://makelogoai.com/?ref=awe50meAI) |     Uniques logos, for less than a coffee  |
|[nightcafe](https://creator.nightcafe.studio/?ref=awe50meAI) |     Create amazing artworks using the power of Artificial Intelligence.  |
|[DALL·E 2 ](https://openai.com/dall-e-2/?ref=awe50meAI) |     DALL·E 2 is a new AI system that can create realistic images and art from a description in natural language.   |
|[deep dream generator](https://deepdreamgenerator.com/?ref=awe50meAI) |     HUMAN AI COLLABORATION  |
|[dream ai](https://dream.ai/?ref=awe50meAI) |     High Quality Artwork In Seconds  |
|[starryai](https://starryai.com/?ref=awe50meAI) |     Create Art with AI  |
|[artbreeder](https://www.artbreeder.com/?ref=awe50meAI) |     craft ai art like never before  |
|[looka](https://looka.com/?ref=awe50meAI) |     Use Looka's AI-powered platform to design a logo and build a brand you love.  |
|[logoAI](https://www.logoai.com/?ref=awe50meAI) |     Let AI-powered logo maker generate your new logo, create matching stationery, and design a brand you love!  |
|[logomaster AI](https://logomaster.ai/?ref=awe50meAI) |     Powered by AI,logomaster.ai helps business owners create beautiful logos.  |
|[durable](https://durable.co/?ref=awe50meAI) |     The AI website builder that generates an entire business website with images and copy in seconds.  |
|[midjourney](https://midjourney.com/?ref=awe50meAI) |  |
|[magicstudio](https://magicstudio.com/?ref=awe50meAI) |     Powered by AI, Created by You  |
|[pfpmaker](https://pfpmaker.com/?ref=awe50meAI) |     Make your new profile picture with AI  |
|[uizard](https://uizard.io/?ref=awe50meAI) |     Uizard | App, Web, & UI Design Made Easy | Powered By AI  |
|[ando](https://ando.studio/?ref=awe50meAI) |     Your AI design copilot.  |
|[pixelz](https://pixelz.ai/?ref=awe50meAI) |     PIXELZ AI AVATAR & IMAGE GENERATOR  |
|[makelogoai](https://makelogo.ai/?ref=awe50meAI) |     Make Unique logos with AI.  |
|[flair](https://withflair.ai/?ref=awe50meAI) |     the AI Design Tool for Branded Content.  |
|[magician](https://magician.design/?ref=awe50meAI) |     A magical design tool for Figma powered by AI.  |
|[Galileo AI](https://www.usegalileo.ai/?ref=awe50meAI) |     Galileo AI creates delightful, editable UI designs from a simple text description. It empowers you to design faster than ever.  |
|[stockimg](https://stockimg.ai/?ref=awe50meAI) |     AI image generation for teams - You can easily generate AI logo, AI book covers, AI posters and more - Stockimg AI  |
|[pixlr](https://pixlr.com/?ref=awe50meAI) |     AI powered photo editor, animation and design.  |
|[brandmark](https://brandmark.io/?ref=awe50meAI) |     Brandmark Logo Maker - the most advanced AI logo design tool  |
|[illustroke](https://illustroke.com/?ref=awe50meAI) |     Stunning vector illustrations from text prompts  |
|[slides AI](https://www.slidesai.io/?ref=awe50meAI) |     Create Presentations Slides with AI in seconds  |
|[Cleanup.pictures](https://cleanup.pictures/?ref=awe50meAI) |     Remove any unwanted object, defect, people or text from your pictures in seconds  |
|[SnapEdit](https://snapedit.app/?ref=awe50meAI) |     Remove Object from photo  |
|[UI-AI](https://ui-ai.com/) |     User Interface Artificial Intelligence  |
|[Whimsical AI for Mind Maps](https://whimsical.com/ai-mind-maps/?ref=awe50meAI) |     Fresh ideas at your fingertips  |
|[Adobe Firefly](https://www.adobe.com/sensei/generative-ai/firefly.html/?ref=Awe50meAI) |     AI Art Generator  |
|[AILab Tools](https://www.ailabtools.com/?ref=awe50meAI) |  |
|[IMGCREATOR](https://imgcreator.zmo.ai/?ref=awe50meAI0) |     All-in-one AI Design Art Generator  |
|[vizcom](https://www.vizcom.ai/?ref=awe50meAI) |     see your drawings come to life in seconds.  |
|[storyd](https://www.storyd.ai/?ref=awe50meAI) |     AI POWERED PRESENTATIONS  |
|[PicWish](https://picwish.com/?ref=awe50meAI) |     PicWish AI Photo Editor | Free Online Photo Editing Tools  |
|[Figma AI](https://www.figmaai.io/?ref=awe50meAI) |     Integrate GPT Chat into your Figma workflow  |
|[DreamStudio](https://beta.dreamstudio.ai/?ref=awe50meAI) |     Tap into the power of our generative text-to-image suite to create new and unique designs.  |
|[Leonardo.Ai](https://leonardo.ai/?ref=awe50meAI) |     Create stunning game assets with AI.  |
|[Spline AI](https://spline.design/ai/?ref=awe50meAI) |     The power of AI is coming to the 3rd dimension. Generate objects, animations, and textures using prompts.  |
|[NVIDIA Canvas](https://www.nvidia.com/en-us/studio/canvas/?ref=awe50meAI) |     Use AI to turn simple brushstrokes into realistic landscape images. Create backgrounds quickly, or speed up your concept exploration so you can spend more time visualizing ideas.  |
|[Thumbly](https://thumbly.ai/?ref=awe50meAI) | Create YouTube thumbnails that get clicks |
|[stylized](https://www.stylized.ai/?ref=awe50meAI) | A new way to take product photos. |

## Coding tools
| Awesome | Description |
| --- | --- |
|[GitHub copilot](https://github.com/features/copilot/?ref=awe50meAI) |     Your AI pair programmer  |
|[tabnine](https://www.tabnine.com/?ref=awe50meAI) |     AI assistant for software developers  |
|[deepOpinion](https://go.deepopinion.ai/?ref=awe50meAI) |     No-code AI for automation professionals  |
|[Amazon CodeWhisperer](https://aws.amazon.com/codewhisperer/?ref=awe50meAI) | Build applications faster and more securely with your AI coding companion |
|[Android Studio Bot](https://developer.android.com/studio/preview/studio-bot/?ref=awe50meAI) | Studio Bot is your coding companion for Android development. |
|[Flatlogic](https://flatlogic.com/blog/chatgpt-flatlogic-generate-fully-functioning-web-apps-based-on-description) |     generate fully-functioning web apps in minutes with OpenAI, simply by describing the app in English!  |
|[Code Mentor AI](https://code-mentor.ai?ref=awe50meAI) | Start coding smarter today with the ultimate explainer tool based on Artificial Intelligence for optimizing, refactoring, and reviewing code! |
|[Fronty](https://fronty.com/?ref=awe50meAI) |     convert image to HTML CSS  |
|[SourceAI](https://sourceai.dev/?ref=awe50meAI) |     Ai-Powered Code Generator  |
|[Microapp](https://www.microapp.ai/build) |     AI-Powered Component Generator  |
|[GitFluence](https://www.gitfluence.com/?ref=awe50meAI) |     Find the Git Command You Need Now!  |
|[bloop.](https://bloop.ai/?ref=awe50meAI) |     bloop is a code-search engine that uses GPT-4 to answer questions about your code. Search both your local and remote repositories with natural language, regex and filtered queries.  |
|[codium](https://www.codium.ai/?ref=awe50meAI) |     Generating meaningful tests for busy devs  |
|[drenaline](https://useadrenaline.com/app?ref=awe50meAI) |     An AI-powered debugger   [GitHub repository](https://github.com/shobrook/adrenaline/)  | 
|[AI CODE](https://aicode-weld.vercel.app/?ref=awe50meAI) |     Turn text into HTML&CSS with AI  |
|[Stunning.so](https://stunning.so/?ref=awe50meAI) |     Build websites with AI.i  |
|[codeium](https://codeium.com/?ref=awe50meAI) |     AI-Powered Autocomplete  |
|[Ghostwriter](https://replit.com/site/ghostwriter/?ref=awe50meAI) |     Meet Ghostwriter, your partner in code.  |
|[Lightning AI](https://lightning.ai/?ref=awe50meAI) |     The platform for teams to build AI, without the headaches  |
|[CommitAI](https://github.com/fengyiqicoder/CommitAi-Free?ref=awe50meAI) |     Let AI Handle Your Commit Messages  |
|[Codewand](https://www.codewand.co/?ref=awe50meAI) |     Use GPT-4 to build software with natural language.  |
|[kopylot](https://github.com/avsthiago/kopylot?ref=awe50meAI) |     An AI-Powered assistant for Kubernetes developers  |
|[Rix](https://hashnode.com/rix/?ref=awe50meAI) |     The Ultimate AI-Powered Chatbot for Developers  |
|[Kodezi](https://kodezi.com/?ref=awe50meAI) |   Kodezi is a AI developer tool platform that auto-corrects your code in real-time. We’re on a mission to 10x productivity in programming!  |
|[Google Gemini](https://gemini.google.com/?ref=awe50meAI) | Gemini gives you direct access to Google AI. Get help with writing, planning, learning, and more.  |
|[Safurai](https://www.safurai.com/?ref=awe50meAI) |     Safurai is the AI Code Assistant that saves you time in changing, optimizing, and searching code.  |
|[10Web](https://10web.io/?ref=awe50meAI) |    AI-Powered WordPress Platform  |
|[codium](https://www.codium.ai/?ref=awe50meAI) |  Generating meaningful tests for busy devs  |
|[blackbox AI](https://www.useblackbox.io/?ref=awe50meAI) |  {Code} As Fast As You Think.  |
|[ZZZ Code AI](https://zzzcode.ai/?ref=awe50meAI) |  Website to ask any programming question or get a code generated by AI |
|[screenshot-to-code](https://github.com/abi/screenshot-to-code?ref=awe50meAI) |  Drop in a screenshot and convert it to clean HTML/Tailwind/JS code |

## color tools
| Awesome | Description |
| --- | --- |
|[colormind](http://colormind.io/?ref=awe50meAI) |     Colormind - the AI powered color palette generator  |
|[Huemint](https://huemint.com/?ref=awe50meAI) |     AI color palette generator  |
|[khroma](https://www.khroma.co/?ref=awe50meAI) |     Khroma - The AI color tool for designers  |
|[ColorGPT](https://colorgpt.vercel.app/?ref=awe50meAI) |     Generating color name captured from real-world using AI  |
|[Chroma AI](https://chroma.szhao.dev/?ref=awe50meAI) |     Generate gradients based on your mood  |
|[PatternedAI](https://www.patterned.ai/?ref=awe50meAI) |     Generate unique patterns for your product using AI!  |

## miscellaneous
| Awesome | Description |
| --- | --- |
|[Browse AI](https://www.browse.ai/?ref=awe50meAI) |     The easiest way to extract and monitor data from any website.  |
|[interview-warmup by google](https://grow.google/certificates/interview-warmup/?ref=awe50meAI) |  |
|[fastoutreach](https://www.fastoutreach.ai/?ref=awe50meAI) |     The smartest AI personalization tool for entrepreneurs.  |
|[getleon](https://getleon.ai/?ref=awe50meAI) |     Leon is your open-source personal assistant who can live on your server.  |
|[Open AI Whisper](https://github.com/openai/whisper/?ref=awe50meAI) |     Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification.  |
|[lightning echo](https://lightning.ai/echo/view/home/?ref=awe50meAI) |     Transcription. simple and open-source.  [more lightning apps](https://lightning.ai/apps/?ref=awe50meAI) |  
|[unschooler](https://unschooler.me/?ref=awe50meAI) |     Personal AI-mentor helps you to find and pursue a new career.  |
|[namelix](https://namelix.com/?ref=awe50meAI) |     generate a short, brandable business name using artificial intelligence  |
|[lens ai](https://lens-ai.com/?ref=awe50meAI) |     AI-powered contextual computer vision ad solution  |
|[ai21](https://www.ai21.com/?ref=awe50meAI) |     When Machines Become Thought Partners  |
|[co:here ai](https://cohere.ai/?ref=awe50meAI) |     Making NLP part of every developer's toolkit  |
|[open ai](https://openai.com/api/?ref=awe50meAI) |     Build next-gen apps with OpenAI’s powerful models.  |
|[zyro ai tools](https://zyro.com/tools/?ref=awe50meAI) |     Free AI tools to set your business up for success  |
|[personal ai](https://www.personal.ai/?ref=awe50meAI) |     Generate new ideas, recall key concepts, and write original content and at the speed of thought.  |
|[monterey ai](https://www.monterey.ai/?ref=awe50meAI) |     Copilot for Product Development  |
|[kalendar ai](https://www.kalendar.ai/?ref=awe50meAI) |     Book new revenue on autopilot with AI  |
|[akkio](https://www.akkio.com/?ref=awe50meAI) |     Modern Business Runs on AI  |
|[cortex](https://www.meetcortex.com/?ref=awe50meAI) |     Enhance Your Creative with Powerful AI  |
|[validatorAI](https://www.validatorai.com/?ref=awe50meAI) |     Validate and receive constructive feedback on any startup idea, powered by AI!  |
|[naming magic](https://www.namingmagic.com/?ref=awe50meAI) |     Use AI to name your company and find a domain.  |
|[poised](https://www.poised.com/?ref=awe50meAI) |     Poised is the AI-powered communication coach that helps you speak with confidence and clarity.  |
|[mem](https://get.mem.ai/?ref=awe50meAI) |     Mem is the world's first AI-powered workspace that's personalized to you. Amplify your creativity, automate the mundane, and stay organized automatically.  |
|[tome](https://beta.tome.app/?ref=awe50meAI) |     Unlock your best work with Tome's AI-powered storytelling format.  |
|[custom GPT](https://customgpt.ai/?ref=awe50meAI) |     Build Your Own ChatBOT With Your Data  |
|[rationale](https://rationale.jina.ai/?ref=awe50meAI) |     a revolutionary AI to assist business owners, managers, and individuals in making tough decisions.  |
|[roomGPT.io](https://www.roomgpt.io/?ref=awe50meAI) |     Generating dream rooms using AI for everyone.  |
|[addcontext](https://addcontext.xyz/?ref=awe50meAI) |     Context is your AI-powered assistant for learning from your favorite websites, e-books, podcasts, videos, and more.  |
|[context](https://usecontext.io/?ref=awe50meAI) |     A brain for your business.  |
|[tl;dv](https://tldv.io/?ref=awe50meAI) |     AI-Powered Meeting Recorder for Zoom and Google Meet - tl;dv  |
|[ttree](https://ttree.ai/?ref=awe50meAI) | A fulfilling job is one step closer to a more inspiring and purposeful life. At ttree, we build AI-powered technology to match talent with the best opportunities out there.  |
|[bardeen](https://www.bardeen.ai/?ref=awe50meAI) |     Automate your manual tasks  |
|[HUMATA](https://www.humata.ai/?ref=awe50meAI) |     Ask AI anything about your files  |
|[Onesta](https://www.onestafinance.com/?ref=awe50meAI) |     Take control of your Financial Future  |
|[Where To AI!](https://www.wheretoai.com/?ref=awe50meAI) |     Welcome to Where To AI! Through the power of AI you will discover new destinations, create unforgettable memories and find the best places to stay.  |
|[castmagic](https://www.castmagic.io/?ref=awe50meAI) |     Podcast show notes & content in a click  |
|[AI Gift For You](https://aigiftforyou.com/?ref=awe50meAI) |     AI Gift For You - Finding the perfect gift just got easier!  |
|[TimeGPT](https://timegpt.vercel.app/?ref=awe50meAI) |     An AI-powered date and time converter. Enter a prompt to get started.   [GitHub repository](https://github.com/Spiderpig86/TimeGPT) | 
|[PromptPal](https://www.promptpal.net/?ref=awe50meAI) |     The destination for the best prompts for marketers, writers, designers, and more to get the most out of ChatGPT  |
|[Harvey.](https://www.harvey.ai/?ref=awe50meAI) |     Harvey | Generative AI for Elite Law Firms  |
|[Engage AI](https://getengageai.com/?ref=awe50meAI) |  |
|[Suggest AI](https://suggestai.co/?ref=awe50meAI) |     Suggest AI is a machine learning powered personalization engine offering a product portfolio customized for online businesses  |
|[Reflect](https://reflect.app/?ref=awe50reAI) |  |
|[waitroom](https://waitroom.com/?ref=awe50meAI) |     The solution to better meetings  |
|[Domains GPT](https://oneword.domains/domains-gpt/?ref=awe50meAI) |     Generate brandable & memorable domain names using AI. Powered by OpenAI and Vercel Edge Functions.  |
|[Gamma](https://gamma.app/?ref=awe50meAI) |     A new medium for presenting ideas. Powered by AI.  |
|[kickresume](https://www.kickresume.com/en/ai-resume-writer/?ref=awe50meAI) |     Automate your CV creation with our AI resume builder.  |
|[stability.ai](https://stability.ai/?ref=awe50meAI) |     AI by the people for the people  |
|[EnhaceAI](https://www.enhanceai.dev/?ref=awe50meAI) |     Add AI Autocomplete to any website in 2 minutes  |
|[June](https://www.june.so/ai?ref=awe50meAI) |     A new way to do product analytics  |
|[Avoma](https://www.avoma.com/v3?ref=awe50meAI) |     AI Meeting assistance and collaboration, reimagined.  |
|[SpeakAide](https://speakaide.com/?ref=awe50meAI) |     Take your public speaking to the next level with SpeakAide's AI script writing and teleprompter tool.  |
|[PowerMode](https://powermodeai.com/?ref=awe50meAI) |     PowerMode is your AI co-founder that will help you ideate and pitch your startup.  |
|[Talk to Books](https://books.google.com/talktobooks/?ref=awe50meAI) |     Browse passages from books using experimental AI  |
|[SheetAI](https://www.sheetai.app/?ref=awe50meAI) |     AI inside Spreadsheets  |
|[Tripnotes](https://tripnotes.ai/app/?ref=awe50meAI) |     Intelligent Travel Planner  |
|[Travel Plan AI](https://www.travelplan-ai.com/?ref=awe50meAI) |     Let AI Craft Your Perfect Travel Itinerary  |
|[Decktopus AI](https://www.decktopus.com/?ref=awe50meAI) |     World's #1 AI-Powered Presentation Generator  |
|[Banter AI](https://www.banterai.app/?ref=awe50meAI) |     Call up your favorite celebrities Scary realistic AI  |
|[tweetmonk_](https://tweetmonk.com/?ref=awe50meAI) |     Maximize your Twitter reach with our intelligent editor - create and schedule engaging tweets and threads to boost your growth.  |
|[AgentGPT](https://agentgpt.reworkd.ai/?ref=awe50meAI) |     Assemble, configure, and deploy autonomous AI Agents in your browser.  |
|[Chatshape](https://www.chatshape.com/?ref=awe50meAI) | Build AI Chatbots from your content, remarkably fast |
|[numerous.ai](https://numerous.ai/?ref=awe50meAI) | Extract text, categorize, generate formulas, and use ChatGPT right inside your spreadsheet |
|[glass.ai](https://www.glass.ai/?ref=awe50meAI)| Transforming sector and company research with AI |
|[ROCKSET](https://rockset.com/?ref=awe50meAI)| Build blazing fast search and AI applications in record time |
