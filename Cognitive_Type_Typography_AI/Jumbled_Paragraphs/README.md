# Jumbled Paragraphs


Aoccdrnig to a rscheearer at Cmabrigde Uinervtisy, it deosn’t mttaer in waht oredr the ltteers in a wrod are, the olny iprmoetnt tihng is taht the frist and lsat ltteer be at the rghit pclae. The rset can be a toatl mses and you can sitll raed it wouthit porbelm. Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe.

Let's test this.

**jumble_paragraph.py**  

To create a Python script that processes a text file to generate a "Jumbled Paragraph" version as described, follow these steps:

1. **Add Spaces Around Punctuation**: Before jumbling the text, add an extra space before and after every punctuation mark. This step ensures that punctuation marks are not scrambled with the words.

2. **Jumble Words**: Scramble the middle letters of each word while keeping the first and last letters intact. This "Jumbled Paragraph" technique allows the text to remain somewhat readable because the human brain can still recognize the word based on the first and last letters and the overall shape of the word.

3. **Remove Extra Spaces Around Punctuation**: After jumbling the words, remove the extra spaces added around punctuation marks to restore the punctuation to its original form.

Below is a Python script that performs these steps. The script takes a text file from the command line, processes it to create a "Jumbled Paragraph", and then prints the result to the console.

```python
import sys
import random
import re

def scramble_word(word):
    if len(word) > 3:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]
    else:
        return word

def add_spaces_around_punctuation(text):
    return re.sub(r'([,.!?;:])', r' \1 ', text)

def remove_extra_spaces_around_punctuation(text):
    return re.sub(r'\s+([,.!?;:])\s+', r'\1', text)

def jumble_paragraph(text):
    text_with_spaces = add_spaces_around_punctuation(text)
    words = text_with_spaces.split()
    jumbled_words = [scramble_word(word) for word in words]
    jumbled_text = ' '.join(jumbled_words)
    return remove_extra_spaces_around_punctuation(jumbled_text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            text = file.read()
            jumbled_text = jumble_paragraph(text)
            print(jumbled_text)
    except FileNotFoundError:
        print(f"File {filename} not found.")
```

**How to Use the Script:**

- Save the script to a file, for example, `jumble_paragraph.py`.
- Make sure you have a text file ready, let's say it's named `input.txt`.
- Run the script from the command line by passing the text file as an argument:
  ```
  python jumble_paragraph.py input.txt
  ```
- The script will print the jumbled version of the paragraph to the console.

## RAPUNZEL REUPZNAL (Jumbled)


Tehre wree once a man and a woman who had lnog in vian wesihd for a
child.At lgetnh the waomn hpoed that God was aubot to gnrat her dierse .
These peploe had a lttile wiondw at the bcak of their house from which
a silpendd geadrn cuold be seen,which was flul of the msot buuiaetfl
frlewos and hrebs.It was,hvewoer,serdurnuod by a high wlal,and no
one dread to go itno it bescuae it beonelgd to an ehrensancts,who had
garet poewr and was deeardd by all the wrold.One day the wamon was
sntndiag by this woindw and lnkooig down itno the grdean,wehn she saw a
bed which was panteld wtih the msot buauetfil rpaiomn (parzenul),and it
loekod so fersh and green taht she lngeod for it,she quite penid away ,
and began to look plae and mrbesiale.Tehn her hnubsad was amerald,and
aksed:‘hWat ails you,daer wife?’ ‘Ah,’ she relpied,‘if I ca’nt eat
smoe of the ropiamn,wchih is in the gdaern bihned our house,I sahll
die.’ The man,who loved her,toughht:‘eSnoor tahn let yuor wfie die ,
bnirg her smoe of the rmipoan yrsuleof,let it csot waht it wlil.’
At twlighit,he clbmareed down oevr the wall itno the garedn of the
eecnnsahrts,hsialty cuhecltd a hdnaufl of rmpaion,and took it to his
wife.She at ocne mdae heserlf a salad of it,and ate it gelediry.It
tetsad so good to h--sreo vrey good,that the nxet day she leognd for it
terhe times as much as brofee.If he was to have any rest,her hsbnuad
must ocne mroe desencd into the gadern.In the golom of evinneg
tohrefree,he let hlmseif down agian;but wehn he had cbaelrmed dwon the
wall he was tbeirlry araifd,for he saw the ehsanrcnets siantdng befroe
him.‘How can you dare,’ said she with argny look,‘sdenecd itno my
graedn and saetl my rompian lkie a theif?You shall sffuer for it!’
‘Ah,’ awresned he,‘elt mrecy tkae the plcae of jiuctse,I only made
up my mind to do it out of nitsescey.My wife saw your riapomn form the
widonw,and flet such a logning for it that she wuold have deid if she
had not got smoe to eat.’ Then the ehctnrnseas awoelld her anegr to be
stfeeond,and said to him:‘If the case be as you say,I will aollw
you to tkae away with you as much roaimpn as you will,only I make one
cidinoton,you must gvie me the child wihch yuor wife will birng itno
the wolrd;it slhal be well tertead,and I wlil crae for it like a
mhteor.’ The man in his terorr cnoseetnd to enevhirtyg,and when the
wmaon was bouhgrt to bed,the erthnsceans aperpaed at once,gvae the
clihd the nmae of Ruzaenpl,and took it aawy wtih her .

Ranepuzl gerw into the most beufatiul child under the sun.When she was
telvwe yraes old,the etaehcnnsrs suht her itno a tewor,whcih lay in
a fsoret,and had neihetr sriats nor door,but qitue at the top was a
lttlie woindw.Wehn the etnercashns wentad to go in,she pceald hserelf
beatenh it and cried :

‘pneauRzl,Rnzaeupl ,
Let dwon your hair to me.’

Rpeanuzl had miifcagnent lnog hiar,fnie as supn gold,and when she
herad the vioce of the ehrascnents she unntseefad her braiedd treesss ,
wunod tehm round one of the hokos of the wodniw above,and then the hair
fell twenty ells down,and the esrtceannhs cbimeld up by it .

Aeftr a yaer or two,it came to pass that the kg’nis son rdoe trhgouh
the fsreot and pssead by the teowr.Then he heard a song,which was so
ciamnhrg taht he sootd still and lenitsed.Tihs was Rzapenul,who in her
sdilotue pssead her time in lnteitg her sewet vicoe reounsd.The ki’ngs
son wnaetd to cimlb up to her,and looekd for the door of the teowr ,
but nnoe was to be fnuod.He rode hmoe,but the sgiinng had so depely
tuheocd his haert,that ervey day he wnet out itno the ferost and
lietnsed to it.Ocne when he was thus sdtniang beihnd a tree,he saw
taht an enhrtcaenss came three,and he herad how she cired :

‘Rzeuapnl,Rauznpel ,
Let dwon your hiar to me.’

Tehn Raunzpel let dwon the bdrias of her hiar,and the ennsaechtrs
celmibd up to her.‘If that is the ldaedr by which one mtnous,I too
will try my frtunoe,’ said he,and the nxet day when it beagn to gorw
drak,he wnet to the tewor and ceird :

‘aRznpuel,Ranuzpel ,
Let down yuor hair to me.’

Imtemedaily the hiar fell down and the kngi’s son cmeilbd up .

At fsrit Rzaeunpl was tbirerly fhrnegeitd wehn a man,such as her eeys
had neevr yet belhed,came to her;but the kin’gs son began to tlak to
her qitue lkie a frenid,and tlod her taht his heart had been so srirted
taht it had let him hvae no rest,and he had been froecd to see her .
Then Rnauzpel lost her fear,and when he akesd her if she wloud take
him for her hnuabsd,and she saw that he was young and hmandose,she
tuhgoht:‘He will lvoe me more tahn old Dmae Gehotl dose’;and she siad
yes,and liad her hand in his.She siad:‘I wlil wllingily go aawy wtih
you,but I do not know how to get down.Birng with you a siken of silk
ervey tmie taht you come,and I will wevae a leaddr wtih it,and when
taht is radey I wlil dscneed,and you wlil take me on your hrsoe.’ Tehy
aeergd that unitl taht time he sohlud come to her eervy enienvg,for the
old wmaon cmae by day.The ehctasnrnes rekeamrd noihntg of this,until
once Ruanpezl said to her:‘elTl me,Dame Gtohel,how it hepapns taht
you are so mcuh haiveer for me to darw up than the ynoug kgin’s sh-no-e
is with me in a mnoemt.’ ‘Ah!you wikced cihld,’ ceird the etrshcannes .
‘What do I hear you say!I tuhgoht I had sreaptead you from all
the wlord,and yet you hvae deeicevd me!’ In her agenr she cuhcetld
Ralupne’zs buaitfuel tseerss,wrepapd them ticwe rnuod her left hand ,
szeied a pair of soscirss with the right,and sinp,snap,they were cut
off,and the lvoely biards lay on the gnurod.And she was so petlisis
taht she took poor Repunazl itno a dreset where she had to live in gaert
gerif and mrseiy .

On the smae day that she csat out Rzpeanul,hweevor,the escarntehns
feanestd the biards of hair,wichh she had cut off,to the hook of the
wndoiw,and wehn the kngi’s son came and creid :

‘aenzRpul,Renuazpl ,
Let down your hair to me.’

she let the hair dwon.The k’ngis son acedsend,but ieatsnd of fdnniig
his deserat Ranuzpel,he found the enrsancehts,who geazd at him with
wkceid and vouenmos looks.‘hAa!’ she cierd mlnigkcoy,‘oyu wulod fetch
yuor deraest,but the bfuaiuetl brid stis no logenr snginig in the nest ;
the cat has got it,and wlil strccah out yuor eyes as wlel.Ruazpnel is
lost to you;you will nveer see her aiagn.’ The kngi’s son was bsdiee
hlmsief wtih pian,and in his dsaiper he lapet dwon form the twoer.He
ecasepd with his life,but the tohnrs into wcihh he fell pieecrd his
eyes.Then he wrdaeend qtiue bnlid auobt the foesrt,ate nnthoig but
rtoos and berries,and did nghaut but lanemt and weep over the loss of
his deesart wife.Thus he rameod aobut in mrisey for smoe years,and at
lgenth cmae to the deesrt wehre Rpazenul,with the tiwns to which she
had given btirh,a boy and a girl,lievd in wsncerhtdees.He hraed a
vicoe,and it smeeed so faiimalr to him taht he went tordaws it,and
when he aoaercphpd,Reupaznl kenw him and flel on his ncek and wept.Two
of her traes wteetd his eeys and tehy gerw celar again,and he cuold
see with tehm as beorfe.He led her to his kigondm wrhee he was
joyflluy reeceivd,and tehy lievd for a lnog time awrrtfaeds,happy and
cttenoend .


## RAPUNZEL (Original)


There were once a man and a woman who had long in vain wished for a
child. At length the woman hoped that God was about to grant her desire.
These people had a little window at the back of their house from which
a splendid garden could be seen, which was full of the most beautiful
flowers and herbs. It was, however, surrounded by a high wall, and no
one dared to go into it because it belonged to an enchantress, who had
great power and was dreaded by all the world. One day the woman was
standing by this window and looking down into the garden, when she saw a
bed which was planted with the most beautiful rampion (rapunzel), and it
looked so fresh and green that she longed for it, she quite pined away,
and began to look pale and miserable. Then her husband was alarmed, and
asked: ‘What ails you, dear wife?’ ‘Ah,’ she replied, ‘if I can’t eat
some of the rampion, which is in the garden behind our house, I shall
die.’ The man, who loved her, thought: ‘Sooner than let your wife die,
bring her some of the rampion yourself, let it cost what it will.’
At twilight, he clambered down over the wall into the garden of the
enchantress, hastily clutched a handful of rampion, and took it to his
wife. She at once made herself a salad of it, and ate it greedily. It
tasted so good to her--so very good, that the next day she longed for it
three times as much as before. If he was to have any rest, her husband
must once more descend into the garden. In the gloom of evening
therefore, he let himself down again; but when he had clambered down the
wall he was terribly afraid, for he saw the enchantress standing before
him. ‘How can you dare,’ said she with angry look, ‘descend into my
garden and steal my rampion like a thief? You shall suffer for it!’
‘Ah,’ answered he, ‘let mercy take the place of justice, I only made
up my mind to do it out of necessity. My wife saw your rampion from the
window, and felt such a longing for it that she would have died if she
had not got some to eat.’ Then the enchantress allowed her anger to be
softened, and said to him: ‘If the case be as you say, I will allow
you to take away with you as much rampion as you will, only I make one
condition, you must give me the child which your wife will bring into
the world; it shall be well treated, and I will care for it like a
mother.’ The man in his terror consented to everything, and when the
woman was brought to bed, the enchantress appeared at once, gave the
child the name of Rapunzel, and took it away with her.

Rapunzel grew into the most beautiful child under the sun. When she was
twelve years old, the enchantress shut her into a tower, which lay in
a forest, and had neither stairs nor door, but quite at the top was a
little window. When the enchantress wanted to go in, she placed herself
beneath it and cried:

 ‘Rapunzel, Rapunzel,
  Let down your hair to me.’

Rapunzel had magnificent long hair, fine as spun gold, and when she
heard the voice of the enchantress she unfastened her braided tresses,
wound them round one of the hooks of the window above, and then the hair
fell twenty ells down, and the enchantress climbed up by it.

After a year or two, it came to pass that the king’s son rode through
the forest and passed by the tower. Then he heard a song, which was so
charming that he stood still and listened. This was Rapunzel, who in her
solitude passed her time in letting her sweet voice resound. The king’s
son wanted to climb up to her, and looked for the door of the tower,
but none was to be found. He rode home, but the singing had so deeply
touched his heart, that every day he went out into the forest and
listened to it. Once when he was thus standing behind a tree, he saw
that an enchantress came there, and he heard how she cried:

 ‘Rapunzel, Rapunzel,
  Let down your hair to me.’

Then Rapunzel let down the braids of her hair, and the enchantress
climbed up to her. ‘If that is the ladder by which one mounts, I too
will try my fortune,’ said he, and the next day when it began to grow
dark, he went to the tower and cried:

 ‘Rapunzel, Rapunzel,
  Let down your hair to me.’

Immediately the hair fell down and the king’s son climbed up.

At first Rapunzel was terribly frightened when a man, such as her eyes
had never yet beheld, came to her; but the king’s son began to talk to
her quite like a friend, and told her that his heart had been so stirred
that it had let him have no rest, and he had been forced to see her.
Then Rapunzel lost her fear, and when he asked her if she would take
him for her husband, and she saw that he was young and handsome, she
thought: ‘He will love me more than old Dame Gothel does’; and she said
yes, and laid her hand in his. She said: ‘I will willingly go away with
you, but I do not know how to get down. Bring with you a skein of silk
every time that you come, and I will weave a ladder with it, and when
that is ready I will descend, and you will take me on your horse.’ They
agreed that until that time he should come to her every evening, for the
old woman came by day. The enchantress remarked nothing of this, until
once Rapunzel said to her: ‘Tell me, Dame Gothel, how it happens that
you are so much heavier for me to draw up than the young king’s son--he
is with me in a moment.’ ‘Ah! you wicked child,’ cried the enchantress.
‘What do I hear you say! I thought I had separated you from all
the world, and yet you have deceived me!’ In her anger she clutched
Rapunzel’s beautiful tresses, wrapped them twice round her left hand,
seized a pair of scissors with the right, and snip, snap, they were cut
off, and the lovely braids lay on the ground. And she was so pitiless
that she took poor Rapunzel into a desert where she had to live in great
grief and misery.

On the same day that she cast out Rapunzel, however, the enchantress
fastened the braids of hair, which she had cut off, to the hook of the
window, and when the king’s son came and cried:

 ‘Rapunzel, Rapunzel,
  Let down your hair to me.’

she let the hair down. The king’s son ascended, but instead of finding
his dearest Rapunzel, he found the enchantress, who gazed at him with
wicked and venomous looks. ‘Aha!’ she cried mockingly, ‘you would fetch
your dearest, but the beautiful bird sits no longer singing in the nest;
the cat has got it, and will scratch out your eyes as well. Rapunzel is
lost to you; you will never see her again.’ The king’s son was beside
himself with pain, and in his despair he leapt down from the tower. He
escaped with his life, but the thorns into which he fell pierced his
eyes. Then he wandered quite blind about the forest, ate nothing but
roots and berries, and did naught but lament and weep over the loss of
his dearest wife. Thus he roamed about in misery for some years, and at
length came to the desert where Rapunzel, with the twins to which she
had given birth, a boy and a girl, lived in wretchedness. He heard a
voice, and it seemed so familiar to him that he went towards it, and
when he approached, Rapunzel knew him and fell on his neck and wept. Two
of her tears wetted his eyes and they grew clear again, and he could
see with them as before. He led her to his kingdom where he was
joyfully received, and they lived for a long time afterwards, happy and
contented.

