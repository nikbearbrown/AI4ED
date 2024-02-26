# Visual Design

If you don't have a lot of experience with generative AI it is recommended that you use prompt-based generative AI to create images for visual design.

Using prompt-based generative AI to create images opens up exciting possibilities for visual design. Prompt-based generative models, like GPT-3, DALL-E, Leanardo.ai or Midjounrey can be used to generate images based on textual descriptions or commands, allowing designers to ideate and explore various visual concepts in a creative and interactive manner.

The focus should be think of what types of concept sketching might be useful of the companies judging the hackathon: Microsoft, Phillips, Amazon, Vui.com, Gaia AI, and Squark AI.

* Concept Sketching: Designers can use natural language prompts to describe their visual ideas or concepts. The generative AI can then transform these textual descriptions into rough sketches or outlines, helping designers quickly visualize their thoughts on paper without the need for advanced drawing skills. This accelerates the concept generation process and allows for rapid iterations.   

* Branding, Poster and Logo Design: Designers can utilize generative AI to assist in logo creation or branding elements. They can describe their brand's personality, values, and target audience through prompts, and the AI can generate logos or visual brand assets that align with the specified characteristics. This can help in brand identity exploration and save time during the design process. 

* Storytelling and Visualization: Prompt-based generative models can be used to generate illustrations or visual elements for storytelling purposes. Authors, game developers, or filmmakers can provide descriptive prompts for scenes or characters, and the AI can produce corresponding images to enhance the narrative.  

* Product Prototyping and Visualization: Designers can leverage generative AI to create visualizations of product prototypes without having to go through the entire design process. By describing product features and design elements, the AI can produce images of potential product variations, aiding in decision-making and communication with stakeholders.   

* Data Visualization and Infographics: By providing data and information in text form, designers can utilize generative AI to create custom data visualizations or infographics. This can enhance the presentation of complex data and make it more accessible to a broader audience.    

While generative AI is a powerful tool for visual design, it is important to remember that it complements rather than replaces human creativity. Designers should use these AI-generated visuals as a starting point for inspiration, exploration, and ideation, refining and adding their personal touch to the final designs. Additionally, ethical considerations, transparency, and validation are essential when using AI in design, ensuring the generated content aligns with ethical guidelines and the brand's values.  

## Step 0 - Collaboration and Folder

Please have a team member add GitHub ID as a collaborator to this repository.  You will create a subfolder for your team.  The judges will be instructed to incorporate how well your repository is organized and commented in their final scores.

## Step 1 - The Anatomy of Prompts

The goal is not just to generate useful visualizations and designs, but to generate code and rules that can generate many designs for a particular purpose. You can prompt however you want but this approach generated stunning results. You can see examples at the Computational Art Lab IG [https://www.instagram.com/artlabneu/](https://www.instagram.com/artlabneu/) and the Skunks.ai IG [https://www.instagram.com/skunks.ai/](https://www.instagram.com/skunks.ai/).  


Think of a prompt as a sequence of tags and categorize all the tags into four meta-categories:

1) Subject  
2) Style  
3) Composition   
4) Boosters  

Refer to the image below for an illustration of the prompt structure:

<img src="https://raw.githubusercontent.com/aiskunks/Generative_AI_Hackathon/main/Art/Anatomy_of_Prompts_GAI.png">


## Step 2 - Generating Tag List Set
To generate a tag list set for your chosen topic, utilize the following resources:

* ChatGPT/Bard  
* Kaggle Datasets: [https://www.kaggle.com/nikbearbrown/datasets ](https://www.kaggle.com/nikbearbrown/datasets)  
* Private Datasets
* Begin with the 55K Midjourney Tags in a Topic Taxonomy dataset: [https://www.kaggle.com/datasets/nikbearbrown/55k-midjourney-tags-in-a-topic-taxonomy](https://www.kaggle.com/datasets/nikbearbrown/55k-midjourney-tags-in-a-topic-taxonomy)  

Follow the "Tag, Categories" style when categorizing the tags. For example:

Tag: yoji shinkawa

Categories:

1971 births, Konami people, Japanese illustrators, Living people, Video game artists

_Please upvote any datasets that you find useful._

Organize your tagset within the appropriate GitHub directory. For instance, if your topic is Game Art, place the tags in the "Tags" folder within the "Game_art" subdirectory.

## Step 3 - Prompt Engineering Experiments

Conduct prompt engineering experiments for your topic and document the results in a Jupyter notebook. Treat the notebook as a journal to record your experiments, including images with well-crafted prompts for your topic.

Ensure that all images are placed in the "Images" subdirectory and are renamed using the alpha_numeric_opt.py script before uploading them to GitHub. See [https://github.com/aiskunks/zebonastic/tree/main/PYZ](https://github.com/aiskunks/zebonastic/tree/main/PYZ)  

Rewrite the contents of the README.md files in a way that is relevant and coherent to your chosen topi

# A simple example of prompt generation

The function *generate_random_text* assumes there are 6 lists that have text elements. The lists are called subjects, actions,
places, styles, formats, and boosters.

The text prompt returned has the following structure
1. Subject - exactly 1 element from the subjects list
2. Action  -  0 or 1 elements from the actions list
3. Place  - 0 or 1 elements from the places list
4. Style  - 0 to 2 elements from the styles list with no duplicates
5. Format - 0 to 2 elements from the formats list with no duplicates
6. Booster - 0 to 5 elements from the boosters list with no duplicates

## Creating a Custom Subject Specific Prompt Generator (Shoe Example)

Let's use the Zebonatistic prompt model to create a custom prompt generator for shoes.  Use your expertise to create subject specific prompt generators.

One basically asks the question, what are the elements of a shoe image and related that to the basic *Anatomy of a Midjourney prompt* model.

Anatomy of a Midjourney prompt
1. Subject (1) - person, animal, character, location, object, etc.
2. Action (0.1) - jumping, dancing, posing, etc.
3. Place (0,1) - supermarket, Venice beach, Eiffel Tower, etc.
4. Style (0,2) - Expressionism, Steampunk, Renaissance, Pop Art, etc.
5. Format (0,2) -  , etc.
6. Booster (0,5) -  , etc.
7. Perspective (0,1) -  , etc.
8. View (0,1) - Portrait, headshot, closeup, birds-eye view, etc.
9. Artists (0,3) -  , etc.
10. Medium (0,1) - photo, painting, illustration, sculpture, doodle, tapestry, etc.
11. Environment (0,1) - indoors, ouaitdoors, on the moon, in Narnia, underwater, the Emerald City, etc.
12. Lighting (0,1) - soft, ambient, overcast, neon, studio lights, etc
13. Color (0,5) - ibrant, muted, bright, monochromatic, colorful, black and white, pastel, etc.
14. Mood (0,1) - Sedate, calm, raucous, energetic, etc.
15. Time Travel (0,1) - 1700s, 1960s, 2070s, etc.
16. mj_prompt (0,1) - an existing mj prompt that has worked
17. Midjourney parameters (0,2)  , etc.

All of the above relates to shoes but we will remove action to show that elements can be removed from a prompt generator. However a lot of shoe specific stuff is missing such as the type of shoe, the fabric of the shoe, the brand of shoe, etc.  Further we may want to make the camera view specific to shots used in shoe photography, design and illustration.

The Zebonatic 9999 lists [https://www.etsy.com/shop/Zebonastic](https://www.etsy.com/shop/Zebonastic) are extremely useful for inspiration. These are lists of randomly selected prompts from the millions of prompts the were posted to the public Midjourney that contain a term like "shoes".  The 9999 lists also come with python formatted "mj_prompts" lists, and term counts of terms that co-occur with the term shoes.

## Using ChatGPT to create term lists

The "Prompt Playground" section [https://www.etsy.com/shop/Zebonastic](https://www.etsy.com/shop/Zebonastic) has many ChatGPT term lists for sale, all for $0.99 or less, so if your time is worth more than a $1 per hour that may be an option.

However, all of the Zebonatic tools are intended to serve as a starting point and you may need to use your expertise to extend those lists using a tool like ChatGPT [https://chat.openai.com/](https://chat.openai.com/) or Bard [https://bard.google.com/](https://bard.google.com/)



Type in something like:

```bash

Can you list the top 44  shoe brands and put that in a python list?

````
 and get a response something like:

Certainly! Here's a list of the top 44 shoe brands as of my knowledge cutoff in 2021:


```python

shoe_brands = [
    "Nike",
    "Adidas",
    "Jordan",
    "Converse",
    "Reebok",
    "Vans",
    "Puma",
    "New Balance",
    "Under Armour",
    "ASICS",
    "Skechers",
    "Timberland",
    "Dr. Martens",
    "Salomon",
    "Merrell",
    "Brooks",
    "Fila",
    "Lacoste",
    "Clarks",
    "Hoka One One",
    "Gucci",
    "Balenciaga",
    "Prada",
    "Valentino",
    "Saint Laurent",
    "Versace",
    "Burberry",
    "Miu Miu",
    "Givenchy",
    "Alexander McQueen",
    "Christian Louboutin",
    "Jimmy Choo",
    "Hermès",
    "Bottega Veneta",
    "Dior",
    "Fendi",
    "Off-White",
    "Yeezy",
    "Balmain",
    "Maison Margiela",
    "Common Projects",
    "Rick Owens",
    "Vetements",
    "Acne Studios",
    "Isabel Marant"
]


````

This list includes a mix of popular athletic shoe brands as well as luxury fashion brands known for their footwear. Please note that the popularity of shoe brands may change over time, and newer brands may emerge.

Let's create some more lists *shoe_brands, shoe_fabrics, designers, colorful_foods, shoe_types, stitches, and clothing_patterns.* You can go wild and create as many relevent lists as you like.




#  Zebonastic Prompt Playground

The Zebonastic Prompt Playground is a Google colab notebook that helps play with prompts. It has lists of tens of thousands of terms related to the components of a midjourney prompt. That is, the subject, action, place, styles, format, booster, perspective, camera view, media type (illustration,photo or design, artistic inspiration, other mj prompts, and midjourney parameters.

To use the Zebonastic Prompt Playground you need to upload it to the free Google colab, and hit "Run All".  Please watch the Colab intro video [https://colab.research.google.com/](https://colab.research.google.com/) if unfamiliar with colab. The code is very simple and comes with python lists for the subject, action, place, styles, format, booster, perspective, camera view, media type (illustration,photo or design, artistic inspiration, other mj prompts, and midjourney parameters. It is intended as a sandbox to begin the play with prompt engineering and as a starting point for you to make the noteboook your own.


The Zebonastic Prompt Playground [https://www.instagram.com/zebonastic.ai/](https://www.instagram.com/zebonastic.ai/) works especially well with our 9999 Midjourney Prompts lists which, besides a .csv file, gives two text files with two formatted python lists called mj_prompts, which can be cut and pasted into the Zebonastic Prompt Playground Colab notebook to create prompts that are specific to a topic like fashion, game art, or data visualization.

Zebonastic has used this notebook the create over 50,000 stuning midjourney images some of which you can see at [https://www.instagram.com/zebonastic.ai/](https://www.instagram.com/zebonastic.ai/) and [https://www.etsy.com/shop/Zebonastic](https://www.etsy.com/shop/Zebonastic)

_*Anatomy of a Midjourney prompt*_

1. Subject (1) - person, animal, character, location, object, etc.
2. Action (0.1) - jumping, dancing, posing, etc.
3. Place (0,1) - supermarket, Venice beach, Eiffel Tower, etc.
4. Style (0,2) - Expressionism, Steampunk, Renaissance, Pop Art, etc.
5. Format (0,2) -  3D Render, Action Photography, Advertising Campaign, etc.
6. Booster (0,5) - #wow, 4k,Arnold Render, Beautiful, Blender 3d,Contest Winner  etc.
7. Perspective (0,1) -  85mm, Aerial View, Bokeh, Close Face, etc.
8. View (0,1) - Portrait, headshot, closeup, birds-eye view, etc.
9. Artists (0,3) - Wes Anderson, Arcimboldo, Pierre Auguste Renoir, Banksy, etc.
10. Medium (0,1) - photo, painting, illustration, sculpture, doodle, tapestry, etc.
11. Environment (0,1) - indoors, outdoors, on the moon, in Narnia, underwater, the Emerald City, etc.
12. Lighting (0,1) - soft, ambient, overcast, neon, studio lights, etc
13. Color (0,5) - vibrant, muted, bright, monochromatic, colorful, black and white, pastel, etc.
14. Mood (0,1) - Sedate, calm, raucous, energetic, etc.
15. Time Travel (0,1) - 1700s, 1960s, 2070s, etc.
16. mj_prompt (0,1) - an existing mj prompt that has worked
17. Midjourney parameters (0,2)  , etc.

The notebook is very simple, (1) means one of the element is required, (0,5) anywhere from zero to five elements of the type, for example, zero to five boosters might be added.

The user specifies the subject or lets the script assingn and random subject and hitting "Run All" generates num_prompts random prompt strings.

The strings can be pasted into midjourney or as English prompts that can be edited by hand.  Note that while you can choose to write your prompts like a traditional sentnce all Midjourney cares about is the keywords in the prompt string.

## Grammar

The Midjourney Bot does not understand grammar, sentence structure, or words like humans. Word choice also matters. More specific synonyms work better in many circumstances. Instead of big, try gigantic, enormous, or immense. Remove words when possible. Fewer words mean each word has a more powerful influence. Use commas, brackets, and hyphens to help organize your thoughts, but know the Midjourney Bot will not reliably interpret them. The Midjourney Bot does not consider capitalization.

## Use Collective Nouns

Plural words leave a lot to chance. Try specific numbers. "Three cats" is more specific than "cats." Collective nouns also work, “flock of birds” instead of "birds.”  Try 27-year-old woman rather than woman.

## Basic Parameters

Using an Apple device?
Many Apple devices automatically change double hyphens (--) to an em-dash (—). Midjourney accepts both!

Aspect Ratios
--aspect, or --ar Change the aspect ratio of a generation.

Chaos
--chaos <number 0–100> Change how varied the results will be. Higher values produce more unusual and unexpected generations.

Image Weight
--iw Sets image prompt weight relative to text weight. The default value is --iw 0.25.

No
--no Negative prompting, --no plants would try to remove plants from the image.

Quality
--quality <.25, .5, or 1>, or --q <.25, .5, or 1> How much rendering quality time you want to spend. The default value is 1. Higher values use more GPU minutes; lower values use less.

Repeat
--repeat <1–40>, or --r <1–40> Create multiple Jobs from a single prompt. --repeat is useful for quickly rerunning a job multiple times.

Seed
--seed <integer between 0–4294967295> The Midjourney bot uses a seed number to create a field of visual noise, like television static, as a starting point to generate the initial image grids. Seed numbers are generated randomly for each image but can be specified with the --seed or --sameseed parameter. Using the same seed number and prompt will produce similar ending images.

Stop
--stop <integer between 10–100> Use the --stop parameter to finish a Job partway through the process. Stopping a Job at an earlier percentage can create blurrier, less detailed results.

Style
--style <raw> Switch between versions of the Midjourney Model Version 5.1.
--style <4a, 4b, or 4c> Switch between versions of the Midjourney Model Version 4.
--style <cute, expressive, or scenic> Switch between versions of the Niji Model Version 5.

Stylize
--stylize <number>, or --s <number> parameter influences how strongly Midjourney's default aesthetic style is applied to Jobs.

Tile
--tile parameter generates images that can be used as repeating tiles to create seamless patterns.




