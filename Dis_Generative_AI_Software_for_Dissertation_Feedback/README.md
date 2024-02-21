# Dis - Generative AI Software for Dissertation Feedback: Requirements Document

# Building Generative AI Software for Dissertation Feedback

## Core Functionality

This generative AI software, named "Dis", serves as an advanced critique partner for PhD students, offering meticulous reviews of their dissertation work. Utilizing a users chosen Language Learning Model (LLM) from a list of options, it analyzes each part of the dissertation, from the abstract to the conclusion, ensuring feedback is both comprehensive and section-specific.

## Feedback Mechanism

### What Was Done Well

- The software identifies strengths within the dissertation, such as compelling arguments, innovative methodologies, thorough literature reviews, clear data presentation, and impactful conclusions. This positive feedback helps students recognize their work's value and boosts confidence.

### Suggestions for Improvement

- Beyond identifying weaknesses, the AI provides constructive suggestions, including recommendations for deeper literature analysis, more robust statistical methods, addressing research gaps, and advice on writing clarity and structure. These suggestions aim to be directly actionable, guiding students toward meaningful improvements.

## Integration with Language Learning Models (LLM)

- Students can select an LLM tailored to their dissertation's subject area, allowing for specialized, relevant feedback. This could range from models excelling in scientific analysis for STEM fields to those adept at nuanced language interpretation for humanities and social sciences.

## Aggregated Feedback Reports

- After section-wise analysis, the software compiles the feedback into a comprehensive report, offering a systematic, prioritized roadmap for dissertation revision. This report is structured to mirror the dissertation's sections, providing clear guidance on strengths and improvement areas.

## Technical and Ethical Considerations

### Accuracy and Relevance

- Ensuring feedback accuracy and relevance requires the AI to be trained on diverse academic texts and feedback samples, tailored to the dissertation's discipline.

### User Interface (UI)

- The software should feature an intuitive UI, simplifying the process for students to upload their work, choose their preferred LLM, and understand the feedback provided.

### Confidentiality and Integrity

- Protecting the confidentiality of dissertations and feedback reports is paramount, safeguarding students' original work.

### Bias and Fairness

- The software must address potential AI biases to ensure feedback is fair and equitable across various fields of study, methodologies, and writing styles.


By providing detailed, constructive feedback tailored to each dissertation section, this generative AI software concept aims to significantly enhance the academic writing process for PhD students, supporting the production of high-quality research work.


*PhD Dissertation Structure*  

A PhD dissertation typically comprises several structured sections, each serving a specific purpose in the research and presentation of the work. While the exact structure can vary depending on the academic discipline, institution, and country, a standard PhD dissertation often includes the following sections:

## Title Page

- The first page of the dissertation that includes the title, author's name, institution, department, date of delivery, research mentor(s) and advisor, their institutions, and email addresses.

## Abstract

- A concise summary of the dissertation, usually about 250-350 words, summarizing the research question, methodology, results, and conclusions.

## Acknowledgements

- An optional section where the author thanks those who have helped them during their research and writing process.

## Table of Contents

- Lists the chapters and major sections of the dissertation, including figures and tables, if applicable.

## List of Figures and Tables (if applicable)

- Lists the figures and tables included in the work, along with their page numbers.

## Introduction

- Introduces the research topic, outlines the research problem, states the research questions, and provides an overview of the dissertation structure.

## Literature Review

- Surveys existing research related to the topic, identifying gaps in the literature that the dissertation aims to fill.

## Methodology

- Describes the research design, data collection methods, and analytical techniques used to conduct the research.

## Results

- Presents the findings of the research, often accompanied by tables, graphs, and statistical analysis, without interpreting the results.

## Discussion

- Interprets the results, explaining how they answer the research question, their implications, and their relationship to existing literature.

## Conclusion

- Summarizes the research findings, discusses their implications, suggests areas for future research, and provides a concluding remark.

## References/Bibliography

- Lists all the sources cited in the dissertation in a consistent format, following the specific guidelines of the citation style used.

## Appendices (if applicable)

- Contains supplementary material that is not essential to the understanding of the dissertation's main text, such as raw data, detailed methodologies, or additional analyses.

This structure ensures a coherent and logical presentation of the research work, allowing readers to understand and evaluate the research process and findings. Different disciplines may have specific requirements or preferred structures, so it's essential to consult your department's guidelines.


# Dis Requirements

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

## 4. Summary

This document has outlined the requirements for a Generative AI software designed to provide detailed feedback on PhD dissertations. By meeting these requirements, the software will serve as a valuable tool for students and educators, enhancing the quality of academic research and facilitating the dissertation review process.
