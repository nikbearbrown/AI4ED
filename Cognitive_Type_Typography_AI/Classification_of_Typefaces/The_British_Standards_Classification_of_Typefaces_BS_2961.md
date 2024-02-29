# CausalAI
Causal AI

## [Content](#content)

<table>
<tr><td colspan="2"><a href="#survey-papers">1. Surveys</a></td></tr> 
<tr>
<tr><td colspan="2"><a href="#individual-treatment-effects">2. Individual treatment effects</a></td></tr>
    <td>&emsp;<a href="#heterogeneous-treatment-effects">2.1. Heterogeneous treatment effects</a></td>
    <td>&emsp;<a href="#static-data">2.2. Static data</a></td>
</tr> 
<tr>
    <td>&emsp;<a href="#temporal-data">2.3. Temporal data</a></td>
</tr> 
<tr><td colspan="2"><a href="#representation-learning">3. Representation learning</a></td></tr>
<tr><td colspan="2"><a href="#semiparametric-inference">4. Semiparametric / double robust inference</a></td></tr>
<tr><td colspan="2"><a href="#policy-learning">5. Policy learning / causal discovery</a></td></tr>
<tr><td colspan="2"><a href="#causal-recommendation">6. Causal recommendation</a></td></tr>
<tr><td colspan="2"><a href="#causal-reinforcement-learning">7. Causal reinforcement learning</a></td></tr>
<tr><td colspan="2"><a href="#causal-reinforcement-learning">8. Feature selection in causal inference</a></td></tr>
<tr><td colspan="2"><a href="#applications">9. Applications</a></td></tr>
    <td>&emsp;<a href="#social-sciences">9.1. Social Sciences</a></td>
    <td>&ensp;<a href="#text">9.2. Text</a></td>
</tr> 
<tr>
    <td>&ensp;<a href="#health">9.3. Health</a></td>
</tr> 
<tr><td colspan="2"><a href="#resources">10. Resources</a></td></tr> 
    <td>&emsp;<a href="#workshops">10.1. Workshops</a></td>
    <td>&emsp;<a href="#proceedings">10.2. Proceedings</a></td>
</tr> 
<tr>
    <td>&ensp;<a href="#code-libraries">10.3. Code libraries</a></td>
    <td>&emsp;<a href="#benchmark-datasets">10.4. Benchmark datasets</a></td>
</tr> 
<tr>
    <td>&emsp;<a href="#courses">10.5. Courses</a></td>
    <td>&emsp;<a href="#industry">10.6. Industry</a></td>
</tr> 
<tr>
    <td>&emsp;<a href="#groups">10.7. Groups</a></td>
    <td>&emsp;<a href="#lists">10.8. Lists</a></td>
</tr> 
<tr>
    <td>&emsp;<a href="#books">10.9. Books</a></td>
</tr> 
</table>

## [Survey papers](#content)

1. **Causal Machine Learning: A Survey and Open Problems**, 2022. [paper](https://arxiv.org/abs/2206.15475)

    Jean Kaddour, Aengus Lynch, Qi Liu, Matt J. Kusner, Ricardo Silva.
	
1. **A Unified Survey of Heterogeneous Treatment Effect Estimation and Uplift Modeling**, *ACM Computing Surveys*, 2022. [paper](https://dl.acm.org/doi/abs/10.1145/3466818)

    Weijia Zhang, Jiuyong Li, Lin Liu.

1. **Toward Causal Representation Learning**, *IEEE*, 2021. [paper](https://ieeexplore.ieee.org/abstract/document/9363924)
    
    Bernhard Schölkopf, Francesco Locatello, Stefan Bauer, Nan Rosemary Ke, Nal Kalchbrenner, Anirudh Goyal, Yoshua Bengio.

1. **A Survey of Learning Causality with Data: Problems and Methods**, *ACM*, 2020. [paper](https://arxiv.org/abs/1809.09337)
    
    Ruocheng Guo, Lu Cheng, Jundong Li, P. Richard Hahn, Huan Liu.

1. **Machine learning and causal inference for policy evaluation**, *KDD*, 2015. [paper](https://dl.acm.org/citation.cfm?id=2785466)
    
    Susan Athey.

## [Individual treatment effects](#content) 

### [Heterogeneous treatment effects](#content)  

1. **Can Transformers be Strong Treatment Effect Estimators?**, *arxiv*, 2022. [paper](https://arxiv.org/abs/2202.01336) [code](https://github.com/hlzhang109/TransTEE)

    Yi-Fan Zhang, Hanlin Zhang, Zachary C. Lipton, Li Erran Li, Eric P. Xing.

1. **Nonparametric Estimation of Heterogeneous Treatment Effects: From Theory to Learning Algorithms**, *AISTATS*, 2021. [paper](https://proceedings.mlr.press/v130/curth21a.html)
    
    Alicia Curth, Mihaela van der Schaar.

1. **Causal Effect Inference for Structured Treatments**, *NeurIPS*, 2021. [paper](https://arxiv.org/abs/2106.01939) [code](https://github.com/JeanKaddour/SIN)
    
    Jean Kaddour, Yuchen Zhu, Qi Liu, Matt J. Kusner, Ricardo Silva.
	
1. **Treatment Effect Estimation with Disentangled Latent Factors**, *AAAI*, 2021. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/17304) [code](https://github.com/WeijiaZhang24/TEDVAE)
    
    Weijia Zhang, Lin Liu, Jiuyong Li.

1. **Generic Machine Learning Inference on Heterogenous Treatment Effects in Randomized Experiments**, *arXiv*, 2020. [paper](https://arxiv.org/abs/1712.04802)

    Victor Chernozhukov, Mert Demirer, Esther Duflo, Iván Fernández-Val.

1. **Quasi-Oracle Estimation of Heterogeneous Treatment Effects**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1712.04912)

    Xinkun Nie, Stefan Wager.

1. **Generalized Random Forests**, *Annals of Statistics*, 2019. [paper](https://arxiv.org/abs/1610.01271)

    Susan Athey, Julie Tibshirani, Stefan Wager.

1. **Machine Learning Estimation of Heterogeneous Treatment Effects with Instruments**, *NeurIPS*, 2019. [paper](https://arxiv.org/abs/1905.10176)
    
    Vasilis Syrgkanis, Victor Lei, Miruna Oprescu, Maggie Hei, Keith Battocchi, Greg Lewis.

1. **Orthogonal Random Forest for Causal Inference**, *PMLR*, 2019. [paper](http://proceedings.mlr.press/v97/oprescu19a.html)

    Miruna Oprescu, Vasilis Syrgkanis, Zhiwei Steven Wu.

1. **Meta-learners for Estimating Heterogeneous Treatment Effects using Machine Learning**, *PNAS*, 2019. [paper](https://arxiv.org/abs/1706.03461)

    Sören R. Künzel, Jasjeet S. Sekhon, Peter J. Bickel, Bin Yu.

1. **Machine Learning Analysis of Heterogeneity in the Effect of Student Mindset Interventions**, *Observational Studies*, 2019. [paper](https://arxiv.org/abs/1811.05975)
    
    Fredrik D. Johansson.

1. **Estimation and Inference of Heterogeneous Treatment Effects using Random Forests**, *JASA*, 2018. [paper](https://amstat.tandfonline.com/doi/full/10.1080/01621459.2017.1319839#.XaPLBeZKhhE)
    
    Stefan Wager, Susan Athey.

1. **Limits of Estimating Heterogeneous Treatment Effects: Guidelines for Practical Algorithm Design**, *PMLR*, 2018. [paper](http://proceedings.mlr.press/v80/alaa18a.html)
    
    Ahmed Alaa, Mihaela Schaar.

1. **Transfer Learning for Estimating Causal Effects using Neural Networks**, *arXiv*, 2018. [paper](https://arxiv.org/abs/1808.07804)

    Sören R. Künzel, Bradly C. Stadie, Nikita Vemuri, Varsha Ramakrishnan, Jasjeet S. Sekhon, Pieter Abbeel.

1. **Recursive partitioning for heterogeneous causal effects**, *PNAS*, 2016. [paper](https://www.pnas.org/content/113/27/7353)
    
    Susan Athey, Guido Imbens.

1. **Machine Learning Methods for Estimating Heterogeneous Causal Effects**, *ArXiv*, 2015. [paper](https://arxiv.org/abs/1504.01132v1)

    Susan Athey, Guido W. Imbens.


### [Static data](#content) 

1. **VCNet and Functional Targeted Regularization For Learning Causal Effects of Continuous Treatments**, *ICLR*, 2021. [paper](https://arxiv.org/abs/2103.07861)  [code](https://github.com/lushleaf/varying-coefficient-net-with-functional-tr)

    Lizhen Nie, Mao Ye, Qiang Liu, Dan Nicolae.

1. **Learning Counterfactual Representations for Estimating Individual Dose-Response Curves**, *AAAI*, 2020. [paper](https://arxiv.org/abs/1902.00981) [code](https://github.com/d909b/drnet)

    Patrick Schwab, Lorenz Linhardt, Stefan Bauer, Joachim M. Buhmann, Walter Karlen.

1. **Estimating the Effects of Continuous-valued Interventions using Generative Adversarial Networks**, *NeurIPS*, 2020. [paper](https://arxiv.org/abs/2002.12326) [code](https://github.com/ioanabica/SCIGAN)

    Ioana Bica, James Jordon, Mihaela van der Schaar.

1. **Learning Individual Causal Effects from Networked Observational Data**, *WSDM*, 2020. [paper](https://arxiv.org/abs/1906.03485) [code](https://github.com/rguo12/network-deconfounder-wsdm20)

    Ruocheng Guo, Jundong Li, Huan Liu.

1. **Learning Overlapping Representations for the Estimation of Individualized Treatment Effects**, *AISTATS*, 2020. [paper](https://arxiv.org/abs/2001.04754)

    Yao Zhang, Alexis Bellot, Mihaela van der Schaar.

1. **Adapting Neural Networks for the Estimation of Treatment Effects**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1906.02120) [code](http://github.com/claudiashi57/dragonnet)
    
    Claudia Shi, David M. Blei, Victor Veitch.

1. **Program Evaluation and Causal Inference with High-Dimensional Data**, *arXiv*, 2018. [paper](https://arxiv.org/abs/1311.2645)
    
    Alexandre Belloni, Victor Chernozhukov, Ivan Fernández-Val, Christian Hansen.    

1. **GANITE: Estimation of Individualized Treatment Effects using Generative Adversarial Nets**, *ICLR*, 2018. [paper](https://openreview.net/pdf?id=ByKWUeWA-) [code](https://github.com/jsyoon0823/GANITE)
    
    Jinsung Yoon, James Jordon, Mihaela van der Schaar.

1. **Estimation of Individual Treatment Effect in Latent Confounder Models via Adversarial Learning**, *arXiv*, 2018. [paper](https://arxiv.org/abs/1811.08943)
    
    Changhee Lee, Nicholas Mastronarde, Mihaela van der Schaar.

1. **Deep IV: A Flexible Approach for Counterfactual Prediction**, *PMLR*, 2017. [paper](http://proceedings.mlr.press/v70/hartford17a.html)
    
    Uri Shalit, Fredrik D. Johansson, David Sontag.

1. **Causal Effect Inference with Deep Latent-Variable Models**, *arXiv*, 2017. [paper](https://arxiv.org/abs/1705.08821) [code](https://github.com/AMLab-Amsterdam/CEVAE)
    
    Christos Louizos, Uri Shalit, Joris Mooij, David Sontag, Richard Zemel, Max Welling.

1. **Estimating individual treatment effect: generalization bounds and algorithms**, *PMLR*, 2017. [paper](http://proceedings.mlr.press/v70/shalit17a.html) [code](https://github.com/clinicalml/cfrnet)
    
    Uri Shalit, Fredrik D. Johansson, David Sontag.

### [Temporal data](#content) 

1. **Time Series Deconfounder: Estimating Treatment Effects over Time in the Presence of Hidden Confounders**, *ICML*, 2020. [paper](https://arxiv.org/abs/1902.00450) [code](https://github.com/ioanabica/Time-Series-Deconfounder)

    Ioana Bica, Ahmed M. Alaa, Mihaela van der Schaar.

1. **Estimating Counterfactual Treatment Outcomes over Time through Adversarially Balanced Representations**, *ICLR*, 2020. [paper](https://openreview.net/pdf?id=BJg866NFvB) [code](https://github.com/ioanabica/Counterfactual-Recurrent-Network)

    Ioana Bica, Ahmed M. Alaa, James Jordon, Mihaela van der Schaar.

1. **Generative Learning of Counterfactual for Synthetic Control Applications in Econometrics**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1910.07178)
    
    Chirag Modi, Uros Seljak.

1. **Robust Synthetic Control**, *JMLR*, 2019. [paper](http://www.jmlr.org/papers/volume19/17-777.pdf)
    
    Muhammad Amjad, Devavrat Shah, Dennis Shen.

1. **ArCo: An artificial counterfactual approach for high-dimensional panel time-series data**, *Journal of Econometrics*, 2018. [paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2823687)
    
    Carlos Carvalho, Ricardo Masini, Marcelo C. Medeiros.

1. **Forecasting Treatment Responses Over Time Using Recurrent Marginal Structural Networks**, *NIPS*, 2018. [paper](https://papers.nips.cc/paper/7977-forecasting-treatment-responses-over-time-using-recurrent-marginal-structural-networks) [code](https://github.com/sjblim/rmsn_nips_2018)
    
    Sonali Parbhoo, Stefan Bauer, Patrick Schwab.

## [Representation learning](#content)   

1. **Deep Structural Causal Models for Tractable Counterfactual Inference**, *NeurIPS*, 2020. [paper](https://arxiv.org/abs/2006.06485) [code](https://github.com/biomedia-mira/deepscm)

    Nick Pawlowski, Daniel C. Castro, Ben Glocker.

1. **NCoRE: Neural Counterfactual Representation Learning for Combinations of Treatments**, *arXiv*, 2021. [paper](https://arxiv.org/abs/2103.11175)
    
    Sonali Parbhoo, Stefan Bauer, Patrick Schwab.

1. **Perfect Match: A Simple Method for Learning Representations For Counterfactual Inference With Neural Networks**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1810.00656) [code](https://github.com/d909b/perfect_match)
    
    Patrick Schwab, Lorenz Linhardt, Walter Karlen.

1. **Representation Learning for Treatment Effect Estimation from Observational Data**, *NeurIPS*, 2019. [paper](https://papers.nips.cc/paper/7529-representation-learning-for-treatment-effect-estimation-from-observational-data.pdf) 
    
    Liuyi Yao et al.

1. **Invariant Models for Causal Transfer Learning**, *JMLR*, 2018. [paper](http://jmlr.org/papers/v19/16-432.html) 
    
    Mateo Rojas-Carulla, Bernhard Schölkopf, Richard Turner, Jonas Peters.

1. **Learning Representations for Counterfactual Inference**, *arXiv*, 2018. [paper](https://arxiv.org/abs/1605.03661) [code](https://github.com/clinicalml/cfrnet)
    
    Fredrik D. Johansson, Uri Shalit, David Sontag.

## [Semiparametric / double robust inference](#content)  

1. **Sparsity Double Robust Inference of Average Treatment Effects**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1905.00744)
    
    Jelena Bradic, Stefan Wager, Yinchu Zhu.

1. **Deep Neural Networks for Estimation and Inference**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1809.09953)
    
    Max H. Farrell, Tengyuan Liang, Sanjog Misra.

1. **Deep Counterfactual Networks with Propensity-Dropout**, *arXiv*, 2017. [paper](https://arxiv.org/abs/1706.05966)
    
    Ahmed M. Alaa, Michael Weisz, Mihaela van der Schaar.

1. **Double/Debiased Machine Learning for Treatment and Causal Parameters**, *arXiv*, 2017. [paper](https://arxiv.org/abs/1608.00060)
    
    Victor Chernozhukov, Denis Chetverikov, Mert Demirer, Esther Duflo, Christian Hansen, Whitney Newey, James Robins.

1. **Doubly Robust Policy Evaluation and Optimization**, *Statistical Science*, 2014. [paper](https://arxiv.org/abs/1503.02834)
    
    Miroslav Dudík, Dumitru Erhan, John Langford, Lihong Li.

## [Policy learning / causal discovery](#content)  

1. **Differentiable Causal Discovery Under Unmeasured Confounding**, *arXiv*, 2021. [paper](https://arxiv.org/abs/2010.06978)
    
    Rohit Bhattacharya, Tushar Nagarajan, Daniel Malinsky, Ilya Shpitser.

1. **Causal Discovery with Attention-Based Convolutional Neural Networks**, *Machine Learning and Knowledge Extraction*, 2019. [paper](https://www.mdpi.com/2504-4990/1/1/19) [code](https://github.com/M-Nauta/TCDF)
    
    Meike Nauta, Doina Bucur, Christin Seifert.

1. **A Meta-Transfer Objective for Learning to Disentangle Causal Mechanisms**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1901.10912)
    
    Yoshua Bengio, Tristan Deleu, Nasim Rahaman, Rosemary Ke, Sébastien Lachapelle, Olexa Bilaniuk, Anirudh Goyal, Christopher Pal.

1. **Causal Discovery with Reinforcement Learning**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1906.04477)
    
    Shengyu Zhu, Zhitang Chen.

1. **CausalGAN: Learning Causal Implicit Generative Models with Adversarial Training**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1709.02023)
    
    Murat Kocaoglu, Christopher Snyder, Alexandros G. Dimakis, Sriram Vishwanath.

1. **Learning When-to-Treat Policies**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1905.09751)
    
    Xinkun Nie, Emma Brunskill, Stefan Wager.

1. **Learning Neural Causal Models from Unknown Interventions**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1910.01075) [code](https://github.com/nke001/causal_learning_unknown_interventions)
    
    Nan Rosemary Ke, Olexa Bilaniuk, Anirudh Goyal, Stefan Bauer, Hugo Larochelle, Chris Pal, Yoshua Bengio.

1. **Counterfactual Policy Optimization Using Domain-Adversarial Neural Networks**, *ICML*, 2018. [paper](http://medianetlab.ee.ucla.edu/papers/cf_treat_v5)
    
    Onur Atan, William R. Zame, Mihaela van der Schaar.

1. **Causal Bandits: Learning Good Interventions via Causal Inference**, *NIPS*, 2016. [paper](https://papers.nips.cc/paper/6195-causal-bandits-learning-good-interventions-via-causal-inference)
    
    Finnian Lattimore, Tor Lattimore, Mark D. Reid.

1. **Counterfactual Risk Minimization: Learning from Logged Bandit Feedback**, *arXiv*, 2015. [paper](https://arxiv.org/abs/1502.02362)
    
    Adith Swaminathan, Thorsten Joachims.

## [Causal recommendation](#content) 

1. **The Deconfounded Recommender: A Causal Inference Approach to Recommendation**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1808.06581) [code](https://github.com/blei-lab/deconfounder_tutorial)
    
    Yixin Wang, Dawen Liang, Laurent Charlin, David M. Blei. 

1. **The Blessings of Multiple Causes**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1805.06826)
    
    Yixin Wang, David M. Blei. 

<details><summary> comments </summary> 

3. **Comment: Reflections on the Deconfounder**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1910.08042)

    Alexander D'Amour

1. **On Multi-Cause Causal Inference with Unobserved Confounding: Counterexamples, Impossibility, and Alternatives**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1902.10286)

    Alexander D'Amour

1. **Comment on "Blessings of Multiple Causes"**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1910.05438)
    
    Elizabeth L. Ogburn, Ilya Shpitser, Eric J. Tchetgen Tchetgen.

1. **The Blessings of Multiple Causes: A Reply to Ogburn et al. (2019)**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1910.07320)
    
    Yixin Wang, David M. Blei.

</details>

7. **Recommendations as Treatments: Debiasing Learning and Evaluation**, *PMLR*, 2016. [paper](http://proceedings.mlr.press/v48/schnabel16.html)
    
    Tobias Schnabel, Adith Swaminathan, Ashudeep Singh, Navin Chandak, Thorsten Joachims.

1. **Collaborative Prediction and Ranking with Non-Random Missing Data**, *RecSys*, 2009. [paper](http://www.cs.toronto.edu/~zemel/documents/acmrec2009-MarlinZemel.pdf)
    
    Benjamin M. Marlin, Richard S. Zemel.

## [Causal reinforcement learning](#content) 

1. **Counterfactual Multi-Agent Policy Gradients**, *AAAI*, 2018. [paper](https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/17193)
    
    Jakob N. Foerster, Gregory Farquhar, Triantafyllos Afouras, Nantas Nardelli, Shimon Whiteson. 

## [Feature Selection in causal inference](#content)

1. **Ultra-high dimensional variable selection for doubly robust causal inference**, *Biometrics*, 2022. [paper](https://arxiv.org/abs/2007.14190) [code](https://github.com/dingketang/ultra-high-DRCI) [slides](https://drive.google.com/file/d/1OlwNi9eMu_MQe3TyiHpHg2ULdfGD2x0S/view?usp=sharing)

    Dingke Tang, Dehan Kong, Wenliang Pan, Linbo Wang

1. **Outcome‐adaptive lasso: variable selection for causal inference**, *Biometrics* 2017. [paper](https://onlinelibrary.wiley.com/doi/pdf/10.1111/biom.12679?casa_token=_xFuHHhoWlAAAAAA:gKO0JyJC0g54pOfbOVlNew7t1M29UD_A46yJJUAGiLAuxO87p4lGmMneYklKfuWGiHCitIbvKtjfEMAN)  [video](https://crossminds.ai/video/variable-selection-for-causal-inference-outcome-adaptive-lasso-6070a5f9fa08279acdb2124a/)

    Susan M. Shortreed, Ashkan Ertefaie

## [Applications](#content)

### [Social sciences](#content)

1. **Double machine learning-based programme evaluation under unconfoundedness**, *The Econometrics Journal*, 2022. [paper](https://doi.org/10.1093/ectj/utac015)
    
    Michael C Knaus.

1. **State-Building through Public Land Disposal? An Application of Matrix Completion for Counterfactual Prediction**, *arXiv*, 2021. [paper](https://arxiv.org/abs/1903.08028) [code](https://github.com/jvpoulos/homesteads)
    
    Jason Poulos.

1. **RNN-based counterfactual prediction, with an application to homestead policy and public schooling**, *JRSS-C*, 2021. [paper](http://jasonvpoulos.com/papers/17117351.pdf) [code](https://github.com/jvpoulos/rnns-causal)
    
    Jason Poulos, Shuxi Zeng.

1. **Estimating Treatment Effects with Causal Forests: An Application**, *arXiv*, 2019. [paper](https://arxiv.org/abs/1902.07409)
    
    Susan Athey, Stefan Wager.

1. **Ensemble Methods for Causal Effects in Panel Data Settings**, *AER P&P*, 2019. [paper](https://arxiv.org/abs/1903.10079)
    
    Susan Athey, Mohsen Bayati, Guido W. Imbens, Zhaonan Qu.

### [Text](#content)

1. **Counterfactual Data Augmentation for Neural Machine Translation**, *ACL*, 2021. [paper](https://www.aclweb.org/anthology/2021.naacl-main.18/) [code](https://github.com/xxxiaol/GCI)
    
     Qi Liu, Matt Kusner, Phil Blunsom.

1. **Everything Has a Cause: Leveraging Causal Inference in Legal Text Analysis**, *arXIv*, 2021. [paper](https://arxiv.org/abs/2104.09420) [code](https://github.com/xxxiaol/GCI)
    
     Xiao Liu, Da Yin, Yansong Feng, Yuting Wu, Dongyan Zhao.

1. **Causal Effects of Linguistic Properties**, *arXIv*, 2021. [paper](https://arxiv.org/abs/2010.12919)
    
     Reid Pryzant, Dallas Card, Dan Jurafsky, Victor Veitch, Dhanya Sridhar.

1. **Sketch and Customize: A Counterfactual Story Generator**, *arXIv*, 2021. [paper](https://arxiv.org/abs/2104.00929)
    
    Changying Hao, Liang Pang, Yanyan Lan, Yan Wang, Jiafeng Guo, Xueqi Cheng.

1. **Counterfactual Generator: A Weakly-Supervised Method for Named Entity Recognition**, *EMNLP*, 2020. [paper](https://github.com/xijiz/cfgen/blob/master/docs/cfgen.pdf) [code](https://github.com/xijiz/cfgen)
    
    Xiangji Zeng, Yunliang Li, Yuchen Zhai, Yin Zhang.

1. **Using Text Embeddings for Causal Inference**, *arXIv*, 2019. [paper](https://arxiv.org/abs/1905.12741) [code](https://github.com/blei-lab/causal-text-embeddings)
    
    Victor Veitch, Dhanya Sridhar, David M. Blei.

1. **Counterfactual Story Reasoning and Generation**, *arXIv*, 2019. [paper](https://arxiv.org/abs/1909.04076)
    
    Lianhui Qin, Antoine Bosselut, Ari Holtzman, Chandra Bhagavatula, Elizabeth Clark, Yejin Choi.

1. **How to Make Causal Inferences Using Texts**, *arXIv*, 2018. [paper](https://arxiv.org/abs/1802.02163)

    Naoki Egami, Christian J. Fong, Justin Grimmer, Margaret E. Roberts, Brandon M. Stewart.

### [Health](#content)

1. **Targeted learning in observational studies with multi-level treatments: An evaluation of antipsychotic drug treatment safety for patients with serious mental illnesses**, *arXIv*, 2022. [paper](https://arxiv.org/abs/2206.15367) [code](https://github.com/jvpoulos/multi-tmle)
    
     Jason Poulos, Marcela Horvitz-Lennon, Katya Zelevinsky, Thomas Huijskens, Pooja Tyagi, Jiaju Yan, Jordi Diaz, Tudor Cristea-Platon, Sharon-Lise Normand.

## [Resources](#content)

### [Workshops](#content)

1. **NeurIPS 2021 Workshop** [link](https://why21.causalai.net/)

1. **UAI 2021 Workshop** [link](https://sites.google.com/uw.edu/causaluai2021/home?authuser=0)

1. **KDD 2021 Workshop** [link](https://bcirwis2021.github.io/cfp.html)

1. **ICML 2021 Workshop** [link](https://sites.google.com/view/naci2021/home)

1. **EMNLP 2021 Workshop** [link](https://causaltext.github.io/2021/)

1. **NeurIPS 2020 Workshop** [link](https://www.cmu.edu/dietrich/causality/neurips20ws/)

1. **NeurIPS 2019 Workshop** [link](http://tripods.cis.cornell.edu/neurips19_causalml/)

1. **NIPS 2018 Workshop** [link](https://sites.google.com/view/nips2018causallearning/home)

1. **NIPS 2017 Workshop** [link](https://sites.google.com/view/causalnips2017)

1. **NIPS 2016 Workshop** [link](https://sites.google.com/site/whatif2016nips/)

1. **NIPS 2013 Workshop** [link](http://clopinet.com/isabelle/Projects/NIPS2013/)

### [Proceedings](#content)

1. **PMLR, Volume 6: Causality: Objectives and Assessment, 12 December 2008, Whistler, Canada** [link](http://proceedings.mlr.press/v6/)

### [Code libraries](#content)

1. **Causal Inference 360: A Python package for inferring causal effects from observational data.** [link](https://github.com/IBM/causallib)

1. **WhyNot: A Python package connecting tools from causal inference and reinforcement learning with a range of complex simulators** [link](https://github.com/zykls/whynot)

1. **EconML: A Python Package for ML-Based Heterogeneous Treatment Effects Estimation** [link](https://github.com/microsoft/EconML)

1. **Uplift modeling and causal inference with machine learning algorithms** [link](https://github.com/uber/causalml)

### [Benchmark datasets](#content)

1. **IHDP, Jobs, and News benchmarks** [link](https://fredjo.com/)

1. **Twins** [link](http://www.nber.org/data/linked-birth-infant-death-data-vitalstatistics-data.htm)

1. **Causality workbench** [link](http://www.causality.inf.ethz.ch/repository.php?page=data)

### [Courses](#content)

1. **CS7792 - Counterfactual Machine Learning** [link](http://www.cs.cornell.edu/courses/cs7792/2016fa/)

1. **Introduction to Causal Inference** [link](https://www.bradyneal.com/causal-inference-course)

1. **Machine Learning & Causal Inference: A Short Course** [link](https://www.youtube.com/playlist?list=PLxq_lXOUlvQAoWZEqhRqHNezS30lI49G-)

1. **KDD 2020: Lecture Style Tutorials: Casual Inference Meets Machine Learning** [link](https://www.youtube.com/watch?v=DbW2e2q8Gjs)

### [Industry](#content)

1. **Causality and Machine Learning: Microsoft Research** [link](https://www.microsoft.com/en-us/research/group/causal-inference/#!publications)

### [Groups](#content)

1. **Society for Causal Inference** [link](https://sci-info.org/)

1. **Research Laboratory led by Prof. Mihaela van der Schaar** [link](http://www.vanderschaar-lab.com/NewWebsite/causal_inference_and_treatment_effects.html)

### [Lists](#content)

1. **An index of algorithms for learning causality with data** [link](https://github.com/rguo12/awesome-causality-algorithms)

1. **An index of datasets that can be used for learning causality** [link](https://github.com/rguo12/awesome-causality-data)

1. **Papers about Causal Inference and Language** [link](https://github.com/causaltext/causal-text-papers)

### [Books](#content)

1. **Causal Machine Learning** [link](https://www.manning.com/books/causal-machine-learning)


# awesome-causality-algorithms [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
An index of algorithms in
- machine learning for causal inference: solves causal inference problems
- causal machine learning: solves ML problems
**Reproducibility is important!** We will remove those methods without open-source code unless it is a survey/review paper.
Please cite [our survey paper](https://arxiv.org/pdf/1809.09337) if this index is helpful.
```
@article{guo2020survey,
  title={A survey of learning causality with data: Problems and methods},
  author={Guo, Ruocheng and Cheng, Lu and Li, Jundong and Hahn, P Richard and Liu, Huan},
  journal={ACM Computing Surveys (CSUR)},
  volume={53},
  number={4},
  pages={1--37},
  year={2020},
  publisher={ACM New York, NY, USA}
```
# Table of Contents
- [Toolboxes](#toolboxes)
- [Causal Effect Estimation](#causal-effect-estimation)
- [Causal Machine Learning](#causal-machine-learning)
## Toolboxes
### Comprehensive
|Name|Code|Comment|
|---|---|---|
|Trustworthy AI|[Python](https://github.com/huawei-noah/trustworthyAI)|Causal Structure Learning, Causal Disentangled Representation Learning, gCastle (or pyCastle, pCastle).|
|[YLearn](https://ylearn.readthedocs.io/en/latest/)|[Python](https://github.com/DataCanvasIO/YLearn)|Python package for causal discovery，causal effect identification/estimation, counterfactual inference，policy learning，etc.|
### Treatment Effect Estimation / Uplift Modeling
|Name|Paper/Documentation|Venue|Code|Comment|
|---|---|---|---|---|
|DoWhy|[Tutorial on Causal Inference and Counterfactual Reasoning](http://causalinference.gitlab.io/kdd-tutorial/)|KDD 2018|[Python](https://github.com/microsoft/dowhy)|Python library for causal inference that supports explicit modeling and testing of causal assumptions.|
|EconML|[Causal Inference and Machine Learning in Practice with EconML and CausalML](https://causal-machine-learning.github.io/kdd2021-tutorial/)|KDD 2021|[Python](https://econml.azurewebsites.net/spec/spec.html)|Python package that applies the power of machine learning techniques to estimate individualized causal responses from observational or experimental data.|
|CausalML|[Causalml: Python package for causal machine learning](https://arxiv.org/pdf/2002.11631.pdf)|arxiv|[Python](https://github.com/uber/causalml)|Uplift modeling and causal inference with machine learning algorithms|
|JustCause|[Underlying thesis](https://justcause.readthedocs.io/en/latest/_downloads/e054f7a0fc9cf9e680173600cb4b4350/thesis-mfranz.pdf)|NA|[Python](https://github.com/inovex/justcause)|For evaluation of heterogeneous treatment effect estimators on common reference as well as synthetic data.|
|WhyNot|[Documentation](https://whynot.readthedocs.io/en/latest/)|NA|[Python](https://github.com/zykls/whynot)|An experimental sandbox for causal inference and decision making in dynamics.|
|scikit-uplift|[Documentation](https://www.uplift-modeling.com/en/latest/index.html) and [User guide for uplift modeling](https://www.uplift-modeling.com/en/latest/user_guide/index.html)|NA|[Python](https://github.com/maks-sh/scikit-uplift)|Uplift modeling in scikit-learn style in python. |
### Causal Discovery
|Name|Paper|Code|Comment|
|---|---|---|---|
|[Bench Press](https://benchpressdocs.readthedocs.io/en/latest/)|[Benchpress: a scalable and versatile workflow for benchmarking structure learning algorithms for graphical models](https://arxiv.org/abs/2107.03863)|[Code](https://github.com/felixleopoldo/benchpress)|Reproducible and scalable execution and benchmarks of **41** structure learning algorithms supporting multiple language|
|[causal-learn](https://causal-learn.readthedocs.io/en/latest/)|NA|[Python](https://github.com/cmu-phil/causal-learn)|Causal Discovery for Python. A translation and extension of TETRAD.|
|[TETRAD R/Java](http://www.phil.cmu.edu/tetrad/about.html)|[TETRAD-A Toolbox FOR CAUSAL DISCOVERY](https://www.atmos.colostate.edu/~iebert/PAPERS/CI2018_paper_35.pdf)|[R](https://github.com/bd2kccd/r-causal)/[Java](https://github.com/cmu-phil/tetrad)|Causal Discovery Toolbox from CMU|
|Causaldag|NA|[code](https://github.com/uhlerlab/causaldag)|Python package for the creation, manipulation, and learning of Causal DAGs|
|CausalNex|NA|[Python](https://github.com/quantumblacklabs/causalnex)|A toolkit for causal reasoning with Bayesian Networks.|
|CausalDiscoveryToolbox|[Causal Discovery Toolbox: Uncover causal relationships in Python](https://arxiv.org/pdf/1903.02278)|[Python](https://github.com/Diviyan-Kalainathan/CausalDiscoveryToolbox)||
### Rootcause Analysis
|Name|Paper|Code|Comments|
|---|---|---|---|
|[Chaos Genius](https://www.chaosgenius.io/)|NA|[Python](https://github.com/chaos-genius/chaos_genius/)|ML powered analytics engine for outlier/anomaly detection and root cause analysis.|
## Causal Effect Estimation
#### Survey Papers
|Name|Paper|Venue|
|---|---|---|
||[A survey on causal inference](https://arxiv.org/abs/2002.02770)|TKDD|
### With i.i.d Data
#### Individual Treatment Effect (ITE) / Conditional Average Treatment Effect (CATE)
##### Deep Learning based methods
|Name|Paper|Venue|Code|
|---|---|---|---|
|TARNet, Counterfactual Regression|[Estimating individual treatment effect: generalization bounds and algorithms](https://arxiv.org/pdf/1606.03976)|ICML 2017|[Python](https://github.com/oddrose/cfrnet)|
|BNN, BLR|[Learning representations for counterfactual inference](http://www.jmlr.org/proceedings/papers/v48/johansson16.pdf)|ICML 2016|[Python](https://github.com/oddrose/cfrnet)|
|Causal Effect VAE|[Causal effect inference with deep latent-variable models](http://papers.nips.cc/paper/7223-causal-effect-inference-with-deep-latent-variable-models.pdf)|Neurips 2017|[Python](https://github.com/AMLab-Amsterdam/CEVAE)|
|Dragonnet|[Adapting neural networks for the estimation of treatment effects.](https://arxiv.org/abs/1906.02120)|Neurips 2019|[Python](https://github.com/claudiashi57/dragonnet)|
|SITE|[Representation Learning for Treatment Effect Estimation from Observational Data](https://papers.nips.cc/paper/7529-representation-learning-for-treatment-effect-estimation-from-observational-data.pdf)|Neurips 2018|[Python](https://github.com/Osier-Yi/SITE)|
|GANITE|[GANITE: Estimation of Individualized Treatment Effects using Generative Adversarial Nets](https://openreview.net/forum?id=ByKWUeWA-)|ICLR 2018|[Python](https://github.com/jsyoon0823/GANITE)|
|Perfect Match|[Perfect match: A simple method for learning representations for counterfactual inference with neural networks](https://arxiv.org/pdf/1810.00656)|arxiv|[Python](https://github.com/d909b/perfect_match)|
|Intact-VAE|Intact-VAE: Estimating treatment effects under unobserved confounding|ICLR 2022|[code](https://openreview.net/forum?id=q7n2RngwOM)|
|CausalEGM|[CausalEGM: a general causal inference framework by encoding generative modeling](https://arxiv.org/abs/2212.05925)|arxiv|[Python](https://github.com/SUwonglab/CausalEGM)|
<!-- |BNR-NNM(balanced and nonlinear representations-nearest neighbor matching)|[Li, Sheng, and Yun Fu. "Matching on balanced nonlinear representations for treatment effects estimation." In Advances in Neural Information Processing Systems, pp. 929-939. 2017.](http://papers.nips.cc/paper/6694-matching-on-balanced-nonlinear-representations-for-treatment-effects-estimation.pdf)|NA| -->
<!-- |Deep Counterfactual Networks (Propensity Dropout)|[Alaa, Ahmed M., Michael Weisz, and Mihaela van der Schaar. "Deep counterfactual networks with propensity-dropout." arXiv preprint arXiv:1706.05966 (2017)](https://arxiv.org/pdf/1706.05966)|NA| -->
##### Classic Methods
|Name|Paper|Code|
|---|---|---|
|Propensity Score Matching|[Rosenbaum, Paul R., and Donald B. Rubin. "The central role of the propensity score in observational studies for causal effects." Biometrika 70, no. 1 (1983): 41-55.](https://academic.oup.com/biomet/article-pdf/70/1/41/662954/70-1-41.pdf)|[Python](https://github.com/akelleh/causality/tree/master/causality/estimation)|
<!-- |Nonparametric Regression Adjustment|   |[Python](https://github.com/akelleh/causality)|
 -->
##### Tree based Methods
|Name|Paper|Code|
|---|---|---|
|Causal Forest|[Wager, Stefan, and Susan Athey. "Estimation and inference of heterogeneous treatment effects using random forests." JASA (2017).](https://www.tandfonline.com/doi/pdf/10.1080/01621459.2017.1319839)|[code R](https://github.com/grf-labs/grf), [code Python](https://github.com/kjung/scikit-learn)|
|Causal MARS, Causal Boosting, Pollinated Transformed Outcome Forests|[S. Powers et al., “Some methods for heterogeneous treatment effect estimation in high-dimensions,” 2017.](https://arxiv.org/pdf/1707.00102.pdf)|[code R](https://github.com/grf-labs/grf), [code R](https://github.com/saberpowers/causalLearning)|
|Bayesian Additive Regression Trees (BART)|[Hill, Jennifer L. "Bayesian nonparametric modeling for causal inference." Journal of Computational and Graphical Statistics 20, no. 1 (2011): 217-240.](https://www.tandfonline.com/doi/pdf/10.1198/jcgs.2010.08162)|[Python](https://github.com/JakeColtman/bartpy)|
<!-- |Active Learning for Decision-Making from Imbalanced Observational Data|[Active Learning for Decision-Making from Imbalanced Observational Data](https://arxiv.org/abs/1904.05268)|NA| -->
<!-- |ABCEI|[Adversarial Balancing-based Representation Learning for Causal Effect Inference with Observational Data](https://arxiv.org/pdf/1904.13335.pdf)|NA| -->
<!-- |NSGP (Non-stationary Gaussian Process Prior)|[Alaa, Ahmed, and Mihaela Schaar. "Limits of estimating heterogeneous treatment effects: Guidelines for practical algorithm design." In International Conference on Machine Learning, pp. 129-138. 2018.](http://proceedings.mlr.press/v80/alaa18a/alaa18a.pdf)|NA| -->
<!-- |CMGP (Causal Multi-task Gaussian Processes)|[Alaa, Ahmed M., and Mihaela van der Schaar. "Bayesian inference of individualized treatment effects using multi-task gaussian processes." In Advances in Neural Information Processing Systems, pp. 3424-3432. 2017.](https://papers.nips.cc/paper/6934-bayesian-inference-of-individualized-treatment-effects-using-multi-task-gaussian-processes.pdf)|NA| -->
<!-- |Functional Interval Estimator|[Kallus, Nathan, Xiaojie Mao, and Angela Zhou. "Interval Estimation of Individual-Level Causal Effects Under Unobserved Confounding." In The 22nd International Conference on Artificial Intelligence and Statistics, pp. 2281-2290. 2019.](https://arxiv.org/abs/1810.02894)|NA| -->
##### Meta Learner
|Name|Paper|Code|
|---|---|---|
|X-learner|[Künzel, Sören R., Jasjeet S. Sekhon, Peter J. Bickel, and Bin Yu. "Metalearners for estimating heterogeneous treatment effects using machine learning." Proceedings of the National Academy of Sciences 116, no. 10 (2019): 4156-4165.](https://www.pnas.org/content/pnas/early/2019/02/14/1804597116.full.pdf)|[code R](https://github.com/soerenkuenzel/hte), [code R](https://github.com/xnie/rlearner/blob/master/R/xlearner.R)|
#### Average Treatment Effect (including ATT and ATC)
|Name|Paper|Code|
|---|---|---|
|Inverse Probability Reweighting|[Rosenbaum, Paul R., and Donald B. Rubin. "The central role of the propensity score in observational studies for causal effects." Biometrika 70, no. 1 (1983): 41-55.](https://academic.oup.com/biomet/article-pdf/70/1/41/662954/70-1-41.pdf)|[R](https://github.com/cran/ipw)|
|Doubly Robust Estimation|[Bang, Heejung, and James M. Robins. "Doubly robust estimation in missing data and causal inference models." Biometrics 61, no. 4 (2005): 962-973.](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1541-0420.2005.00377.x)|[R](https://github.com/gregridgeway/fastDR)|
|Doubly Robust Estimation for High Dimensional Data|[Antonelli, Joseph, Matthew Cefalu, Nathan Palmer, and Denis Agniel. "Doubly robust matching estimators for high dimensional confounding adjustment." Biometrics (2016).](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6347556/)|[R](https://github.com/jantonelli111/DoublyRobustHD)|
|TMLE|[Gruber, Susan, and Mark J. van der Laan. "tmle: An R package for targeted maximum likelihood estimation." (2011).](https://www.jstatsoft.org/article/view/v051i13)|[R](https://cran.r-project.org/web/packages/tmle/index.html)|
|Entropy Balancing|[Hainmueller, Jens. "Entropy balancing for causal effects: A multivariate reweighting method to produce balanced samples in observational studies." Political Analysis 20, no. 1 (2012): 25-46.](https://www.jstor.org/stable/pdf/41403737.pdf)|[R](https://github.com/cran/ebal)|
|CBPS(Covariate Balancing Propensity Score)|[Imai, Kosuke, and Marc Ratkovic. "Covariate balancing propensity score." Journal of the Royal Statistical Society: Series B (Statistical Methodology) 76, no. 1 (2014): 243-263.](https://rss.onlinelibrary.wiley.com/doi/full/10.1111/rssb.12027)|[R](https://github.com/kosukeimai/CBPS)|
|Approximate Residual Balancing|[Athey, Susan, Guido W. Imbens, and Stefan Wager. "Approximate residual balancing: debiased inference of average treatment effects in high dimensions." Journal of the Royal Statistical Society: Series B (Statistical Methodology) 80, no. 4 (2018): 597-623.](https://rss.onlinelibrary.wiley.com/doi/pdf/10.1111/rssb.12268)|[R](https://github.com/swager/balanceHD)|
|Causal Bootstrapping|Little, Max A., and Reham Badawy. "Causal bootstrapping." arXiv preprint arXiv:1910.09648 (2019).|[Matlab](http://www.maxlittle.net/software/cblib.zip)|
<!-- |Differentiated Confounder Balancing|[Kuang, Kun, Peng Cui, Bo Li, Meng Jiang, and Shiqiang Yang. "Estimating Treatment Effect in the Wild via Differentiated Confounder Balancing." In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 265-274. ACM, 2017.](http://media.cs.tsinghua.edu.cn/~multimedia/cuipeng/papers/CausalDCA.pdf)|NA| -->
<!-- |Adversarial Balancing|[Ozery-Flato, Michal, Pierre Thodoroff, and Tal El-Hay. "Adversarial Balancing for Causal Inference." arXiv preprint arXiv:1810.07406 (2018).](https://arxiv.org/pdf/1810.07406)|NA| -->
<!-- |DeepMatch|[Kallus, Nathan. "Deepmatch: Balancing deep covariate representations for causal inference using adversarial training." arXiv preprint arXiv:1802.05664 (2018).](https://arxiv.org/pdf/1802.05664)|NA| -->
#### Instrumental Variable (IV)
|Name|Paper|Code|
|---|---|---|
|DeepIV|[Hartford, Jason, Greg Lewis, Kevin Leyton-Brown, and Matt Taddy. "Deep iv: A flexible approach for counterfactual prediction." In International Conference on Machine Learning, pp. 1414-1423. 2017.](http://proceedings.mlr.press/v70/hartford17a/hartford17a.pdf)|[Python](https://github.com/jhartford/DeepIV)|
|PDSLasso|[Achim Ahrens & Christian B. Hansen & Mark E Schaffer, 2018. "PDSLASSO: Stata module for post-selection and post-regularization OLS or IV estimation and inference," Statistical Software Components S458459, Boston College Department of Economics, revised 24 Jan 2019.](https://ideas.repec.org/c/boc/bocode/s458459.html)|[STATA](https://statalasso.github.io/)|
#### Does-Response Curve (Continuous Treatment)
|Name|Paper|Code|
|---|---|---|
|Causal Dose-Response Curves / Causal Curves|[Kobrosly, R. W., (2020). causal-curve: A Python Causal Inference Package to Estimate Causal Dose-Response Curves. Journal of Open Source Software, 5(52), 2523, https://doi.org/10.21105/joss.02523](https://joss.theoj.org/papers/10.21105/joss.02523)|[Python](https://github.com/ronikobrosly/causal-curve)|
|Dose response networks (DRNets)|[Schwab, Patrick, Lorenz Linhardt, Stefan Bauer, Joachim M. Buhmann, and Walter Karlen. "Learning Counterfactual Representations for Estimating Individual Dose-Response Curves." arXiv preprint arXiv:1902.00981 (2019).](https://arxiv.org/pdf/1902.00981.pdf)|[Python](https://github.com/d909b/drnet)|
#### Vectorized Treatments
|Name|Paper|Code|
|---|---|---|
|Causal Effect Inference for Structured Treatments|[Jean Kaddour, Qi Liu, Yuchen Zhu, Matt J. Kusner, Ricardo Silva. "Causal Effect Inference for Structured Treatments", In NeurIPS 2021.](https://arxiv.org/pdf/2106.01939.pdf)|[Python](https://github.com/JeanKaddour/SIN)|
<!-- #### Treatment Responder Classification
|Name|Paper|Code|
|---|---|---| -->
<!-- |RespSVM|[Kallus, Nathan. "Classifying Treatment Responders Under Causal Effect Monotonicity." arXiv preprint arXiv:1902.05482 (2019)](https://arxiv.org/pdf/1902.05482.pdf)|NA| -->
#### Multiple Causes
|Name|Paper|Code|
|---|---|---|
|Deconfounder|[Wang, Yixin, and David M. Blei. "The blessings of multiple causes." arXiv preprint arXiv:1805.06826 (2018).](https://arxiv.org/abs/1805.06826)|[Python](https://github.com/blei-lab/deconfounder_tutorial)|
<!-- ||[Imai, Kosuke, and Zhichao Jiang. "Discussion of "The Blessings of Multiple Causes" by Wang and Blei."](https://imai.fas.harvard.edu/research/files/deconfounder.pdf)|NA|
||[D'Amour, Alexander. "On multi-cause causal inference with unobserved confounding: Counterexamples, impossibility, and alternatives." arXiv preprint arXiv:1902.10286 (2019).](https://arxiv.org/abs/1902.10286)|NA|
||[Ranganath, Rajesh, and Adler Perotte. "Multiple causal inference with latent confounding." arXiv preprint arXiv:1805.08273 (2018).](https://arxiv.org/pdf/1805.08273)|NA|
||[Kong, Dehan, Shu Yang, and Linbo Wang. "Multi-cause causal inference with unmeasured confounding and binary outcome." arXiv preprint arXiv:1907.13323 (2019).](https://arxiv.org/pdf/1907.13323.pdf)|NA|
||[Elizabeth L. Ogburn, Ilya Shpitser, Eric J. Tchetgen Tchetgen "Comment on Blessings of Multiple Causes." arXiv preprint arXiv:1910.05438 (2019)](https://arxiv.org/abs/1910.05438v2?from=timeline)|NA| -->
#### Multiple Outcomes
|Name|Paper|Code|
|---|---|---|
|Multiple Responses in Uplift Models|[Weiss, Sam. Estimating and Visualizing Business Tradeoffs in Uplift Models](https://medium.com/building-ibotta/estimating-and-visualizing-business-tradeoffs-in-uplift-models-80ff845a5698) |[Python](https://github.com/Ibotta/mr_uplift)|
<!-- #### Transfer Learning for Causal Effect Estimation
|Name|Paper|Code|
|---|---|---|
|The Y-learner|[Künzel, Sören R., Bradly C. Stadie, Nikita Vemuri, Varsha Ramakrishnan, Jasjeet S. Sekhon, and Pieter Abbeel. "Transfer Learning for Estimating Causal Effects using Neural Networks." arXiv preprint arXiv:1808.07804 (2018).](https://arxiv.org/pdf/1808.07804.pdf)|NA| -->
<!-- #### Variable Selection/Importance for Learning Causal Effects
|Name|Paper|Code|
|---|---|---|
|Variable importance through targeted causal inference|[The Github Repo "varimpact" by Alan E. Hubbard and Chris J. Kennedy, University of California, Berkeley](https://github.com/ck37/varimpact)|[R](https://github.com/ck37/varimpact)| -->
### Non-i.i.d Data
#### Panel Data / Time Series
|Name|Paper|Code|
|---|---|---|
|Synthetic Control Method|[Abadie, Alberto. "Using synthetic controls: Feasibility, data requirements, and methodological aspects." Journal of Economic Literature 59.2 (2021): 391-425.](https://www.aeaweb.org/articles?id=10.1257/jel.20191450)|[R](https://cran.r-project.org/web/packages/Synth/Synth.pdf)|
|Synthetic Difference in Differences|[Arkhangelsky, Dmitry, et al. Synthetic difference in differences. No. w25532. National Bureau of Economic Research, 2019.](https://www.nber.org/system/files/working_papers/w25532/w25532.pdf)|[R](https://github.com/synth-inference/synthdid)<br>[Python](https://github.com/MasaAsami/pysynthdid)|
|Causal Impact|[Brodersen, K. H., Gallusser, F., Koehler, J., Remy, N., & Scott, S. L. (2015). Inferring causal impact using Bayesian structural time-series models. The Annals of Applied Statistics, 9(1), 247–274. doi: 10.1214/14-AOAS788](https://projecteuclid.org/journals/annals-of-applied-statistics/volume-9/issue-1/Inferring-causal-impact-using-Bayesian-structural-time-series-models/10.1214/14-AOAS788.full)|[R](https://github.com/cran/bsts)<br>[Python](https://github.com/WillianFuks/tfcausalimpact)|
|Time Series Deconfounder|[Bica, Ioana, Ahmed M. Alaa, and Mihaela van der Schaar. "Time Series Deconfounder: Estimating Treatment Effects over Time in the Presence of Hidden Confounders." In ICML 2020.](https://arxiv.org/pdf/1902.00450.pdf)|[code](https://github.com/ioanabica/Time-Series-Deconfounder)|
|Recurrent Marginal Structural Networks|[Lim, Bryan. "Forecasting Treatment Responses Over Time Using Recurrent Marginal Structural Networks." In Advances in Neural Information Processing Systems, pp. 7494-7504. 2018.](http://medianetlab.ee.ucla.edu/papers/nips_rmsn.pdf)|[Python](https://github.com/sjblim/rmsn_nips_2018)|
|Longitudinal Targeted Maximum Likelihood Estimation|[Petersen, Maya, Joshua Schwab, Susan Gruber, Nello Blaser, Michael Schomaker, and Mark van der Laan. "Targeted maximum likelihood estimation for dynamic and static longitudinal marginal structural working models." Journal of causal inference 2, no. 2 (2014): 147-185.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4405134/)|[R](https://github.com/joshuaschwab/ltmle)|
|Causal Transformer|[Melnychuk, Valentyn, Dennis Frauen, and Stefan Feuerriegel. "Causal Transformer for Estimating Counterfactual Outcomes." arXiv preprint arXiv:2204.07258 (2022).](https://arxiv.org/abs/2204.07258)|[Python](https://github.com/Valentyn1997/CausalTransformer)|
#### Network Data (with or without Interference)
|Name|Paper|Code|
|---|---|---|
|Network Deconfounder|[Guo, Ruocheng, Jundong Li, and Huan Liu. "Learning Individual Causal Effects from Networked Observational Data." WSDM 2020.](https://arxiv.org/abs/1906.03485)|[Python](https://github.com/rguo12/network-deconfounder-wsdm20)|
|Causal Inference with Network Embeddings|[Veitch, Victor, Yixin Wang, and David M. Blei. "Using embeddings to correct for unobserved confounding." arXiv preprint arXiv:1902.04114 (2019).](https://arxiv.org/pdf/1902.04114)|[Python](https://github.com/vveitch/causal-network-embeddings)|
|Linked Causal Variational Autoencoder (LCVA)|[Rakesh, Vineeth, Ruocheng Guo, Raha Moraffah, Nitin Agarwal, and Huan Liu. "Linked Causal Variational Autoencoder for Inferring Paired Spillover Effects." CIKM 2018.](http://www.public.asu.edu/~rguo12/CIKM18.pdf)|[Python](https://github.com/rguo12/CIKM18-LCVA)|
|Method-of-moments Estimators|[Li, Wenrui, Daniel L. Sussman, and Eric D. Kolaczyk. "Causal Inference under Network Interference with Noise." arXiv preprint arXiv:2105.04518 (2021).](https://arxiv.org/abs/2105.04518)|[code](https://github.com/KolaczykResearch/CausInfNoisyNet)|
<!-- |GNN-based Causal Effect Estimators|[Ma, Yunpu, Yuyi Wang, and Volker Tresp. "Causal Inference under Networked Interference." arXiv preprint arXiv:2002.08506 (2020).](https://arxiv.org/pdf/2002.08506.pdf)|NA| -->
## Causal Machine Learning
### Surveys
|Name|Paper|Code|
|---|---|---|
|CausalML|[Jean Kaddour, Aengus Lynch, Qi Liu, Matt J. Kusner, Ricardo Silva. "Causal Machine Learning: A Survey and Open Problems" arXiv preprint arXiv:2206.15475 (2022)](https://arxiv.org/abs/2206.15475).|NA|
### OoD Generalization
|Name|Paper|Code|
|---|---|---|
|DomainBed|Gulrajani, Ishaan, and David Lopez-Paz. "In Search of Lost Domain Generalization." In International Conference on Learning Representations. 2020.|[code](https://github.com/facebookresearch/DomainBed)|
|WILDS|Koh, Pang Wei, Shiori Sagawa, Henrik Marklund, Sang Michael Xie, Marvin Zhang, Akshay Balsubramani, Weihua Hu et al. "Wilds: A benchmark of in-the-wild distribution shifts." In International Conference on Machine Learning, pp. 5637-5664. PMLR, 2021.|[code](https://github.com/p-lambda/wilds)|
|IBM OoD|Repository for theory and methods for Out-of-Distribution (OoD) generalization by IBM Research|[code](https://github.com/IBM/OoD)|
|OoD Bench|Ye, Nanyang, Kaican Li, Lanqing Hong, Haoyue Bai, Yiting Chen, Fengwei Zhou, and Zhenguo Li. "Ood-bench: Benchmarking and understanding out-of-distribution generalization datasets and algorithms." arXiv preprint arXiv:2106.03721 (2021).|[code](https://github.com/m-Just/OoD-Bench)|
|BEDS-Bench|Avati, Anand, Martin Seneviratne, Emily Xue, Zhen Xu, Balaji Lakshminarayanan, and Andrew M. Dai. "BEDS-Bench: Behavior of EHR-models under Distributional Shift--A Benchmark." arXiv preprint arXiv:2107.08189 (2021).|[code](https://github.com/Google-Health/records-research/tree/master/beds-bench)|
|Survey THU|Shen, Zheyan, Jiashuo Liu, Yue He, Xingxuan Zhang, Renzhe Xu, Han Yu, and Peng Cui. "Towards out-of-distribution generalization: A survey." arXiv preprint arXiv:2108.13624 (2021).|NA|
#### Graph OoD Generalization
|Name|Paper|Code|
|---|---|---|
|CIGA|Chen, Yongqiang, Yonggang Zhang, Yatao Bian, Han Yang, Kaili Ma, Binghui Xie, Tongliang Liu, Bo Han, and James Cheng. "Learning Causally Invariant Representations for Out-of-Distribution Generalization on Graphs." In Advances in Neural Information Processing Systems (2022).|[code](https://github.com/LFhase/CIGA)|
|Survey THU|Li, Haoyang, Xin Wang, Ziwei Zhang, and Wenwu Zhu. "Out-of-distribution generalization on graphs: A survey." arXiv preprint arXiv:2202.07987 (2022).|NA|
### Recommendation Systems
#### Inverse Propensity Scoring / Doubly Robust
|Name|Paper|Code|
|---|---|---|
|Top-K Off-policy Correction|[Chen, Minmin, Alex Beutel, Paul Covington, Sagar Jain, Francois Belletti, and Ed H. Chi. "Top-k off-policy correction for a REINFORCE recommender system." In Proceedings of the Twelfth ACM International Conference on Web Search and Data Mining, pp. 456-464. ACM, 2019.](https://arxiv.org/abs/1812.02353)|[Python](https://github.com/awarebayes/RecNN)|
|Unbiased Offline Recommender Learning|[Saito, Yuta, Suguru Yaginuma, Yuta Nishino, Hayato Sakata, and Kazuhide Nakata. "Unbiased Recommender Learning from Missing-Not-At-Random Implicit Feedback." In Proceedings of the 13th International Conference on Web Search and Data Mining, pp. 501-509. ACM, 2020.](https://dl.acm.org/doi/abs/10.1145/3336191.3371783)|[Python](https://github.com/usaito/unbiased-implicit-rec-real)|
|Unbiased Offline Recommender Evaluation|[Yang, Longqi, Yin Cui, Yuan Xuan, Chenyang Wang, Serge Belongie, and Deborah Estrin. "Unbiased offline recommender evaluation for missing-not-at-random implicit feedback." In Proceedings of the 12th ACM Conference on Recommender Systems, pp. 279-287. ACM, 2018.](https://dl.acm.org/citation.cfm?id=3240355)|[Python](https://github.com/ylongqi/unbiased-offline-recommender-evaluation)|
|IPS Estimator|[Schnabel, Tobias, Adith Swaminathan, Ashudeep Singh, Navin Chandak, and Thorsten Joachims. "Recommendations as treatments: Debiasing learning and evaluation." arXiv preprint arXiv:1602.05352 (2016).](http://www.jmlr.org/proceedings/papers/v48/schnabel16.pdf)|[Python](http://www.cs.cornell.edu/~schnabts/mnar/index.html)|
<!-- |Doubly Robust Joint Learning|[Wang, Xiaojie, Rui Zhang, Yu Sun, and Jianzhong Qi. "Doubly Robust Joint Learning for Recommendation on Data Missing Not at Random." In International Conference on Machine Learning, pp. 6638-6647. 2019.](http://proceedings.mlr.press/v97/wang19n.html)|NA| -->
#### Hidden Confounding
|Name|Paper|Code|
|---|---|---|
|Deconfounded Recsys|[Wang, Yixin, Dawen Liang, Laurent Charlin, and David M. Blei. "Causal Inference for Recommender Systems." In Proceedings of the Fourteenth ACM Conference on Recommender Systems (2020).](https://dl.acm.org/doi/10.1145/3383313.3412225)|[Python](https://github.com/yixinwang/causal-recsys-public)|
#### Domain Adaptation
|Name|Paper|Code|
|---|---|---|
|Causal Embedding for Recommendation|[Bonner, Stephen, and Flavian Vasile. "Causal embeddings for recommendation." In Proceedings of the 12th ACM Conference on Recommender Systems, pp. 104-112. ACM, 2018. (**BEST PAPER**)](https://arxiv.org/pdf/1706.07639)|[Python](https://github.com/criteo-research/CausE)|
|Domain Adversarial Matrix Factorization|[Saito, Yuta, and Masahiro Nomura. "Towards Resolving Propensity Contradiction in Offline Recommender Learning." In IJCAI 2022](https://usaito.github.io/files/IJCAI2022_DAMF.pdf)|[code](https://github.com/usaito/ijcai2022-adversarial-mf)|
#### Disentanglement
|Name|Paper|Code|
|---|---|---|
|Causal Embedding for User Interest and Conformity|[Zheng, Y., Gao, C., Li, X., He, X., Li, Y., & Jin, D. (2021, April). Disentangling User Interest and Conformity for Recommendation with Causal Embedding. In Proceedings of the Web Conference 2021 (pp. 2980-2991).](https://arxiv.org/abs/2006.11011)|[Python](https://github.com/tsinghua-fib-lab/DICE)|
### Learning to Rank
|Name|Paper|Code|
|---|---|---|
|Policy-aware Estimator|[Oosterhuis, Harrie, and Maarten de Rijke. "Policy-aware unbiased learning to rank for top-k rankings." In Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval, pp. 489-498. 2020.](https://arxiv.org/pdf/2005.09035.pdf)|[Python](https://github.com/HarrieO/2020topkunbiasedltr)|
|Heckman^{rank}|[Ovaisi, Zohreh, Ragib Ahsan, Yifan Zhang, Kathryn Vasilaky, and Elena Zheleva. "Correcting for Selection Bias in Learning-to-rank Systems." arXiv preprint arXiv:2001.11358 (2020).](https://arxiv.org/abs/2001.11358)|[code](https://github.com/edgeslab/heckman_rank)|
|Unbiased LambdaMart|[Hu, Ziniu, Yang Wang, Qu Peng, and Hang Li. "Unbiased LambdaMART: An Unbiased Pairwise Learning-to-Rank Algorithm." In The World Wide Web Conference, pp. 2830-2836. ACM, 2019.](https://acbull.github.io/pdf/unbias.pdf)|[code](https://github.com/acbull/Unbiased_LambdaMart)|
|IPW_rank and the Dual Learning Algorithm|[Qingyao Ai, Keping Bi, Cheng Luo, Jiafeng Guo, W. Bruce Croft. 2018. Unbiased Learning to Rank with Unbiased Propensity Estimation. In Proceedings of SIGIR '18](https://arxiv.org/abs/1804.05938)|[Python](https://github.com/QingyaoAi/Unbiased-Learning-to-Rank-with-Unbiased-Propensity-Estimation)|
|Propensity SVM-rank|[Joachims, Thorsten, Adith Swaminathan, and Tobias Schnabel. "Unbiased learning-to-rank with biased feedback." In Proceedings of the Tenth ACM International Conference on Web Search and Data Mining, pp. 781-789. ACM, 2017. (**BEST PAPER**)](https://dl.acm.org/ft_gateway.cfm?id=3018699&type=pdf)|[Python](http://www.cs.cornell.edu/people/tj/svm_light/svm_proprank.html)|
<!-- |Regression EM|[Wang, Xuanhui, Nadav Golbandi, Michael Bendersky, Donald Metzler, and Marc Najork. "Position bias estimation for unbiased learning to rank in personal search." In Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining, pp. 610-618. ACM, 2018.](https://pub-tools-public-publication-data.storage.googleapis.com/pdf/3bace79f9bcead0b20dec31e2a0878346ad2fb0d.pdf)|NA| -->
<!-- |Various Bias Models|[Wang, Xuanhui, Michael Bendersky, Donald Metzler, and Marc Najork. "Learning to rank with selection bias in personal search." In Proceedings of the 39th International ACM SIGIR conference on Research and Development in Information Retrieval, pp. 115-124. ACM, 2016.](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45286.pdf)|NA| -->
<!-- |TrustPBM| [Agarwal, Aman, Xuanhui Wang, Cheng Li, Mike Bendersky, and Marc Najork. "Addressing Trust Bias for Unbiased Learning-to-Rank." In The World Wide Web Conference, pp. 4-14. ACM, 2019.](https://research.google/pubs/pub47859/) |NA| -->
<!-- |Intervention Harvesting|[Agarwal, Aman, Ivan Zaitsev, Xuanhui Wang, Cheng Li, Marc Najork, and Thorsten Joachims. "Estimating Position Bias without Intrusive Interventions." In Proceedings of the Twelfth ACM International Conference on Web Search and Data Mining, pp. 474-482. ACM, 2019.](https://dl.acm.org/doi/10.1145/3289600.3291017)|NA| -->
### Off-line Policy Evaluation/Optimization (for Contextual Bandit or RL)
|Name|Paper|Code|
|---|---|---|
|Optimal Kernel Balancing|[Andrew Bennett, Nathan Kallus. "Policy Evaluation with Latent Confounders via Optimal Balance"](http://arxiv.org/abs/1908.01920)|[Python](https://github.com/CausalML/LatentConfounderBalancing)|
|BanditNet|[Joachims, Thorsten, Adith Swaminathan, and Maarten de Rijke. "Deep learning with logged bandit feedback." (2018).](https://openreview.net/pdf?id=SJaP_-xAb)|[Python](https://www.cs.cornell.edu/people/tj/banditnet/index.html)|
|Counterfactual Risk Minimization (POEM)|[Swaminathan, Adith, and Thorsten Joachims. "Counterfactual risk minimization: Learning from logged bandit feedback." In International Conference on Machine Learning, pp. 814-823. 2015.](http://www.jmlr.org/proceedings/papers/v37/swaminathan15.pdf)|[Python](http://www.cs.cornell.edu/~adith/POEM/index.html)|
|Self Normalized Estimator|[Swaminathan, Adith, and Thorsten Joachims. "The self-normalized estimator for counterfactual learning." In Advances in Neural Information Processing Systems, pp. 3231-3239. 2015.](http://papers.nips.cc/paper/5748-the-self-normalized-estimator-for-counterfactual-learning.pdf)|[Python](http://www.cs.cornell.edu/~adith/POEM/index.html)|
<!-- |Surrogate Policy|[Xie, Yuan, Boyi Liu, Qiang Liu, Zhaoran Wang, Yuan Zhou, and Jian Peng. "Off-Policy Evaluation and Learning from Logged Bandit Feedback: Error Reduction via Surrogate Policy." arXiv preprint arXiv:1808.00232 (2018).](https://arxiv.org/abs/1808.00232)|NA| -->
<!-- |Balanced Policy Evaluation and Learning|[Kallus, Nathan. "Balanced policy evaluation and learning." In Advances in Neural Information Processing Systems, pp. 8895-8906. 2018.](http://papers.nips.cc/paper/8105-balanced-policy-evaluation-and-learning.pdf)|NA| -->
<!-- |Confounding-robust Policy Learning|[Kallus, Nathan, and Angela Zhou. "Confounding-robust policy improvement." In Advances in Neural Information Processing Systems, pp. 9269-9279. 2018.](http://papers.nips.cc/paper/8105-balanced-policy-evaluation-and-learning)|NA| -->
<!-- |Multi-action Policy Learning|[Zhou, Zhengyuan, Susan Athey, and Stefan Wager. "Offline multi-action policy learning: Generalization and optimization." arXiv preprint arXiv:1810.04778 (2018).](https://arxiv.org/abs/1810.04778)|NA| -->
<!-- |Efficient Policy Learning|[Athey, Susan, and Stefan Wager. "Efficient policy learning." arXiv preprint arXiv:1702.02896 (2017).](https://arxiv.org/abs/1702.02896)|NA| -->
<!-- |Focused Context Balancing|[Zou, Hao, Kun Kuang, Boqi Chen, Peixuan Chen, and Peng Cui. "Focused Context Balancing for Robust Offline Policy Evaluation." In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, pp. 696-704. ACM, 2019.](http://delivery.acm.org/10.1145/3340000/3330852/p696-zou.pdf?ip=209.147.139.170&id=3330852&acc=ACTIVE%20SERVICE&key=B63ACEF81C6334F5%2EBD7B0059B564CDBA%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1568671555_f79e8c0ff7c1b351ed2bbc13191485ef)|NA| -->
### Natural Language Processing
|Name|Paper|Code|
|---|---|---|
|A Review of Using Text to Remove Confounding from Causal Estimates|[Keith, Katherine A., David Jensen, and Brendan O'Connor. "Text and Causal Inference: A Review of Using Text to Remove Confounding from Causal Estimates." ACL 2020.](https://www.aclweb.org/anthology/2020.acl-main.474.pdf)|NA|
|Causal Analysis with Lexicons|[Pryzant, Reid, Kelly Shen, Dan Jurafsky, and Stefan Wagner. "Deconfounded lexicon induction for interpretable social science." NAACL 2018.](https://www.aclweb.org/anthology/N18-1146.pdf)|[Python](https://github.com/rpryzant/causal_attribution)|
|Causal Text Embeddings|[Veitch, Victor, Dhanya Sridhar, and David M. Blei. "Using Text Embeddings for Causal Inference." arXiv preprint arXiv:1905.12741 (2019).](https://arxiv.org/pdf/1905.12741.pdf)|[Python](https://github.com/blei-lab/causal-text-embeddings)|
|Handling Missing/Noisy Treatment|[Wood-Doughty, Zach, Ilya Shpitser, and Mark Dredze. "Challenges of Using Text Classifiers for Causal Inference." In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, pp. 4586-4598. 2018.](https://aclweb.org/anthology/D18-1488)|[Python](https://github.com/zachwooddoughty/emnlp2018-causal)|
|Causal Inferences Using Texts|[Egami, Naoki, Christian J. Fong, Justin Grimmer, Margaret E. Roberts, and Brandon M. Stewart. "How to make causal inferences using texts." arXiv preprint arXiv:1802.02163 (2018).](https://arxiv.org/pdf/1802.02163.pdf)|NA|
<!-- |Causal FS for text classification|[Michael J. Paul. Feature selection as causal inference: experiments with text classification. Conference on Computational Natural Language Learning (CoNLL), Vancouver, Canada. August 2017.](https://www.aclweb.org/anthology/K/K17/K17-1018.pdf)|NA| -->
<!-- |Conditional Treatment-adversarial Learning Based Matching|[Yao, Liuyi, Sheng Li, Yaliang Li, Hongfei Xue, Jing Gao, and Aidong Zhang. "On the estimation of treatment effect with text covariates." In Proceedings of the 28th International Joint Conference on Artificial Intelligence, pp. 4106-4113. AAAI Press, 2019.](https://pdfs.semanticscholar.org/2e2f/39232771711248940f68c3c1d6bd0a22c3e4.pdf)|NA| -->
### Counterfactual Explanations
|Paper|Code|
|---|---|
|[Mothilal, Ramaravind Kommiya, Amit Sharma, and Chenhao Tan. "Explaining machine learning classifiers through diverse counterfactual explanations." arXiv preprint arXiv:1905.07697 (2019).](https://arxiv.org/pdf/1905.07697.pdf)|[Python](https://github.com/microsoft/DiCE)|
|[Russell, Chris. "Efficient search for diverse coherent explanations." In Proceedings of the Conference on Fairness, Accountability, and Transparency, pp. 20-28. 2019.](https://dl.acm.org/doi/pdf/10.1145/3287560.3287569)|[Python](https://bitbucket.org/ChrisRussell/diverse-coherent-explanations/)|
|[Wachter, Sandra, Brent Mittelstadt, and Chris Russell. "Counterfactual explanations without opening the black box: Automated decisions and the GDPR." Harv. JL & Tech. 31 (2017): 841.](https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/hjlt31&section=29)||
### Counterfactual Fairness
|Paper|Code|
|---|---|
|[Kusner, Matt J., Joshua Loftus, Chris Russell, and Ricardo Silva. "Counterfactual fairness." In Advances in Neural Information Processing Systems, pp. 4066-4076. 2017.](http://papers.nips.cc/paper/6995-counterfactual-fairness.pdf)|[Python](https://github.com/mkusner/counterfactual-fairness)|
|[Wu, Yongkai, Lu Zhang, Xintao Wu, and Hanghang Tong. "Pc-fairness: A unified framework for measuring causality-based fairness." Advances in Neural Information Processing Systems 32 (2019).](https://proceedings.neurips.cc/paper/2019/file/44a2e0804995faf8d2e3b084a1e2db1d-Paper.pdf)|[code](https://github.com/yongkaiwu/Path-specific-Counterfactual-Fairness)|
|[Chiappa, Silvia. "Path-specific counterfactual fairness." In Proceedings of the AAAI Conference on Artificial Intelligence, vol. 33, pp. 7801-7808. 2019.](https://www.aaai.org/ojs/index.php/AAAI/article/download/4777/4655)|[code](https://www.deepmind.com/open-source/path-specific-counterfactual-fairness-in-jax)|
|[Garg, Sahaj, Vincent Perot, Nicole Limtiaco, Ankur Taly, Ed H. Chi, and Alex Beutel. "Counterfactual fairness in text classification through robustness." In Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and Society, pp. 219-226. 2019.](https://dl.acm.org/doi/pdf/10.1145/3306618.3317950)|[code](https://github.com/SaiSakethAluru/Counterfactual-fairness)|
<!-- |[Russell, Chris, Matt J. Kusner, Joshua Loftus, and Ricardo Silva. "When worlds collide: integrating different counterfactual assumptions in fairness." In Advances in Neural Information Processing Systems, pp. 6414-6423. 2017.](http://papers.nips.cc/paper/7220-when-worlds-collide-integrating-different-counterfactual-assumptions-in-fairness.pdf)|| -->
### Reinforcement Learning
|Name|Paper|Code|
|---|---|---|
|Deconfounded RL|[Lu, Chaochao, Bernhard Schölkopf, and José Miguel Hernández-Lobato. "Deconfounding reinforcement learning in observational settings." arXiv preprint arXiv:1812.10576 (2018).](https://arxiv.org/pdf/1812.10576)|[Python](https://github.com/CausalRL/DRL)|
||[Vansteelandt, Stijn, and Marshall Joffe. "Structural nested models and G-estimation: the partially realized promise." Statistical Science 29, no. 4 (2014): 707-731.](https://arxiv.org/pdf/1503.01589.pdf)|NA|
|Counterfactual-Guided Policy Search (CF-GPS)|Buesing, Lars, Theophane Weber, Yori Zwols, Sebastien Racaniere, Arthur Guez, Jean-Baptiste Lespiau, and Nicolas Heess. "Woulda, Coulda, Shoulda: Counterfactually-Guided Policy Search." arXiv preprint arXiv:1811.06272 (2018).|NA|
### Multi-Armed Bandit/Causal Bandit
|Name|Paper|Code|
|---|---|---|
|Causal Bandits|[Lattimore, Finnian, Tor Lattimore, and Mark D. Reid. "Causal bandits: Learning good interventions via causal inference." In Advances in Neural Information Processing Systems, pp. 1181-1189. 2016.](https://arxiv.org/abs/1606.03203)|NA|
|Offline+MAB|[Ye, Li, Yishi Lin, Hong Xie, and John Lui. "Combining Offline Causal Inference and Online Bandit Learning for Data Driven Decisions." arXiv preprint arXiv:2001.05699 (2020).](https://arxiv.org/pdf/2001.05699v1.pdf)|NA|
|B-kl-UCB, B-TS|[Zhang, Junzhe, and Elias Bareinboim. "Transfer learning in multi-armed bandit: a causal approach." In Proceedings of the 16th Conference on Autonomous Agents and MultiAgent Systems, pp. 1778-1780. 2017.](http://www.ifaamas.org/Proceedings/aamas2017/pdfs/p1778.pdf)|NA|
|Incremental Model|[Sawant, Neela, Chitti Babu Namballa, Narayanan Sadagopan, and Houssam Nassif. "Contextual Multi-Armed Bandits for Causal Marketing." arXiv preprint arXiv:1810.01859 (2018).](https://arxiv.org/pdf/1810.01859)|NA|
<!-- ### Causality and GAN
|Name|Paper|Code|
|---|---|---|
||Odena, Augustus, Jacob Buckman, Catherine Olsson, Tom B. Brown, Christopher Olah, Colin Raffel, and Ian Goodfellow. "Is Generator Conditioning Causally Related to GAN Performance?." arXiv preprint arXiv:1802.08768 (2018).|NA|
|Causal GAN|Kocaoglu, Murat, Christopher Snyder, Alexandros G. Dimakis, and Sriram Vishwanath. "CausalGAN: Learning Causal Implicit Generative Models with Adversarial Training." arXiv preprint arXiv:1709.02023 (2017).|[Python](https://github.com/mkocaoglu/CausalGAN)| -->
## Causal Discovery
### for i.i.d. Data
#### Classic Methods
|Name|Paper|Code|
|---|---|---|
|IC algorithm| |[Python](https://github.com/akelleh/causality)|
|PC algorithm|P. Spirtes, C. Glymour, and R. Scheines. Causation, Prediction, and Search. The MIT Press, 2nd edition, 2000.|[Python](https://github.com/keiichishima/pcalg) [R](https://github.com/cran/pcalg) [Julia](https://github.com/mschauer/CausalInference.jl)|
|FCI algorithm|P. Spirtes, C. Glymour, and R. Scheines. Causation, Prediction, and Search. The MIT Press, 2nd edition, 2000. |[R](https://github.com/cran/pcalg) [Julia](https://github.com/mschauer/CausalInference.jl)|
#### Continuous Optimization
|Paper|Venue|Code|
|---|---|---|
|[DAGs with NO TEARS: Continuous optimization for structure learning](http://papers.nips.cc/paper/8157-dags-with-no-tears-continuous-optimization-for-structure-learning)|NeurIPS 2018|[code](https://github.com/xunzheng/notears)|
|[DAG-GNN: DAG Structure Learning with Graph Neural Networks](https://arxiv.org/abs/1904.10098)|ICML 2019|[code](https://github.com/fishmoon1234/DAG-GNN)|
|[Learning Sparse Nonparametric DAGs](http://proceedings.mlr.press/v108/zheng20a/zheng20a.pdf)|AISTATS 2020|[code](https://github.com/xunzheng/notears)|
|[Amortized Inference for Causal Structure Learning](https://proceedings.neurips.cc/paper_files/paper/2022/file/54f7125dee9b8b3dc798bb9a082b09e2-Paper-Conference.pdf)|Neurips 2022|[code](https://github.com/larslorch/avici)|
#### Learning IV
|Name|Paper|Code|
|---|---|---|
|[Learning instrumental variables with structural and non-gaussianity assumptions](http://www.jmlr.org/papers/volume18/17-014/17-014.pdf)|JMLR|[code](http://www.homepages.ucl.ac.uk/~ucgtrbd/code/iv_discovery/)|
#### Distinguishing Cause from Effect (Bivariate)
|Name|Paper|Code|
|---|---|---|
|BMLiNGAM|S. Shimizu and K. Bollen. Bayesian estimation of causal direction in acyclic structural equation models with individual-specific confounder variables and non-Gaussian distributions. Journal of Machine Learning Research, 15: 2629-2652, 2014.|[Python](https://github.com/taku-y/bmlingam)|
|Sloppy|Marx, A & Vreeken, J Identifiability of Cause and Effect using Regularized Regression. In: Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), ACM, 2019.|[R](https://eda.mmci.uni-saarland.de/prj/sloppy/)|
|RECI|Blöbaum, Patrick, Dominik Janzing, Takashi Washio, Shohei Shimizu, and Bernhard Schölkopf. "Cause-effect inference by comparing regression errors." In International Conference on Artificial Intelligence and Statistics, pp. 900-909. PMLR, 2018.|in [CausalDiscoveryToolbox](https://github.com/FenTechSolutions/CausalDiscoveryToolbox)|
|bQCD|Tagasovska, Natasa, Valérie Chavez-Demoulin, and Thibault Vatter. "Distinguishing cause from effect using quantiles: Bivariate quantile causal discovery." In International Conference on Machine Learning, pp. 9311-9323. PMLR, 2020.|[code](https://github.com/tagas/bQCD)|
|CGNN|Goudet, Olivier, Diviyan Kalainathan, Philippe Caillou, Isabelle Guyon, David Lopez-Paz, and Michele Sebag. "Learning functional causal models with generative neural networks." In Explainable and interpretable models in computer vision and machine learning, pp. 39-80. Springer, Cham, 2018.|[code](https://github.com/GoudetOlivier/CGNN)|
#### Conditional Independence Tests (for Constraint-based Algorithms)
|Name|Paper|Code|
|---|---|---|
|RCIT|   |[R](https://github.com/ericstrobl/RCIT)|
#### Causal Discovery with Probabilistic Logic Programming
|Name|Paper|Code|
|---|---|---|
|Causal PSL|Sridhar, Dhanya, Jay Pujara, and Lise Getoor. "Scalable Probabilistic Causal Structure Discovery." In IJCAI, pp. 5112-5118. 2018.|[Java](https://bitbucket.org/linqs/causpsl)|
#### Scalable Ensemble Causal Discovery
|Name|Paper|Code|
|---|---|---|
|Scalable and Hybrid Ensemble-Based Causality Discovery|[Pei Guo, Achuna Ofonedu, Jianwu Wang. "Scalable and Hybrid Ensemble-Based Causality Discovery." In Proceedings of the 2020 IEEE International Conference on Smart Data Services (SMDS), pp. 72-80.](https://ieeexplore.ieee.org/document/9288491)|[Python](https://github.com/big-data-lab-umbc/ensemble_causality_learning)|
### with Temporal Data
|Name|Paper|Code|
|---|---|---|
|TCDF: Temporal Causal Discovery Framework|[Nauta, Meike, Doina Bucur, and Christin Seifert. "Causal discovery with attention-based convolutional neural networks." Machine Learning and Knowledge Extraction.](https://www.mdpi.com/2504-4990/1/1/19)|[Pytorch](https://github.com/M-Nauta/TCDF)|

# Awesome Causality Links

- [Awesome Causality](#awesome-causality)
  * [Other Awesome lists](#other-awesome-lists)
- [Data](#data)
- [Tools](#tools)
- [Learning resources](#learning-resources)
  * [Tutorials](#tutorials)
  * [Blogs](#blogs)
  * [Books](#books)
  * [Courses](#courses)
  * [Videos](#videos)
- [Events](#events)
  * [Workshops](#workshops)
- [Communities, and Mailing lists](#communities--and-mailing-lists)
- [Miscellaneous](#miscellaneous)
<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>
## Other Awesome lists
These list contain a more focused compilation of algorithms and data related to causality under more specific categories. 
* [awesome-causality-algorithms](https://github.com/rguo12/awesome-causality-algorithms)
* [awesome-causality-data](https://github.com/rguo12/awesome-causality-data)
# Data
* [Amazon Review Sales](https://github.com/rguo12/CIKM18-LCVA) - [Google drive](https://drive.google.com/drive/u/1/folders/1Ff_GdfjhrDFbZiRW0z81lGJW-cUrYmo1) - [Paper](https://arxiv.org/abs/1808.03333)
* [Jobs Training](http://users.nber.org/~rdehejia/data/nswdata2.html) - [Train](http://www.fredjo.com/files/jobs_DW_bin.train.npz) [Test](http://www.fredjo.com/files/jobs_DW_bin.test.npz) - [Paper](http://proceedings.mlr.press/v70/shalit17a.html)
* [Twins](https://github.com/AMLab-Amsterdam/CEVAE/tree/master/datasets/TWINS)
* [Synthetic IHDP](https://github.com/AMLab-Amsterdam/CEVAE/tree/master/datasets/IHDP)
* [2016 Atlantic Causal Inference competition](https://github.com/vdorie/aciccomp/tree/master/2016)
* [News trearment effect measurement](http://www.fredjo.com/files/NEWS_csv.zip)
* [Cause effect pairs](http://webdav.tuebingen.mpg.de/cause-effect/)
* [Movie recommendations - Missing not at random (MNAR)](http://www.cs.cornell.edu/~schnabts/mnar/index.html) - [Paper](http://proceedings.mlr.press/v48/schnabel16.html)
* [CHALEARN Fast Causation Coefficient Challenge](http://www.causality.inf.ethz.ch/cause-effect.php?page=rules) - [Kaggle](https://www.kaggle.com/c/cause-effect-pairs#description)
* [Causal inference datasets in quantitative social sciences](https://github.com/kosukeimai/qss)
# Tools
* [Counter factual regression](https://github.com/clinicalml/cfrnet) <img height="16" width="16" color="blue" src="https://unpkg.com/simple-icons@latest/icons/python.svg" />
* [DoWhy - Microsoft Research](https://github.com/Microsoft/dowhy) <img height="16" width="16" color="blue" src="https://unpkg.com/simple-icons@latest/icons/python.svg" />
* [Quantitative Social Science](https://github.com/kosukeimai/qss-package) - [Book](https://github.com/kosukeimai/qss) <img height="16" width="16" color="blue" src="https://unpkg.com/simple-icons@latest/icons/r.svg" />
* [Causal Inference using Bayesian Additive Regression Trees](https://github.com/vdorie/bartCause) <img height="16" width="16" color="blue" src="https://unpkg.com/simple-icons@latest/icons/r.svg" />
* [Non-parametrics for Causal Inference](https://github.com/vdorie/npci) <img height="16" width="16" color="blue" src="https://unpkg.com/simple-icons@latest/icons/r.svg" />
* [Causality by author of Causal Data Science Series (see blogs)](https://github.com/akelleh/causality) <img height="16" width="16" color="blue" src="https://unpkg.com/simple-icons@latest/icons/python.svg" />
* [InvariantCausalPrediction: Invariant Causal Prediction](https://cran.r-project.org/web/packages/InvariantCausalPrediction/index.html) <img height="16" width="16" color="blue" src="https://unpkg.com/simple-icons@latest/icons/r.svg" />
* [Causal Discovery Toolbox](https://github.com/Diviyan-Kalainathan/CausalDiscoveryToolbox) <img height="16" width="16" color="blue" src="https://unpkg.com/simple-icons@latest/icons/python.svg" />
* [CausalImpact - causal inference in time series](https://google.github.io/CausalImpact/) <img height="16" width="16" color="blue" src="https://unpkg.com/simple-icons@latest/icons/python.svg" />
* [Daggity - Create causal graphs](http://www.dagitty.net/) <img height="16" width="16" color="blue" src="https://unpkg.com/simple-icons@latest/icons/r.svg" />
* [TETRAD](http://www.phil.cmu.edu/projects/tetrad/) <img height="16" width="16" color="blue" src="https://unpkg.com/simple-icons@latest/icons/java.svg" />
* [ProbLog - Do-calculus](https://dtai.cs.kuleuven.be/problog/tutorial/various/14_robot_key.html) <img height="16" width="16" color="blue" src="https://unpkg.com/simple-icons@latest/icons/python.svg" />
* [Causalnex - A toolkit for causal reasoning with Bayesian Networks](https://github.com/quantumblacklabs/causalnex)
* [Causal Fusion - A web based app for drawing and making inference via do-calculus on causal diagrams](https://causalfusion.net/app)
# Learning resources
## Tutorials
* [CompSci 590.6, Understanding	Data: Theory	and	Applications Lecture	15 Causality	in	AI Instructor:	Sudeepa Roy Email:	sudeepa@cs.duke.edu](https://www2.cs.duke.edu/courses/fall15/compsci590.6/Lectures/Lecture-15.pdf)
* [ICML 2016 Tutorial Causal Inference for Observational Studies](https://cs.nyu.edu/~shalit/tutorial.html)
* [KDD 2018 Causal Inference Tutorial](https://causalinference.gitlab.io/kdd-tutorial/)
* [Joris Mooij ML2 Causality](https://web.archive.org/web/20190312053009/https://drive.google.com/file/d/0B2DZf1QHTotxX2RiNXJ0NUwwekk/edit)
* [Emre Kiciman - Observational Studies in Social Media (OSSM) at ICWSM 2017](https://web.archive.org/web/20180830204832/http://kiciman.org/wp-content/uploads/2016/06/tutorial_kiciman_ossm17.pdf)
* [The Blessings of Multiple Causes: A Tutorial](https://github.com/blei-lab/deconfounder_tutorial)
* [Susan Athey: Counterfactual Inference (NeurIPS 2018 Tutorial)](https://www.youtube.com/watch?v=yKs6msnw9m8) - [Slides](https://web.archive.org/web/20181214003957/https://media.neurips.cc/Conferences/NIPS2018/Slides/Counterfactual_Inference.pdf)
* [Ferenc Huszár Causal Inference Practical from MLSS Africa 2019](https://colab.research.google.com/drive/1rjjjA7teiZVHJCMTVD8KlZNu3EjS7Dmu#scrollTo=h2zDcSPqYuAa) - [\[Notebook Runthrough\]](https://www.youtube.com/watch?v=evmGGusk6gg) [\[Video 1\]](https://www.youtube.com/watch?v=HOgx_SBBzn0) [\[Video 2\]](https://www.youtube.com/watch?v=_RtxTpOb8e4) 
* [Causality notes and implementation in Python using statsmodels and networkX](https://github.com/ericmjl/causality)
* [Thinking Clearly About Correlations and Causation: Graphical Causal Models for Observational Data](https://journals.sagepub.com/doi/10.1177/2515245917745629)
* [The Hitchhiker’s Guide to the tlverse
or a Targeted Learning Practitioner’s Handbook](https://tlverse.org/tlverse-handbook/)
## Blogs, and Articles
* [Causal Data Science Series](https://medium.com/causal-data-science/causal-data-science-721ed63a4027)
* [Ferenc Huszár Series on Causal Modelling: various parts](https://www.inference.vc/) - [1](https://www.inference.vc/untitled/), [2](https://www.inference.vc/blessings-of-multiple-causes-causal-inference-when-you-cant-measure-confounders/), [3](https://www.inference.vc/causal-inference-2-illustrating-interventions-in-a-toy-example/), [4](https://www.inference.vc/causal-inference-3-counterfactuals/)
* [Diving deeper into causality Pearl, Kleinberg, Hill and untested assumptions](https://yanirseroussi.com/2016/05/15/diving-deeper-into-causality-pearl-kleinberg-hill-and-untested-assumptions/)
* [Simpson's Paradox: An Anatomy](http://bayes.cs.ucla.edu/R264.pdf)
* [Simpson’s paradox and causal inference with observational data](https://roamanalytics.com/2017/09/08/simpsons-paradox-and-causal-inference-with-observational-data/)
* [Causation and Correlation - Talks about possible causes for observed correlations](https://kunalmenda.com/2019/02/21/causation-and-correlation/)
* [(Non-)Identification in Latent Confounder Models](http://www.alexdamour.com/blog/public/2018/05/18/non-identification-in-latent-confounder-models/)
* [Causal Inference Animated Plots - Good explanation of various causal inference methods](http://nickchk.com/causalgraphs.html)
* [Explanation, prediction, and causality: Three sides of the same coin?](https://osf.io/u6vz5/)
* [A chill intro to causal inference via propensity scores](https://osf.io/preprints/socarxiv/ncvqs/)
* [All the DAGs from Hernan and Robins' Causal Inference Book by Sam Finlayson](https://sgfin.github.io/2019/06/19/Causal-Inference-Book-All-DAGs/) - [Causal Inference Book Part I -- Glossary and Notes](https://sgfin.github.io/2019/06/19/Causal-Inference-Book-Glossary-and-Notes/)
* [Causal Inference with Bayes Rule by Gradient Institute](https://gradientinstitute.org/blog/6/)
* [Causal Inference cheat sheet for data scientists](http://nc233.com/2020/04/causal-inference-cheat-sheet-for-data-scientists/)
## Books
* [Causal Inference Book](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)
* [Causal Inference in statistics: A primer](http://bayes.cs.ucla.edu/PRIMER/)
* [Elements of Causal Inference - Foundations and Learning Algorithms (includes code examples in R and Jupyter notebooks)](http://web.math.ku.dk/~peters/elements.html)
* [The Book of Why: The New Science of Cause and Effect](http://bayes.cs.ucla.edu/WHY/)
* [Causal Inference Mixtape](http://scunning.com/mixtape.html)
* [Elements of Causal Inference - Foundations and Learning Algorithms](https://mitpress.mit.edu/books/elements-causal-inference)
* [Actual Causality By Joseph Y. Halpern](https://www.cs.cornell.edu/home/halpern/papers/causalitybook-ch1-3.html)
* [Causal Reasoning: Fundamentals and Machine Learning Applications by Emre Kiciman and Amit Sharma ](https://causalinference.gitlab.io/)
## Courses 
* [Causal Diagrams: Draw Your Assumptions Before Your Conclusions](https://www.edx.org/course/causal-diagrams-draw-your-assumptions-before-your-conclusions)
* [Causal Inference: prediction, explanation, and intervention](http://www.skleinberg.org/teaching/CI18/index.html)
* [Causal Inference Experiments Short Course](http://www.macartan.nyc/experiment/short-course/)
* [ECON 305: Economics, Causality, and Analytics](http://www.nickchk.com/econ305.html) [\[github\]](https://github.com/NickCH-K/introcausality)
* [Algorithmic Information Dynamics: A Computational Approach to Causality and Living Systems From Networks to Cells](https://www.complexityexplorer.org/courses/63-algorithmic-information-dynamics-a-computational-approach-to-causality-and-living-systems-from-networks-to-cells-2018/)
* [Four Lectures on Causality by Jonas Peters](https://www.youtube.com/playlist?list=PLW01hpWnEtbTcuY0a0jhZyanHX3GPImAy)
* [Julian Schuessler's Causal Graphs Seminar - Winner of 2019 American Statistics Association Causality in Statistics Education Award](http://www.julianschuessler.net/graphs2018.html)
* [Ilya Shpitser's course on Causal Inference (Zip file) - Winner of 2017 American Statistics Association Causality in Statistics Education Award](https://www.amstat.org/asa/files/zipfiles/Causality-ShpitserMaterials.zip)
* [Arvid Sjölander's course on Causal Inference (Zip file) - Winner of 2016 American Statistics Association Causality in Statistics Education Award](https://ww2.amstat.org/misc/causaliity/Sjolander-Supplemental.zip)
* [Onyebuchi A. Arah course on Causality in Statistics (Dropbox folder) - Winner of 2016 American Statistics Association Causality in Statistics Education Award](https://www.dropbox.com/sh/mzuy3bewepwunye/AACn-zaBRAGMvxO-TVtCxH9Ba?dl=0)
* [Introduction to causal inference by Maya L. Petersen & Laura B. Balzer](https://www.ucbbiostat.com/labs)
## Videos
* [PyData LA 2018 Keynote: Judea Pearl - The New Science of Cause and Effect](https://www.youtube.com/watch?v=ZaPV1OSEpHw)
* [CACM Mar. 2019 - The Seven Tools of Causal Inference](https://www.youtube.com/watch?v=CsMV5o3hotY)
* [ACM Turing Award Lecture 2011 - Judea Pearl](https://amturing.acm.org/vp/pearl_2658896.cfm)
* [Leon Bottou - Learning representations using causal invariance](https://www.facebook.com/iclr.cc/videos/534780673594799/)
# Events
## Workshops 
* [Beyond Curve Fitting: Causation, Counterfactuals, and Imagination-based AI](https://why19.causalai.net/#)
* [Causality Challenge #1: Causation and Prediction](http://www.causality.inf.ethz.ch/challenge.php)
* [NIPS 2013 Workshop on Causality](http://clopinet.com/isabelle/Projects/NIPS2013/)
* [ChaLearn Fast Causation Coefficient Challenge](https://competitions.codalab.org/competitions/1381)
# Communities, and Mailing lists
* [Causality Challenge Google group](https://groups.google.com/forum/#!forum/causalitychallenge)
# Miscellaneous 
* [Causal Inference Reading list](https://yanirseroussi.com/causal-inference-reading-list/)
* [Causal inference paper reading list](https://web.archive.org/web/20190312230219/https://www.reddit.com/r/MachineLearning/comments/8lti7g/d_ml_beyond_curve_fitting_introduction_to_causal/dzipydw/)
* [American Statistics Association Causality in Statistics Education Award](https://www.amstat.org/ASA/Your-Career/Awards/Causality-in-Statistics-Education-Award.aspx)
  
