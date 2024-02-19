# A Survey of Tools for Educational AI

This survey presents a comprehensive analysis of tools for educational AI, focusing on Large Language Models (LLMs), Prompt Engineering, Bots and "Bot Gardens", Vector Databases, LangChain and LangFlow, No Code Chatbot Creation, Fine-Tuning Custom LLMs, Cloud Agnosticism and Performance, and Interface Agnosticism and Performance. These technologies represent the forefront of integrating artificial intelligence into educational settings, offering unprecedented opportunities for personalized learning, interactive engagement, and scalable educational solutions.

For each category, we explore evaluation criteria such as performance metrics, ease of use, scalability, adaptability to educational content, ethical considerations, cost-effectiveness, support and community engagement, and innovation potential. These criteria provide a structured framework to assess the capabilities, user experience, and overall impact of AI tools in education.

The AI for Education Project (AI4ED) at Northeastern University exemplifies the practical application and potential of these tools. By developing open-source platforms and fostering collaborative ecosystems, AI4ED aims to democratize AI tools for educators worldwide, enhancing personalized learning experiences and addressing key educational challenges. This survey underscores the transformative power of AI in education, highlighting the need for continued innovation, ethical practices, and collaborative development to shape future learning environments.

## Invitation to Contribute

The AI for Education Project (AI4ED) warmly invites educators to contribute to work in educational AI by sharing your valuable insights, experiences, and resources. If you've encountered or utilized software tools that have transformed your teaching and learning environments, or if you have thoughts on emerging technologies in education, we'd love to hear from you. Please consider sending links and your reflections to ai@skunks.ai or uploading directly to our collaborative platform at [https://github.com/nikbearbrown/AI4ED/tree/main/A_Survey_of_Tools_for_Educational_AI](https://github.com/nikbearbrown/AI4ED/tree/main/A_Survey_of_Tools_for_Educational_AI). Your contributions are vital in shaping an inclusive, innovative, and effective educational future. Together, let's build a comprehensive resource that empowers educators around the globe to harness the potential of AI in transforming educational practices.

## LLMs

Large Language Models (LLMs) like the GPT series (OpenAI), LLaMA (Facebook AI), Gemini (Google), and others enable interaction with computers using natural language, moving beyond traditional programming languages such as C++, SQL, or Python.

### Evaluation Criteria for LLMs:

- **Performance Metrics**
  - **Accuracy**: The model's precision in understanding and generating responses, especially for complex educational content.
  - **Response Time**: The speed at which the model produces responses, critical for keeping users engaged.
  - **Language Understanding and Generation**: The ability to process multiple languages and produce coherent, context-appropriate responses.

- **Scalability and Accessibility**
  - **Ease of Integration**: Simplicity of incorporating the model into existing educational platforms and systems.
  - **Customization**: The model's flexibility to adapt to specific educational needs or curricula.
  - **User Interface (UI) and User Experience (UX)**: Usability and accessibility for educators and learners, including those with disabilities.

- **Content and Domain Adaptability**
  - **Subject Matter Coverage**: The breadth and depth of support for various subject areas, from STEM to humanities.
  - **Adaptability to Learning Levels**: The model's ability to modify content complexity based on the learner's proficiency.
  - **Interactive Learning Support**: Support for interactive learning experiences like quizzes, problem-solving, and simulations.

- **Ethical and Safety Considerations**
  - **Bias and Fairness**: Assessing the model's inherent biases and efforts to ensure fairness across diverse user groups.
  - **Privacy and Data Security**: Adherence to data protection laws and policies, particularly regarding student data.
  - **Content Filtering**: Filtering mechanisms to remove inappropriate content and safeguard educational interactions.

- **Cost Effectiveness**
  - **Licensing and Subscription Models**: Cost structures for educational institutions, including free tiers or educational discounts.
  - **Resource Requirements**: The computational and infrastructure needs for deploying and maintaining the model, impacting the total cost.

- **Support and Community**
  - **Documentation and Tutorials**: The availability and quality of resources for educators to integrate and utilize the model effectively.
  - **Community and Developer Support**: The presence of a supportive community and developer assistance for customization and troubleshooting.

- **Innovation and Future Potential**
  - **Continual Learning and Updates**: The model's ability to learn from interactions and improve over time.
  - **Research and Development Focus**: Ongoing research and future model enhancements, especially for educational applications.

## Prompt Engineering

Prompt engineering is both an art and a science of crafting language inputs (prompts) that elicit the best, most accurate, or most useful responses from Large Language Models (LLMs).

### Evaluation Criteria for Prompt Engineering Tools:

- **Ease of Use and Accessibility**
  - **User Interface (UI)**: The intuitiveness and simplicity of the user interface, enabling educators and students to craft prompts without extensive training.
  - **Documentation and Learning Resources**: Availability and quality of tutorials, guides, and examples that help users understand how to effectively use the tool for Prompt Engineering.

- **Flexibility and Customization**
  - **Prompt Templates and Examples**: The variety and relevance of built-in prompt templates or examples that can be customized for different educational needs and subjects.
  - **Adaptability to Various LLMs**: The tool's ability to work with multiple Large Language Models, allowing users to choose the best model for their specific educational context.

- **Efficiency and Effectiveness**
  - **Prompt Optimization Features**: Features that help users refine prompts to elicit more accurate or informative responses from LLMs, including suggestions for prompt improvement.
  - **Feedback and Iteration Capabilities**: The ability to test prompts, receive feedback on their effectiveness, and iterate on prompt design within the tool.

- **Integration and Compatibility**
  - **Compatibility with Educational Platforms**: The ease with which the tool can be integrated into existing educational software and learning management systems (LMS).
  - **API Access and Custom Integration Support**: Availability of API access for custom integrations, allowing for more advanced uses and automations in educational contexts.

- **Analytical and Support Tools**
  - **Response Analysis**: Tools that help analyze the LLM's responses for relevance, accuracy, and bias, supporting the refinement of prompts.
  - **Collaboration Features**: Support for collaborative prompt development, enabling teams of educators to work together on prompt engineering.

- **Ethical and Bias Considerations**
  - **Bias Detection and Mitigation Tools**: Features that help identify and mitigate potential biases in prompts and responses, ensuring fairness and inclusivity in educational content.
  - **Privacy and Security**: Measures to protect the privacy of users and the security of data within the prompt engineering process.

- **Scalability and Performance**
  - **Handling of Large-scale Deployments**: The tool's capability to support large numbers of users and high volumes of prompt interactions without significant degradation in performance.
  - **Resource Efficiency**: Optimization for computational and financial resources, especially important for educational institutions with limited budgets.

- **Support and Community**
  - **Technical Support and Customer Service**: The availability and quality of support for users encountering issues or needing assistance with the tool.
  - **Community Engagement**: The presence of an active user community for sharing best practices, prompt examples, and innovative uses of prompt engineering in education.

## Bots and "Bot Gardens"

In the landscape of digital education, the advent of bots—autonomous or semi-autonomous programs designed to execute specific tasks—has opened new horizons for personalized learning experiences. These digital agents, or "bots," are engineered to perform a wide array of functions, from generating quizzes to providing constructive feedback on student submissions. The concept of "Bot Gardens" represents a curated ensemble of these task-oriented bots, which are either explicitly designed for educational purposes or can be tailored to fit such contexts. This framework empowers educators to seamlessly integrate a variety of bots into bespoke educational ecosystems, effectively creating custom-tailored mentorship experiences for learners. For example, a versatile quiz bot can be reconfigured into a specialized tutor focused on a particular discipline, such as mathematics or visual arts, under the guidance of educational professionals.

Furthermore, the integration of AI Task Routing mechanisms, commonly referred to as "router bots" or "orchestration layers," enhances the functionality of bot gardens by managing the distribution of tasks among the available bots. These router bots assess the nature of each inquiry or task, leveraging context or content cues to assign it to the most appropriate task-specific bot. This process includes soliciting additional information from users whenever the initial request lacks clarity, ensuring that each student's question is addressed by the most capable digital agent. This dynamic interplay between various types of bots—including task bots, orchestration bots, and others—establishes a robust infrastructure for adaptive and responsive educational tools. By harnessing the collective capabilities of these digital agents, educational technologists and faculty can craft highly engaging and interactive learning environments tailored to the diverse needs of students.

### Evaluation Criteria for Bots and "Bot Gardens":

- **Functionality and Task Specialization**
  - **Range of Capabilities**: Assess the variety and scope of tasks that bots within the garden can perform, from generating quizzes to providing feedback.
  - **Specialization and Customization**: Evaluate the ease with which bots can be specialized or customized for different educational subjects or pedagogical approaches.

- **Integration and Orchestration**
  - **Ease of Integration**: Consider how seamlessly bots can be integrated into existing educational platforms or ecosystems.
  - **Orchestration Efficiency**: Evaluate the effectiveness of AI Task Routing mechanisms in distributing tasks among bots based on the context or content of requests.

- **User Interface and Experience**
  - **Accessibility for Educators and Learners**: Assess the user-friendliness of the bot interfaces for both educators and learners, including those with disabilities.
  - **Interactivity and Engagement**: Evaluate how interactive and engaging the bots are, and their ability to maintain student interest and facilitate active learning.

- **Adaptability and Learning Support**
  - **Personalization Capabilities**: Examine the extent to which bots can adapt to individual learner profiles, preferences, and progress.
  - **Support for Diverse Learning Styles**: Consider how well the bot garden supports various learning styles and pedagogical strategies, including flipped classrooms, project-based learning, etc.

- **Scalability and Performance**
  - **Scalability**: Evaluate the bot garden's capacity to scale up to accommodate a large number of users or to expand its range of functionalities.
  - **Performance Metrics**: Consider the responsiveness and reliability of the bots, including load times and accuracy of task execution.

- **Ethical and Privacy Considerations**
  - **Data Privacy and Security**: Assess the measures in place to protect user data, especially sensitive student information.
  - **Bias and Fairness**: Evaluate the efforts to address and mitigate biases within the bots, ensuring equitable and fair educational experiences for all students.

- **Cost-Effectiveness and Resource Efficiency**
  - **Cost Structure**: Consider the cost associated with deploying and maintaining the bot garden, including subscription fees and any required infrastructure investments.
  - **Resource Efficiency**: Evaluate the efficiency of bots in terms of computational resources required, ensuring they are accessible to institutions with limited IT resources.

- **Support and Community**
  - **Developer and Community Support**: Examine the availability and quality of support for educators and developers, including documentation, forums, and customer service.
  - **Continuous Improvement and Updates**: Consider how actively the bot garden is maintained and updated, including the addition of new features and the resolution of issues.

## Vector Databases - External Data for LLMs

Vector databases are specialized systems designed to store, manage, and index high-dimensional unstructured data efficiently. The primary function of vector databases is to enable fast and efficient similarity searches. Vector databases are crucial for LLMs and generative AI applications. They can serve as an external knowledge base, helping to ensure that generative AI models like ChatGPT provide trustworthy information by retrieving relevant data points based on the similarity of vector embeddings.

### Evaluation Criteria for Vector Databases:

- **Efficiency and Performance**
  - **Search Speed**: Evaluate the speed at which the database can perform similarity searches, as this impacts the responsiveness of LLMs in real-time interactions.
  - **Scalability**: Assess the database's ability to handle increasing amounts of data and concurrent requests without significant performance degradation.

- **Accuracy and Relevance**
  - **Precision of Search Results**: Determine the accuracy of the database in returning highly relevant results for similarity queries, which is critical for the trustworthiness of LLM responses.
  - **Update and Refresh Capabilities**: Evaluate how effectively the database incorporates new data and updates existing vectors to maintain the relevance of search results over time.

- **Data Privacy and Security**
  - **Encryption and Data Protection**: Assess the measures in place for securing stored data, especially when handling sensitive or personal information.
  - **Compliance with Data Regulations**: Evaluate the database's adherence to international data privacy standards and regulations.

- **Integration and Compatibility**
  - **Ease of Integration**: Consider how easily the vector database can be integrated with LLMs and generative AI applications, including compatibility with various AI models and frameworks.
  - **APIs and Tooling**: Evaluate the availability and quality of APIs and developer tools for interacting with the database, facilitating custom integrations and extensions.

- **Management and Maintenance**
  - **Administrative Tools**: Assess the tools available for managing and monitoring the database, including user interfaces for data ingestion, indexing, and query analysis.
  - **Support and Documentation**: Consider the level of technical support and the quality of documentation provided to help users manage and troubleshoot the database.

- **Cost Efficiency**
  - **Pricing Model**: Evaluate the cost implications of using the database, including subscription fees, data storage costs, and query processing charges.
  - **Resource Optimization**: Consider the database's efficiency in using computational and storage resources, affecting the overall cost of operation.

- **Innovation and Future Proofing**
  - **Adaptability to New Technologies**: Assess the database's capacity to integrate with emerging technologies and AI advancements, ensuring it remains effective as LLMs evolve.
  - **Research and Development Focus**: Evaluate the ongoing investment in research and development to improve the database's features, performance, and security measures.




