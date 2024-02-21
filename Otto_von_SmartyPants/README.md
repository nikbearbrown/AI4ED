
# Requirements Document for Otto von SmartyPants and Automated Grading App

## The logic, the idea behind Otto von SmartyPants

The Automated Grading App is designed to streamline the process of grading student assignments by leveraging the capabilities of Large Language Models (LLMs). Here's a clear description of the app's logic and workflow:

### 1. **Uploading Assignments and Rubric**

- **Step 1.1: Upload Process**
  - Users (educators/institutions) start by uploading a zip file containing the students' assignments. This could include essays, reports, or any text-based work that needs grading.
  - Alongside the assignments, users upload a document that outlines the grading rubric. This rubric is provided in the form of prompt instructions, detailing the criteria against which the assignments will be evaluated.

### 2. **Model Selection**

- **Step 2.1: Choosing LLMs**
  - The app allows users to select from a variety of pre-integrated Large Language Models. Each model has its strengths, and users can choose one or multiple models based on the nature of the assignments or their preference for a particular model's evaluation style.

### 3. **Assignment Submission and Evaluation**

- **Step 3.1: Submission to LLMs**
  - Once the models are selected, the app submits the assignments to the chosen LLM(s). Each assignment can be submitted multiple times to each model to ensure consistency and reliability in grading.
  
- **Step 3.2: Evaluation by Models**
  - The selected LLMs evaluate the assignments based on the provided rubric. This evaluation process involves analyzing the content for its adherence to the criteria, such as argument strength, evidence, clarity, creativity, and technical accuracy.

### 4. **Aggregation and Analysis**

- **Step 4.1: Aggregating Results**
  - After all selected models have evaluated the assignments, the app aggregates the scores and feedback from each submission. This includes compiling scores from multiple submissions to the same model and across different models.
  
- **Step 4.2: Averaging Scores**
  - The app calculates an average score for each assignment by considering all the scores it received across all submissions and models. This step is crucial for balancing out any anomalies and ensuring a fair evaluation.

- **Step 4.3: Calculating Confidence Levels**
  - Along with average scores, the app calculates a confidence level in the grading. This is based on the consistency of scores across multiple submissions and models. A higher consistency results in a higher confidence level, indicating that the LLMs largely agree on the quality of the work.

### 5. **Feedback and Report Generation**

- **Step 5.1: Detailed Feedback**
  - The app generates detailed feedback for each assignment, including specific points of strength and areas for improvement as identified by the LLMs. This feedback is aligned with the rubric's criteria, providing actionable insights for students.
  
- **Step 5.2: Report Generation**
  - A comprehensive report is created for each student assignment, which includes the average score, confidence level, and detailed feedback. These reports can be accessed by the educators for review and then shared with students for their reference.

### 6. **Data Storage and Security**

- **Step 6.1: Secure Storage**
  - All uploaded documents, evaluation results, and generated reports are securely stored, ensuring the confidentiality and integrity of student work and grading outcomes.
  
- **Step 6.2: Compliance**
  - The app adheres to data protection regulations, safeguarding the privacy and security of the information it handles.

This logic ensures that the Automated Grading App not only automates the grading process but does so in a way that is thorough, fair, and transparent, enhancing the educational feedback loop between educators and students.

## 1. Introduction

This document outlines the functional and non-functional requirements for an automated grading application designed to streamline the process of evaluating student assignments. The application will accept a zip file containing student assignments and a rubric in the form of prompt instructions for grading. It will utilize various Large Language Models (LLMs) to grade assignments, allowing for submissions to be evaluated multiple times by each model and across multiple models. The system will then compile these evaluations, average the metrics and scores, and generate both an average score and a confidence level for each assignment.

## 2. Functional Requirements

### 2.1 User Interface

1. **Upload Interface:** Users can upload a zip file containing student assignments and a separate document or file containing the grading rubric in the form of prompt instructions.
2. **Model Selection:** Users can select one or more LLMs from a list of available models for evaluating the assignments.
3. **Submission Management:** Users can submit the assignments to be graded multiple times to each selected model.
4. **Results Interface:** Users can view and download detailed feedback, including scores, confidence levels, and combined reports for each student assignment.

### 2.2 Core Features

1. **Assignment Processing:** The app shall extract assignments from the uploaded zip file and process them according to the provided rubric.
2. **Model Integration:** The app shall integrate with various LLMs, allowing for flexible assignment grading based on user-selected models.
3. **Evaluation Repetition:** The app shall support submitting each assignment multiple times to each selected LLM to ensure grading consistency and reliability.
4. **Score Aggregation:** The app shall aggregate scores and metrics from all evaluations, calculating an average score and a confidence level for each assignment.
5. **Report Generation:** The app shall generate detailed reports for each assignment, including individual scores from each LLM, average scores, and confidence levels.

### 2.3 Data Management

1. **Data Storage:** The app shall securely store all uploaded documents, grading results, and generated reports.
2. **Data Privacy:** The app shall comply with data protection regulations, ensuring the confidentiality and integrity of student assignments and grading results.

## 3. Non-Functional Requirements

### 3.1 Performance

1. **Response Time:** The app shall process uploads and generate grading results within a reasonable time frame, not exceeding a specified limit for the total number of assignments.
2. **Scalability:** The app shall efficiently handle varying loads, from individual assignments to large batches of submissions.

### 3.2 Usability

1. **Ease of Use:** The app shall offer an intuitive user interface, minimizing the learning curve for new users.
2. **Accessibility:** The app shall comply with accessibility standards, ensuring it is usable by people with a wide range of abilities.

### 3.3 Security

1. **Data Security:** The app shall implement robust security measures to protect sensitive information, including student assignments and grading results.
2. **Compliance:** The app shall comply with relevant legal and regulatory requirements regarding data protection and privacy.

### 3.4 Reliability

1. **Uptime:** The app shall aim for high availability, with minimal downtime.
2. **Data Integrity:** The app shall ensure the integrity of grading results, with mechanisms in place to detect and correct any errors in the grading process.

## 4. System Requirements

### 4.1 Hardware Requirements

- The app shall be deployable on standard server hardware or cloud platforms, with scalable resources to meet demand.

### 4.2 Software Requirements

- **Backend:** Compatible with major server operating systems (e.g., Linux, Windows Server).
- **Frontend:** Accessible through modern web browsers without requiring any specific plugins.
- **APIs:** Integration with LLMs through their respective APIs, requiring internet connectivity.

## 5. Compliance and Standards

- The app shall adhere to GDPR (for European users) and other relevant data protection laws.
- The app shall follow best practices in software development and cybersecurity.

## 6. Quality Assurance

- **Testing:** The app shall undergo thorough testing, including unit tests, integration tests, and user acceptance testing.
- **Documentation:** Comprehensive user and technical documentation shall be provided.

## 7. Implementation Timeline

- A detailed project timeline, including phases for design, development, testing, and deployment, shall be prepared and followed.

## 8. Maintenance and Support

- The app shall include a plan for ongoing maintenance, updates, and user support.

This document sets the foundation for developing an automated grading application that leverages the capabilities of LLMs to provide efficient, reliable, and scalable assignment grading.
