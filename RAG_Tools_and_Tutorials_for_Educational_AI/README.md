# RAG Tools and Tutorials Educational AI

Retrieval-Augmented Generation (RAG) is a methodology used in building advanced language models, particularly for applications like chatbots, that combines the best of both retrieval-based and generative AI technologies. The basic idea behind RAG is to enhance the response generation capability of a chatbot by dynamically retrieving relevant information from a large database or corpus of text and then generating a response based on both the retrieved information and the generative model's knowledge.

# Table of Contents
1. [RAG Tools and Tutorials Educational AI](#rag-tools-and-tutorials-educational-ai)
   - [How RAG Works](#how-rag-works)
   - [Benefits of RAG for LLM-Based Chatbots](#benefits-of-rag-for-llm-based-chatbots)
   - [Use Cases](#use-cases)
2. [Cloud Services for RAG](#cloud-services-for-rag)
3. [Useful Cloud Services for Building RAG Educational AI Applications](#useful-cloud-services-for-building-rag-educational-ai-applications)
4. [No Code Chatbot Tools](#no-code-chatbot-tools)
5. [UIs for RAG Apps](#uis-for-rag-apps)
   - [Existing Commonly Used Apps for Students](#existing-commonly-used-apps-for-students)
   - [Commonly Used LMS](#commonly-used-lms)
6. [Other Useful Tools](#other-useful-tools)
7. [DeepLearning.ai Generative AI Short Courses]

   
### How RAG Works

1. **Retrieval Phase**: When a user inputs a query or question, the RAG system first searches a database or document collection to find relevant pieces of information. This retrieval is typically powered by vector search technologies, where documents and queries are converted into vectors (mathematical representations), and the system looks for the closest matches.

2. **Augmentation Phase**: The retrieved documents or text snippets are then fed into a generative model along with the original query. This process enriches the context the model has to work with, providing it with specific information that may not be contained within its pre-trained knowledge base.

3. **Generation Phase**: The generative model, usually a large language model (LLM) like GPT (Generative Pre-trained Transformer), uses this augmented context to generate a response that is informed by both its pre-trained knowledge and the specific details retrieved in the first step.

### Benefits of RAG for LLM-Based Chatbots

- **Increased Accuracy and Relevance**: By pulling in specific information relevant to the user's query, RAG systems can provide more accurate and contextually relevant responses than a purely generative model might be able to, particularly for questions about niche or specialized topics.

- **Up-to-date Information**: Because RAG-based chatbots pull information from a constantly updated database or corpus, they can provide more current responses than a model that only relies on the knowledge it was trained on.

- **Reduced Hallucination**: Generative models are known to sometimes "hallucinate" responses, meaning they generate plausible but factually incorrect information. The retrieval step in RAG helps mitigate this by anchoring the response in real, retrieved documents.

- **Customizability and Extensibility**: The database or corpus used for retrieval can be customized and expanded based on the specific needs of the application, allowing for specialized chatbots that can answer questions in specific domains, such as legal, medical, or technical fields.

### Use Cases

RAG applications are particularly useful in scenarios where accuracy, depth of knowledge, and the ability to provide up-to-date information are critical. Examples include customer support chatbots, educational tutors, research assistants, and more. In these applications, the ability of the chatbot to pull in the latest information or delve deeply into a specialized knowledge domain can significantly enhance the user experience.

In summary, RAG represents a powerful approach to building LLM-based chatbots, offering a blend of the depth and breadth of knowledge of generative models with the specificity and accuracy provided by retrieval-based systems. This methodology enables the creation of chatbots that are not only more helpful and informative but also more reliable and trustworthy.

## Cloud Services for RAG

When building RAG (Retrieval-Augmented Generation) applications, cloud services like Pinecone, OpenAI, Anyscale, AWS Lambda, and Azure AI offer a range of functionalities that can be leveraged for efficient development and deployment. 

Cloud services play a vital role in the development and deployment of RAG (Retrieval-Augmented Generation) applications, offering a plethora of functionalities. These services include vector database capabilities, powerful language models for text generation, serverless computing environments, and AI-enriched search mechanisms.

For the storage and retrieval aspects of RAG applications, Pinecone stands out with its vector database capabilities. Canopy, which utilizes Pinecone, offers a RAG framework that streamlines text data processing.

OpenAI provides APIs for the generative component of RAG applications, offering advanced language models like GPT.

Anyscale, along with Ray, delivers a compute layer that enhances the retrieval capabilities of RAG applications, promoting a serverless development environment.

AWS Lambda enables serverless application deployment, seamlessly integrating with OpenAI's technologies for building QA chatbots.

Azure AI Search delivers vector support and AI enrichment tools, essential for content retrieval and processing within RAG applications.

Google Cloud and Google Vertex AI join this suite with robust data ingest and machine learning services, allowing for scalable and efficient embeddings computation.

## Useful Cloud Services for builing RAG Educational AI applications.

- **Pinecone**: A vector database service designed for machine learning applications, offering high-performance similarity search for embedding vectors, making it ideal for RAG applications. [https://www.pinecone.io/](https://www.pinecone.io/)

- **OpenAI API**: Provides access to powerful AI models, including the GPT series, enabling developers to incorporate advanced natural language processing and generation into their applications. [https://openai.com/api/](https://openai.com/api/)

- **Anyscale**: Offers a platform that simplifies the process of deploying and scaling Ray applications, making distributed computing easier and more accessible. [https://www.anyscale.com/](https://www.anyscale.com/)

- **AWS Lambda**: A serverless computing service that runs code in response to events and automatically manages the computing resources required, perfect for on-demand processing within RAG applications. [https://aws.amazon.com/lambda/](https://aws.amazon.com/lambda/)

Sure, AWS offers several tools and services that are particularly useful for building websites and mobile applications, complementing their offerings for RAG applications. Here's a description of some of these services:

- **Amazon EC2 (Elastic Compute Cloud)**: Provides resizable compute capacity in the cloud, allowing developers to launch virtual servers as instances, with a variety of configurations to suit different workloads. [Amazon EC2](https://aws.amazon.com/ec2/)

- **Amazon S3 (Simple Storage Service)**: An object storage service that offers industry-leading scalability, data availability, security, and performance. It's often used for storing and serving static website content. [Amazon S3](https://aws.amazon.com/s3/)

- **AWS Amplify**: A set of tools and services for building full-stack mobile and web applications, including features like authentication, data storage, backend integration, and more. [AWS Amplify](https://aws.amazon.com/amplify/)

- **Amazon RDS (Relational Database Service)**: Simplifies setting up, operating, and scaling a relational database in the cloud, providing cost-efficient and resizable capacity while managing time-consuming database administration tasks. [Amazon RDS](https://aws.amazon.com/rds/)

- **AWS Elastic Beanstalk**: An easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS. [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)

- **AWS AppSync**: A managed service that uses GraphQL to make it easy for applications to get exactly the data they need, allowing for the building of scalable applications, including real-time updates, offline data sync, and data manipulation across multiple data sources. [AWS AppSync](https://aws.amazon.com/appsync/)

These AWS tools and services offer robust solutions for developers to build, deploy, manage, and scale their websites and mobile applications efficiently in the cloud.

- **Azure AI Search**: Integrates AI capabilities with Azure's search service to provide enriched content retrieval, which includes both semantic search and traditional keyword search. [https://azure.microsoft.com/en-us/services/search/](https://azure.microsoft.com/en-us/services/search/)

- **Google Cloud**: Offers a wide range of cloud services including computing, storage, and machine learning, which can be leveraged for building and hosting RAG applications. [https://cloud.google.com/](https://cloud.google.com/)

- **Google Vertex AI**: A managed machine learning platform that allows developers to build, deploy, and scale ML models faster, with pre-trained and custom tooling within Google Cloud. [https://cloud.google.com/vertex-ai](https://cloud.google.com/vertex-ai)

Each of these services provides specific functionalities that support various aspects of building and operating RAG applications, from data storage and management to machine learning model training and deployment.

These cloud services empower developers to build, scale, and maintain RAG applications effectively, catering to various needs from initial data processing to the final stages of content retrieval and response generation.

These cloud services and frameworks offer a rich set of features that can support the development of RAG applications across various stages, from data processing and embeddings computation to content retrieval and text generation.

## No Code Chatbot Tools

No-code tools like Flowise, Dify, and Langflow offer intuitive visual programming interfaces for building Retrieval-Augmented Generation (RAG) applications. These low-code/no-code platforms are equipped with drag & drop capabilities, streamlining the development of customized Large Language Model (LLM) applications.

Key features of these platforms include:

- **Ease of Use**: Designed to be user-friendly, enabling individuals without deep programming expertise to visualize and construct LLM applications.
- **Integration Support**: They support a variety of integrations through APIs and SDKs, along with an embedded chat widget for enhanced functionality.
- **Open-Source and Platform-Agnostic**: These tools are typically open-source and can operate across different environments, including air-gapped setups with local resources.
- **Cloud Compatibility**: The flexibility to self-host on various cloud platforms like AWS, Azure, and GCP, provides scalability and access to robust cloud services.
- **Community-Driven**: A growing community of developers values these platforms for the rapid development and deployment of LLM applications, catering to diverse needs such as academic resources and student support services.

Overall, Flowise, Dify, and Langflow represent a shift towards more accessible AI application development, democratizing the use of advanced LLMs across industries and use cases.

![No Code Chatbot Tools](https://raw.githubusercontent.com/nikbearbrown/AI4ED/b3e4e14c0bcc5d81e478cf9acaffcaa40b63ebc3/AI4ED_Art/Flowise.png)


- **Flowise**: A drag & drop UI platform for building customized LLM flows, facilitating easy LLM app development. [Flowise on GitHub](https://github.com/FlowiseAI/Flowise)
  
- **Dify**: An open-source alternative to Assistants API and GPTs, Dify.AI serves as an LLM application development platform integrating Backend as a Service and LLMOps, including a built-in RAG engine. [Dify on GitHub](https://github.com/langgenius/dify)

- **Langflow**: Langflow is a dynamic graph where each node is an executable unit. Its modular and interactive design fosters rapid experimentation and prototyping, pushing hard on the limits of creativity. [Langflow on GitHub](https://github.com/logspace-ai/langflow)


## UI's for RAG apps

Retrieval-Augmented Generation (RAG) integration into these platforms typically involves using the respective platform's API to send and receive messages. The RAG app processes the content of these messages to retrieve relevant information and generate responses that are then sent back to the chat interface. This integration enables seamless AI interaction within the existing communication ecosystem of a team or community.

Retrieval-Augmented Generation (RAG) applications can be integrated with platforms like Slack, Discord, and Microsoft Teams to enhance productivity, collaboration, and engagement by leveraging AI capabilities. Here's how RAG apps could use each platform as an interface:

**Existing Commonly Used Apps for Students**

### Slack
- **Team Productivity**: RAG apps could act as virtual assistants in Slack channels, providing quick, contextually relevant information retrieved from company documents or the web to answer queries.
- **Workflow Automation**: They could automate workflows by retrieving necessary information and generating responses for approval processes, scheduling, and task management.
- **Onboarding and Training**: RAG apps can facilitate onboarding by answering new hires' questions, offering a self-service knowledge base.
- **Slack API** 
[https://api.slack.com/](https://api.slack.com/)
- 

### Discord
- **AI-Driven Moderation**: RAG apps can help moderate discussions by retrieving community guidelines or precedents to address queries about conduct or to assist in decision-making for moderators.
- **User Engagement**: They can generate content or game-related trivia, enhancing user engagement in community channels.
- **Support Channels**: RAG bots can provide instant support by retrieving FAQs or guides, reducing the load on human support staff.
- **Discord API** 
  [https://discord.com/developers/docs/intro](https://discord.com/developers/docs/intro)

### Microsoft Teams
- **Enterprise Collaboration**: In Teams, RAG apps can enhance collaboration by fetching project-specific data or documentation to assist teams in their discussions.
- **Meeting Summaries**: Post-meeting, a RAG app could generate concise summaries by retrieving key points from a recorded meeting transcript.
- **Learning and Development**: They can serve as on-demand trainers, retrieving educational content or answering questions to support continuous learning within Teams.
- **Microsoft Teams API** 
Microsoft Teams offers a developer platform with an API that enables the creation of custom integrations within Teams. This API can be utilized to develop custom commands and controls, such as toggling mute or camera functions, which can be compatible with Stream Deck or other similar devices.

To explore and develop such integrations, here are some useful resources:

1. **Microsoft Teams Developer Platform**: A comprehensive guide to all developer resources and documentation for Microsoft Teams. [Visit the Developer Platform](https://developer.microsoft.com/en-us/microsoft-teams/)

2. **Microsoft Teams API Reference**: Detailed API documentation for Microsoft Teams, providing information for using different endpoints. [Access the API Reference](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-beta)

3. **Microsoft Teams App Studio**: A tool within the Microsoft Teams developer platform that simplifies the process of creating and registering apps. [Learn about App Studio](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/build-and-test/app-studio-overview)

**Commonly Used LMS**

Retrieval-Augmented Generation (RAG) applications can be integrated into learning management systems (LMS) like Moodle and Canvas to enrich the educational experience. Here's how they could be used:

### Moodle
- **Student Support**: A RAG chatbot integrated into Moodle can provide students with instant answers to their questions about course materials, deadlines, and administrative processes by retrieving information from the Moodle database.
- **Content Summarization**: RAG apps can summarize forum discussions and course content, making it easier for students to catch up on missed work or review key concepts.
- **Assessment Assistance**: They can assist educators by generating quiz questions based on the course content or by providing students with practice questions and answers.
- **Moodle API** 
  [https://docs.moodle.org/dev/Main_Page](https://docs.moodle.org/dev/Main_Page)

### Canvas
- **Personalized Learning**: RAG apps can suggest additional resources and reading materials by understanding the context of a student’s query and retrieving relevant information from within the Canvas ecosystem or external sources.
- **Grading Support**: For educators, RAG applications can help grade short-answer questions by retrieving information from a knowledge base to evaluate student responses.
- **Announcements and Updates**: RAG bots can automatically generate announcements about upcoming assignments or changes to the syllabus, based on the course schedule and curriculum.
- **Canvas API** 
  [https://canvas.instructure.com/doc/api/](https://canvas.instructure.com/doc/api/)

Integration with Moodle and Canvas would typically use their respective APIs to interact with the system's data and user interface. The RAG application would process requests from users within the LMS, retrieve the necessary information or generate content as required, and provide that information back to the LMS for display to the user. This enhances the LMS's capability to deliver responsive and personalized educational experiences.

## Other Useful Tools

**Image Creation and Video Tools**

Sure, adding Midjourney and Bing Image Creator to the list:

- **DALL·E**: Created by OpenAI, DALL·E is an AI program capable of generating images from textual descriptions, offering a wide range of creative possibilities. [DALL·E](https://openai.com/dall-e/)

- **RunwayML**: Offers a creative studio in the cloud that enables creators to use advanced AI in their creative process, including image generation and manipulation. [RunwayML](https://runwayml.com/)

- **Midjourney**: An independent research lab exploring new mediums of thought and expanding the imaginative powers of the human species. Midjourney focuses on creating images through textual prompts, offering detailed and artistic renditions. [Midjourney](https://www.midjourney.com/)

- **Bing Image Creator**: Powered by Microsoft, this tool integrates with the Bing search engine to generate images based on text descriptions, providing users with creative and diverse visual content. [Bing Image Creator](https://www.bing.com/)

These AI image creation tools demonstrate the breadth of possibilities in generating art, realistic images, and visual content through advanced machine learning and artificial intelligence technologies.

Here's the cleaned and formatted list of courses:

### DeepLearning.ai Generative AI Short Courses

AI4ED highly recommends these courses for individuals interested in Retrieval Augmented Generation (RAG). DeepLearning.AI offers a series of short courses designed to elevate your generative AI expertise. These concise, impactful courses are crafted to provide you with the knowledge, tools, and concepts needed to advance your skills in a time-efficient manner. Currently, they are available at no cost for a limited period, making this an excellent opportunity for those keen on exploring RAG and other generative AI technologies.

#### Beginners

- **ChatGPT Prompt Engineering for Developers**
  - Instructors: Isa Fulford, Andrew Ng
  - Learn API access, LLM leverage, custom chatbot building, and prompt engineering best practices.
  - Prerequisite: Basic Python

- **Building Systems with the ChatGPT API**
  - Instructors: Isa Fulford, Andrew Ng
  - Level up in LLM usage, complex task breakdown, workflow automation, and multistage prompt chaining.
  - Prerequisite: Basic Python

- **LangChain for LLM Application Development**
  - Instructor: Harrison Chase
  - Use LangChain for new environments, with personal assistants and chatbots focus.
  - Prerequisite: Basic Python

- **LangChain: Chat with Your Data**
  - Instructor: Harrison Chase
  - Create a chatbot to interface with private data, utilizing LangChain loaders.
  - Prerequisite: Basic Python

- **Large Language Models with Semantic Search**
  - Instructors: Jay Alammar, Luis Serrano
  - Enhance search capabilities using LLMs and Cohere Rerank.
  - Prerequisite: Basic Python

- **Building Generative AI Applications with Gradio**
  - Instructor: Apolinário Passos
  - Develop and share ML applications, focusing on image generation and text summarization.
  - Prerequisite: Basic Python

- **LLMOps**
  - Instructor: Erwin Huizenga
  - Design and automate LLM tuning and deployment with a focus on question-answering applications.
  - Prerequisite: Basic Python

- **Build LLM Apps with LangChain.js**
  - Instructor: Jacob Lee
  - Explore LangChain.js for application building, emphasizing conversational retrieval chains.
  - Prerequisite: Intermediate JavaScript

- **Reinforcement Learning from Human Feedback**
  - Instructor: Nikita Namjoshi
  - Introduction to RLHF for LLM tuning and evaluation, using the Llama 2 model.
  - Prerequisite: Intermediate Python

- **Building and Evaluating Advanced RAG Applications**
  - Instructors: Jerry Liu, Anupam Datta
  - Focus on enhancing RAG techniques and mastering evaluation metrics for robust systems.
  - Prerequisite: Basic Python

- **Quality and Safety for LLM Applications**
  - Instructor: Bernease Herman
  - Evaluate safety and security of LLM applications against various risks.
  - Prerequisite: Basic Python

- **Vector Databases: from Embeddings to Applications**
  - Instructor: Sebastian Witalec
  - Design real-world applications using vector databases for efficient searches.
  - Prerequisite: Basic Python, knowledge of data structures useful

- **Pair Programming with a Large Language Model**
  - Instructor: Laurence Moroney
  - Utilize LLMs for code improvement, debugging, understanding, and documentation.
  - Prerequisite: Basic Python

- **Understanding and Applying Text Embeddings**
  - Instructors: Nikita Namjoshi, Andrew Ng
  - Accelerate development with text embeddings for clustering, classification, and QA systems.
  - Prerequisite: Basic Python

- **How Business Thinkers Can Start Building AI Plugins With Semantic Kernel**
  - Instructor: John Maeda
  - Use Microsoft's Semantic Kernel for business application development with LLMs.
  - Prerequisite: Basic Python

#### Intermediate

- **Serverless LLM apps with Amazon Bedrock**
  - Instructor: Mike Chambers
  - Deploy LLM-based applications using serverless technology and Amazon Bedrock.
  - Prerequisite: Familiarity with Python and AWS services

- **Finetuning Large Language Models**
  - Instructor: Sharon Zhou
  - Master LLM finetuning, differentiate from prompt engineering with hands-on experience.
  - Prerequisite: Basic Python

- **Evaluating and Debugging Generative AI Models Using Weights and Biases**
  - Instructor: Carey Phelps
  - Learn MLOps tools for AI model management, versioning, and debugging.
  - Prerequisite: Familiarity with Python, PyTorch or similar frameworks

- **How Diffusion Models Work**
  - Instructor: Sharon Zhou
  - Build and understand diffusion models, with a focus on algorithm implementation.
  - Prerequisite: Python, TensorFlow, or Pytorch

- **Automated Testing for LLMOps**
  - Instructor: Rob Zuber
  - Create an automated CI pipeline for LLM application evaluation.
  - Prerequisite: Basic Python, familiarity with LLM-based applications

- **Advanced Retrieval for AI with Chroma**
  - Instructor: Anton Troynikov
  - Improve retrieval relevancy with advanced techniques and LLM integration.
  - Prerequisite: Intermediate Python

- **Functions, Tools and Agents with LangChain**
  - Instructor: Harrison Chase
  - Explore

