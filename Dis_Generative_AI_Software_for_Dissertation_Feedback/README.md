# Generative AI Software for Dissertation Feedback: Requirements Document

## 1. Introduction

This document outlines the functional and non-functional requirements for a Generative AI-based software designed to provide detailed feedback on PhD dissertations. The software aims to assist students by analyzing their submitted dissertations and all referenced papers, offering constructive feedback on what was done well and suggestions for improvement across various sections.

### 1.1 Purpose

The purpose of this software is to provide PhD candidates with comprehensive, actionable feedback on their dissertations, focusing on enhancing the quality of their academic work before final submission.

### 1.2 Scope

The software will accept dissertation documents and their reference papers as input, analyze each section of the dissertation, request feedback from a chosen Language Model (LLM), and compile an overall feedback report detailing strengths and areas for improvement.

## 2. Overall Description

### 2.1 User Needs

- PhD students require detailed, section-wise feedback on their dissertations to understand their work's strengths and areas needing improvement.
- Supervisors and reviewers seek efficient tools to provide constructive feedback to students.

### 2.2 Assumptions and Dependencies

- Users have access to a compatible LLM for processing feedback requests.
- The software relies on the accuracy and capabilities of the chosen LLM for generating feedback.

## 3. System Features and Requirements

### 3.1 Functional Requirements

#### 3.1.1 Document Upload and Parsing

- **F1**: The system shall allow users to upload their dissertation and reference papers in a supported format (e.g., PDF, DOCX).
- **F2**: The system shall parse the uploaded dissertation into its constituent sections as per the standard structure (e.g., Abstract, Introduction, Literature Review, etc.).

#### 3.1.2 Feedback Generation

- **F3**: For each section, the system shall make specialized requests to the chosen LLM, sending the section's content and asking for feedback on "what was done well" and "suggestions for improvement."
- **F4**: The system shall compile the feedback from the LLM for each section into a comprehensive feedback report.

#### 3.1.3 User Interaction and Output

- **F5**: The system shall allow users to select their preferred LLM for processing the feedback requests.
- **F6**: The system shall present the feedback report to the user, organized by dissertation section, in a readable and accessible format.

### 3.2 Non-Functional Requirements

#### 3.2.1 Performance

- **N1**: The system shall process feedback requests and generate the report within a reasonable time frame, considering the length and complexity of the dissertation.

#### 3.2.2 Usability

- **N2**: The software shall offer an intuitive user interface, allowing users to easily upload documents, select an LLM, and view their feedback reports.

#### 3.2.3 Scalability

- **N3**: The system shall be capable of handling a large number of concurrent users and feedback requests without significant degradation in performance.

#### 3.2.4 Security

- **N4**: The system shall ensure the confidentiality and integrity of user-uploaded documents and feedback reports, employing secure data storage and transmission practices.

### 3.3 System Interface Requirements

- **I1**: The software shall provide an API or interface for interacting with various LLMs, allowing for flexible LLM selection and integration.

### 3.4 User Documentation and Training

- **D1**: Comprehensive user documentation shall be provided, detailing the process of uploading documents, selecting an LLM, and interpreting the feedback report.
- **D2**: Online training materials or tutorials shall be made available to guide users through the software's features and best practices.

## 4. Conclusion

This document has outlined the requirements for a Generative AI software designed to provide detailed feedback on PhD dissertations. By meeting these requirements, the software will serve as a valuable tool for students and educators, enhancing the quality of academic research and facilitating the dissertation review process.
