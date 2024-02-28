# The Cognitive Type project

*Mapping Typography to Cognition*

The Cognitive Type Project is about creating computational tools which will allow the design of beautiful typefaces which have different cognitive properties. This will allow typographers to design type for such things as better click-through rates on Google ads, children's books that improve reading levels, or companies that better understand how their customers react to the text in their media. 

The basic idea is that it is well known that different typefaces have different cognitive properties. Most people will find some type more readable or more beautiful. What is not known is exactly which visual characteristics of a type such as a serif, the x-height map to visual properties like readability or beauty. Recent advances in AI now allow us to create tools that map visual characteristics of type to cognition.  

## Abstract

Reading is a fundamental process through which we acquire information and learn. This is especially true for online education where the presentation of information can solely be through text and images. Understanding the relationship a font has on recall and comprehension is valuable to ensure understanding of critical information. Of the few studies that have investigated the influence of font type on information recall, data has shown that serif fonts significantly improve recall of information compared to sans serif fonts. The choice of font is often arbitrary, yet it can significantly impact readability and comprehension.

This research aims to create public datasets and deep learning models which map a detailed “anatomy of type” to eye tracking data of people reading and answering questions on short passages of text. We plan to extend existing datasets with a focus on the detailed physical characterization of type and its cognitive effects.

## Classification of Latin-Typefaces

- **PANOSE Classification System:** The PANOSE Classification System is a comprehensive tool for categorizing typefaces based on ten specific visual attributes. These attributes are designed to capture the most distinctive aspects of a font's appearance, enabling precise matching and identification. Here are the ten attributes used in the PANOSE system:

1. **Family Type:** Distinguishes between general design classes such as serif, sans serif, scripts, and decorative.

2. **Serif Style:** Identifies the type of serif present in a font (if any), such as no serifs, cove serifs, square serifs, etc.

3. **Weight:** Measures the visual thickness of the strokes, ranging from very light to very heavy.

4. **Proportion:** Describes the width of the characters in relation to their height, distinguishing between fonts that are expanded, normal, condensed, or very condensed.

5. **Contrast:** Indicates the degree of contrast between thick and thin strokes within the characters, from none to very high contrast.

6. **Stroke Variation:** Refers to the variation in stroke thickness, identifying whether the stroke widths are uniform or vary significantly.

7. **Arm Style:** Describes the design of the arms, legs, and tails of characters, such as straight arms/horizontal, straight arms/wedge, etc.

8. **Letterform:** Focuses on the overall shape of the letters, considering aspects like normal/square, extended, or oval.

9. **Midline:** Indicates the position of the midline in characters (if applicable), which affects the appearance of lowercase letters, ranging from standard to high or low.

10. **X-height:** Measures the height of lowercase letters relative to the height of uppercase letters, identifying whether the x-height is short, medium, or tall.

By analyzing a typeface across these ten dimensions, the PANOSE system provides a nuanced and detailed approach to font classification. This enables software and designers to find the closest possible matches among fonts, ensuring that text appearance remains consistent even when the original font is not available. This level of detail helps maintain design integrity across various digital platforms and documents.

- **ATypI Classification (Vox-ATypI Classification):** Originally developed by Maximilien Vox in 1954 and later adopted by the Association Typographique Internationale (ATypI), this system categorizes typefaces into 11 general classes, such as Humanist, Garalde, Transitional, etc. It is one of the most widely recognized classification systems in the typographic community.

- **British Standards Classification (BS 2961):** Issued by the British Standards Institution, this system provides a different approach to classifying typefaces based on characteristics such as x-height, character width, and contrast between thick and thin strokes.

- **DIN 16518:** A German standard classification system for typefaces developed in 1964. It classifies typefaces into groups based on their historical and stylistic characteristics, similar to the Vox-ATypI system but with some differences in categories and definitions.

- **Alessandrini System:** Jean Alessandrini proposed a classification system that focuses on the visual and stylistic aspects of typefaces, grouping them into broader categories that reflect their overall appearance and mood, rather than their historical roots.

- **Bringhurst's System:** In "The Elements of Typographic Style," Robert Bringhurst proposes a system based on the evolution and characteristics of typefaces, from Renaissance letterforms to modern digital types. While not a formal classification system, it provides a framework for understanding the development and characteristics of type.

- **TypeLogic:** This is a less conventional system that categorizes typefaces based on their perceived personality and emotional impact, rather than their physical characteristics. It's more subjective and is used in design contexts to match typefaces with the desired tone of a project.

Each of these systems offers a unique lens through which to view and classify typefaces, catering to different needs and perspectives within the design and typographic communities. The choice of system often depends on the specific requirements of a project, the historical or stylistic focus of a designer, or the need for compatibility with existing classification standards.

## Keywords

Typography, Reading, Education, Reading Comprehension, Deep Learning.

## Introduction

Despite the well-known effects of typeface on readability, productivity, and comprehension, there are no datasets or tools that enable a detailed study of physical characteristics of type and their cognitive implications. This project seeks to fill that gap by creating open source datasets and computational tools for analyzing and designing typefaces based on cognitive properties.

## Expected Results

- Foundation Models.


## Appendix A - References

- Coles, S. (2012). *The Anatomy of Type*. Harper Design, US.
- Coles, S. (2013). *The Geometry of Type*. Thames & Hudson, UK.
- Dalmaijer, E.S., Mathôt, S., & Van der Stigchel, S. (2014). PyGaze: an open-source, cross-platform toolbox for minimal-effort programming of eye tracking experiments. *Behavior Research Methods, 46*, 913-921. doi:10.3758/s13428-013-0422-2.
- French, M. M. J.; Blood, A.; Bright, N. D.; Futak, D.; Grohmann, M. J.; Hasthorpe, A.; Heritage, J.; Poland, R. L.; Reece, S.; & Tabor J. (2013). Changing fonts in education: How the benefits vary with ability and dyslexia. *The Journal of Educational Research, 106*(4), 301-304. doi: 10.1080/00220671.2012.736430.
- Gasser, M.; Boeke, J.; Haffernan, M.; Tan, R. (2005). The influence of font type on information recall. *North American Journal of Psychology, 7*(2), 181-188.
- Halin, N. (2016). Distracted while reading? Changing to a hard-to-read font shields against the effects of environmental noise and speech on text memory. *Frontiers in Psychology, 7*(1196), 570 - 590. doi: 10.3389/fpsyg.2016.01196.
- Haralambous, Yannis. (2007). *Fonts & Encodings*. O’Reilly Press. ASIN: 0596102429.
- Kanfer, R. & Ackerman, P. L. (1989). Motivation and cognitive abilities: An integrative/aptitude-treatment interaction approach to skill acquisition. *Journal of Applied Psychology, 74*, 657-690.
- Krafka K, Khosla A, Kellnhofer P, Kannan H, Bhandarkar S, Matusik W, & Torralba A. (2016). Eye Tracking for Everyone. IEEE Conference on Computer Vision and Pattern Recognition (CVPR).
- McNamara, D. S., Kintsch, E., Butler-Songer, N., & Kintsch, W. (1996). Are good texts always better? Text coherence, background knowledge, and levels of understanding in learning from text. *Cognition and Instruction, 14*, 1–43.
- Magre N, Brown N. (2022). Typography-MNIST (TMNIST): an MNIST-Style Image Dataset to Categorize Glyphs and Font-Styles. arXiv:2202.08112 [cs.CV].
- Oppenheimer, D.M., & Frank, M.C. (2007). A rose in any other font would not smell as sweet: Effects of perceptual fluency on categorization. *Cognition* (2007), doi:10.1016/j.cognition.2007.05.020.


