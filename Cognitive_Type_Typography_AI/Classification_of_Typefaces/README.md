# Type Classification Systems



1. [The Panose-1 Classification](#the-panose-1-classification)
2. [Vox-ATypI Classification](#vox-atypi-classification)
3. [IBM's Classification of Fonts](#ibms-classification-of-fonts)
4. [The Alessandrini Classification of Typefaces: Codex 80](#the-alessandrini-classification-of-typefaces-codex-80)
5. [The British Standards Classification of Typefaces (BS 2961)](#the-british-standards-classification-of-typefaces-bs-2961)
6. [DIN 16518](#din-16518)
7. [Bringhurst's System](#bringhursts-system)




## The Panose-1 Classification

The Panose-1 Classification is a detailed system for describing Latin fonts through a 10-number code, each ranging from 0 to 15, representing various typographic attributes. This method turns a font into a vector in a 10-dimensional space, allowing for the calculation of the distance between two fonts based on their characteristics such as family kind, serif style, weight, proportion, contrast, stroke variation, arm style, letterform, midline, and x-height. Originally developed by Ben Bauermeister around 1982, Panose-1 was integrated into TrueType and Windows 3.1 by Microsoft in 1990, showcasing its utility in font identification and compatibility across digital platforms.

The Panose-1 Classification system uses a 10-number code to describe key characteristics of Latin typefaces. Each digit in this code represents a different attribute of a font, such as its family kind, serif style, weight, proportion, and contrast among others. This allows for precise identification and matching of fonts by comparing these attributes. The system enables a nuanced approach to font classification, facilitating the selection and pairing of typefaces in digital design and typography by quantifying typographic similarities in a standardized format.

The Panose-1 Classification system is detailed and structured around 10 key characteristics, each providing a nuanced approach to font classification. These characteristics are as follows:

1. **Family Kind**: Classifies the overall type of the font, with six possible values:
   - 0: Any type of font
   - 1: No fit with any other types
   - 2: Latin text
   - 3: Handwritten
   - 4: Decorative
   - 5: Symbol font

2. **Serif Style**: Focuses on the serif design, offering 16 possibilities ranging from no serif to various serif styles like cove, square, thin, oval, triangle, and rounded.

3. **Weight**: Describes the font's weight from very light to extra black, indicating the visual heaviness of the stroke.

4. **Proportion**: Identifies the font's proportion, including old style, modern, even width, extended, condensed, very extended, very condensed, and monospaced.

5. **Contrast**: Measures the difference between the thickest and thinnest parts of the letters, from no contrast to very high contrast.

6. **Stroke Variation**: Examines how the stroke width changes across a character, including no variation, gradual/diagonal, gradual/vertical, rapid/vertical, and instant variations.

7. **Arm Style and Termination of Open Curves**: Looks at the style of the font's arms (straight or not) and the termination of open curves, differentiating between horizontal, wedge, and vertical terminations, with or without serifs.

8. **Slant and Shape of the Letter 'O'**: Assesses the slant (normal or oblique) and the overall shape of the letter 'O', such as contact, weighted, boxed, flattened, rounded, off-center, and square.

9. **Midlines and Apexes**: Focuses on the height of the midlines (standard, high, constant, low) and the style of the apexes (trimmed, pointed, serifed) of letters like 'E' and 'A'.

10. **X-Height and Behavior of Uppercase Letters Relative to Accents**: Addresses the ratio of lowercase letter height to uppercase letter height and notes any peculiar behavior in accented uppercase letters.

This comprehensive classification allows for a detailed analysis and comparison of typefaces, enabling designers to find fonts with similar characteristics or to understand the nuanced differences between fonts in a systematic manner.

## Vox-ATypI Classification

The ATypI Classification, also known as the Vox-ATypI classification, is a system used to categorize typefaces based on their characteristics and historical influences. Originally devised by French typographer Maximilien Vox in 1954, it was later adopted and expanded by the Association Typographique Internationale (ATypI). This system classifies typefaces into 11 main categories, each reflecting distinct stylistic and historical attributes. These categories provide a framework for understanding the evolution of typeface design and for identifying the visual and structural characteristics of different fonts. Here's a detailed look at each category within the Vox-ATypI classification:

- Humanist: Inspired by the handwriting of Italian Renaissance scribes, Humanist typefaces are characterized by a strong calligraphic influence, evident in their varied stroke weights and serifs that resemble pen strokes. This category includes the earliest Roman typefaces, such as those designed by Nicolas Jenson.

- Garalde: Named after Aldus Manutius' punchcutter Francesco Griffo (Garalde is a portmanteau of Garamond and Aldine). These typefaces, from the 16th century, show an evolution from Humanist designs, with more contrast between thick and thin strokes, and more uniform serifs.

- Transitional: Marking the transition between Garalde and Didone typefaces, these fonts, epitomized by John Baskerville's work in the 18th century, feature greater contrast between thick and thin lines, sharper serifs, and a more vertical axis.

- Didone: Characterized by strong contrast between thick and thin lines, narrow and unbracketed serifs, and a vertical stress in the letters, Didone typefaces emerged in the late 18th century. They are associated with designers like Firmin Didot and Giambattista Bodoni.

- Slab Serif: Also known as Egyptian, these typefaces, which originated in the early 19th century, feature thick, block-like serifs. They were designed for advertising and display purposes and include variations with rounded edges and more refined proportions.

- Sans Serif: This class includes typefaces without serifs, characterized by clean, simple lines. They can be further divided into subcategories such as Grotesque, Neo-grotesque, Geometric, and Humanist, each with distinct characteristics.

- Script: Mimicking handwriting, Script typefaces range from formal styles, based on seventeenth and eighteenth-century writing masters, to more casual, contemporary designs. They often feature connecting letters.

- Graphic: A broad category that encompasses decorative fonts and those designed for specific purposes or effects, not fitting into the traditional classifications. These can include display, novelty, and artistic fonts.

- Blackletter: Also known as Gothic or Fraktur, these typefaces are based on medieval script and characterized by their dense, dark appearance and ornate detail. They were commonly used in Europe before the Renaissance.

- Glyphic: Encompassing typefaces that mimic inscriptions or engraving, Glyphic fonts often have flared or tapered strokes and may include serifs that are integrated into the letterform rather than added as separate elements.

- Non-Latin: This category acknowledges the vast world of typefaces designed for scripts other than Latin, recognizing the global diversity of typography. It includes fonts for scripts such as Cyrillic, Greek, Arabic, Indic, East Asian, and more.

The Vox-ATypI classification provides a comprehensive framework for understanding the vast landscape of typeface design, reflecting both the evolution of typographic style and the broad diversity of letterforms. By categorizing fonts into these classes, the system helps designers, typographers, and enthusiasts to appreciate the nuances of typeface selection and application.

## IBM's Classification of Fonts

IBM's Classification of Fonts, utilized in the OS/2 table of TrueType fonts, divides typefaces into 10 classes, each with specific subclasses to further categorize fonts based on characteristics and historical context. This system includes:

- Class 0: No Classification
- Class 1: Old-Style Serifs, subdivided into subclasses for various styles like IBM rounded legibility, garalde, Venetian, and more.
- Class 2: Transitional Serifs, identifying typefaces that bridge old-style and modern serif designs.
- Class 3: Modern Serifs, focusing on the "modernity" of didones.
- Class 4: Clarendon Serifs, for industrial typefaces with pronounced serifs.
- Class 5: Slab Serifs, highlighting mechanistic typefaces.
- Class 7: Free-Form Serifs, a unique category for fonts like Souvenir.
- Class 8: Sans Serif, with subclasses for different styles including IBM neo-grotesque gothic and humanist.
- Class 9: Ornamentals, covering gothic, engraved, and shadowed typefaces.
- Class 10: Scripts, not distinguishing between manual and script typefaces, and including subclasses for uncial, brush joined, formal joined, and more.

Each class and subclass provides a framework to classify fonts by their visual characteristics, historical origins, and stylistic features.

## The Alessandrini Classification of Typefaces: Codex 80 

The Alessandrini Classification of Typefaces, introduced in Codex 80 by Jean Alessandrini in 1979, offers a detailed and innovative approach to categorizing typefaces, drawing inspiration from the biological classification of species. This classification is distinctive for its comprehensive framework, including 19 preliminary designations, two orthogonal modifiers, and five additional lists of qualifiers, enriched with creative neologisms and a touch of humor. Here's a detailed breakdown of how this classification works:

### Preliminary Designations (Dénominations Préliminaires)
Alessandrini introduces 19 preliminary categories for typefaces, each with unique characteristics:

1. **Simplices**: Refers to sans-serif typefaces, emphasizing that all typefaces consist of lines, thereby critiquing the term "lineal."
2. **Emparectes**: Denotes Egyptian typefaces known for their strictly rectangular serifs, differentiating from Vox's "mechanistic" category.
3. **Emparectes à Congés**: Features Egyptian typefaces with a rounding effect between the downstroke and the serif.
4. **Deltapodes**: Identifies typefaces with delta-shaped (triangular) serifs, a category not anticipated by Vox.
5. **Deltapodes à Congés**: Covers Deltapodes with rounded serifs.
6. **Filextres**: Refers to typefaces with threadlike serifs, a nod to Didones.
7. **Claviennes**: Lumps all varieties of Roman typefaces into one category, based on serifs shaped like nail heads.
8. **Romaines**: Specifically applies to incised typefaces inspired by engraving in marble.
9. **Gestuelles Calligraphiques**: Encompasses scripts based on pen-drawn calligraphic scripts.
10. **Gestuelles Brossées**: Pertains to scripts drawn with a brush, reflecting everyday handwriting rather than formal calligraphy.
11. **Onciales**: Represents scripts inspired by uncial handwriting, including what are commonly known as Celtic scripts.
12. **Germanes**: Refers to Gothic typefaces, acknowledging the cultural stereotype associated with Gothic script in Northern Europe.
13. **Aliennes**: Encompasses all non-Latin scripts, reflecting a Latin-centric view.
14. **Exotypes**: Identifies Latin typefaces that simulate non-Latin scripts, often used in advertising.
15. **Machinales**: Covers typefaces from the 1970s inspired by OCR fonts used in administrative documents.
16. **Ludiques**: Denotes typefaces designed more for amusement than readability.
17. **Hybrides**: Applies to typefaces combining elements from multiple categories.
18. **Transfuges**: Refers to typefaces whose different weights span several categories.

### Orthogonal Modifiers (Éventualités)
Two orthogonal qualifications complement the preliminary designations:

1. **Diagones**: Pertains to italics and slanted typefaces, with variations like mini-diagones, maxi-diagones, and anti-diagones indicating the degree of slope.
2. **Stenciliennes**: Refers to stenciled letters, popular in the 1970s.

### Additional Lists of Qualifiers
Alessandrini further refines classification with five lists of qualifiers:

1. **Objective Formal Considerations**: Includes attributes like light, bold, extended, shadowed, three-dimensional, etc.
2. **Historical Reference Points**: Lists periods like Archaic, Renaissance, Modern, etc.
3. **Aesthetic and Stylistic Considerations**: Features styles like Classical, Baroque, Pop, etc.
4. **Subjective Formal Considerations**: Offers a list that can be extended to include terms like monotone, expressive, dramatic, etc.
5. **Geographic Areas and Original Aspects**: Focuses on the geographical origin of typefaces.

This classification system stands out for its depth, flexibility, and the creative lexicon introduced by Alessandrini. Despite receiving a lukewarm reception from the printing profession, largely due to its departure from tradition and the emphasis on 1970s typefaces, Alessandrini's Codex 80 offers a rich, albeit unconventional, framework for understanding and categorizing the diversity of typefaces beyond the constraints of earlier systems.

## The British Standards Classification of Typefaces (BS 2961)

The British Standards Classification of Typefaces (BS 2961) is a system developed in the United Kingdom for classifying typefaces systematically. Unlike the more general and stylistic approaches such as the ATypI (Vox-ATypI) classification, the BS 2961 standard provides a structured method, focusing on specific attributes of typefaces to categorize them. While it shares the goal of classifying typefaces to facilitate understanding and selection, the specifics of the BS 2961 system are distinct and tailored to align with British standards for typography.

However, as of my last update, detailed, attribute-by-attribute breakdowns similar to the Panose-1 system for BS 2961 specifically were not widely documented or disseminated in public resources. The British Standards Classification system was designed to cover various aspects of typography and printing practices, but the detailed attributes it uses for classifying typefaces—such as serif style, weight, proportion, and others—are not as publicly and precisely outlined as in the Panose-1 system.

The BS 2961 system would likely categorize typefaces based on several key attributes, potentially including:

1. **Typeface Family**: Similar to Panose-1's Family Kind, classifying typefaces into broad categories based on their general appearance and purpose (e.g., serif, sans-serif, script).

2. **Serif Style**: Identifying the style of serifs if present, which could range from traditional to contemporary, and including specific shapes and forms.

3. **Weight**: The visual heaviness of the typeface, from light to bold or black, affecting readability and emphasis in text.

4. **Width/Proportion**: The relative width of characters, which could influence text density and aesthetic appeal.

5. **X-Height**: The height of lowercase letters relative to capital letters, affecting readability and overall visual balance.

6. **Contrast**: The degree of variation between thick and thin strokes within characters, a feature that can dramatically affect the typeface's character.

While this structure would logically align with the principles of type classification, the specific implementation of these or other attributes in BS 2961 is less commonly discussed in widely accessible typographic literature or resources. The system was intended for use within the UK's printing and design industries to standardize typeface classification, which could include more technical specifications and standards relevant to those fields.

For precise details on how the BS 2961 classification system is structured and the specific attributes it employs, one would typically refer to the official documentation provided by the British Standards Institution (BSI). This documentation would offer the authoritative guide on how typefaces are classified under this system, including any updates or revisions to the classification criteria over time.


## DIN 16518

The DIN 16518 classification system is a German standard for categorizing typefaces based on their characteristics and historical development. Established by the Deutsches Institut für Normung (German Institute for Standardization), this system organizes typefaces into groups that reflect their stylistic and structural features. Unlike the Panose-1 system, which is based on specific, quantifiable attributes of typefaces, the DIN 16518 system groups typefaces more historically and stylistically. Here's a detailed breakdown of how the DIN 16518 classification system works:

1. **Group I: Venetian Renaissance Antiqua (Venetian)**
   - Characterized by: Low contrast between thick and thin strokes, diagonal stress on curves, and slanted serifs. These typefaces are inspired by the early Italian Renaissance and include typefaces similar to those used by Aldus Manutius.

2. **Group II: French Renaissance Antiqua (Garalde)**
   - Characterized by: Increased contrast between thick and thin strokes compared to Venetian Antiquas, a more vertical stress, and bracketed serifs. This group includes typefaces inspired by the work of Claude Garamond and his contemporaries.

3. **Group III: Baroque Antiqua (Transitional)**
   - Characterized by: Even greater contrast between thick and thin strokes, less pronounced bracketing on serifs, and a more vertical axis. Transitional typefaces bridge the gap between the Garalde and Didone styles, with John Baskerville's typefaces being prime examples.

4. **Group IV: Classical Antiqua (Didone)**
   - Characterized by: Strong contrast between thick and thin strokes, straight serifs without brackets, and a strictly vertical stress. These typefaces emerged in the late 18th century, with Bodoni and Didot being notable examples.

5. **Group V: Slab Serif (Egyptian)**
   - Characterized by: Thick, block-like serifs and little to no contrast between thick and thin strokes. This group emerged in the early 19th century, designed for advertising and display purposes.

6. **Group VI: Grotesque Sans Serif**
   - Characterized by: Uniform stroke width and no serifs, with a somewhat crude and irregular design. These are early sans serif designs from the 19th and early 20th centuries.

7. **Group VII: Neo-Grotesque Sans Serif**
   - Characterized by: More refined than grotesque sans serifs, with uniform stroke width and a more harmonious geometric structure. Helvetica is a quintessential example of this group.

8. **Group VIII: Geometric Sans Serif**
   - Characterized by: Simple, geometric shapes forming the basis of letterforms, with uniform stroke width and no serifs. Futura is a well-known example of this style.

9. **Group IX: Humanist Sans Serif**
   - Characterized by: Variation in stroke width and more organic, calligraphic forms, reflecting humanist handwriting influences. Gill Sans and Optima are examples of this group.

10. **Group X: Scripts and Calligraphic Typefaces**
    - Includes typefaces that mimic handwritten text, ranging from formal scripts based on calligraphy to more casual, cursive styles.

11. **Group XI: Blackletter (Gothic)**
    - Characterized by: The dense, ornate letterforms typical of medieval manuscript hand. This category includes Textura, Fraktur, and Schwabacher styles.

12. **Group XII: Broken Scripts (Gebrochene Schriften)**
    - A subset of Blackletter, these include typefaces with a more 'broken' appearance, typically used in Germany until the mid-20th century.

The DIN 16518 system provides a historical and stylistic framework for classifying typefaces, emphasizing the evolution of type design from the Renaissance to the modern era. By grouping typefaces into these categories, the system helps users understand the historical context and stylistic nuances of different fonts, aiding in the selection process for various typographic projects.

## Bringhurst's System

Robert Bringhurst's system for classifying typefaces, detailed in his seminal work "The Elements of Typographic Style," proposes a more nuanced and historical approach compared to many classification systems like Panose-1. Bringhurst's system is deeply rooted in the history of typography and the evolution of typeface design, reflecting a blend of technical, cultural, and aesthetic considerations. Unlike systems that categorize typefaces based on specific physical characteristics alone, Bringhurst's method also considers the historical and stylistic lineage of typefaces.

While Bringhurst does not lay out a simple, numbered classification system akin to DIN 16518 or the Vox-ATypI classification, his approach can be summarized by identifying key historical and stylistic periods of type design, each with its defining characteristics. Here’s an overview inspired by the principles found in "The Elements of Typographic Style," tailored to resemble the structure requested:

1. **Humanist or Old Style**: Reflects the influence of early Italian Renaissance letterforms, characterized by moderate contrast between thick and thin strokes, a diagonal stress, and bracketed serifs. This style mimics the look of pen-drawn letters.

2. **Transitional**: Marks the evolution from Old Style to Modern typefaces, with greater contrast between thick and thin strokes, more vertical stress, and less pronounced bracketing on the serifs. This style bridges the gap with a balance between old and new.

3. **Neoclassical & Didone**: Known for extreme contrast between thick and thin strokes, vertical axis, and fine, unbracketed serifs. These typefaces emerged in the late 18th century, showcasing elegance and precision.

4. **Slab Serif**: Features robust, block-like serifs and minimal contrast between strokes. Originating in the 19th century, this style varies from geometric to more humanist approaches.

5. **Sans Serif**: Encompasses a broad category from Grotesque to Geometric, Humanist, and Neo-grotesque sans serif designs. These typefaces are defined by the absence of serifs and have various letter shapes based on geometric simplicity or more organic, humanist forms.

6. **Script**: Includes typefaces that resemble handwritten text, from formal, elegant scripts to casual, informal styles. These fonts mimic the fluidity and variance of handwriting.

7. **Blackletter**: Characterized by dense, intricate letterforms that harken back to medieval manuscript calligraphy. This style is distinguished by its textured, ornate appearance.

8. **Decorative and Display**: A broad category that encompasses a variety of typefaces designed for specific uses, effects, or to capture attention. These fonts often prioritize aesthetic expression over readability.

9. **Non-Latin Scripts**: Acknowledges the vast diversity of type design beyond the Latin alphabet, covering scripts from around the world, each with its own historical and cultural significance.

Bringhurst’s system is deeply informative, providing insight into the evolution of typeface design and encouraging typographers to consider the historical context and intended use of typefaces in their work. This approach helps designers make more informed choices that enhance the readability, beauty, and function of printed and digital texts.


