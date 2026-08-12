Kronos: A Foundation Model for the Language of Financial Markets
YuShi1,†,ZongliangFu2,†,ShuoChen1,BohanZhao1,WeiXu1,ChangshuiZhang2,JianLi1
1InstituteforInterdisciplinaryInformationSciences,2DepartmentofAutomation
TsinghuaUniversity
{shi-y23,fzl22,zhaobh23}@mails.tsinghua.edu.cn,ChenSh2003@outlook.com,weixu@tsinghua.edu.cn,
zcs@mail.tsinghua.edu.cn,lapordge@gmail.com
5202 guA 2  ]TS.nif-q[  1v93720.8052:viXra
Return Forecasting
|     |     |     |          |     |     |     |     |                        |     | 0.0675(RankIC) |     | R e         | t urn Forecasting |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | ---------------------- | --- | -------------- | --- | ----------- | ----------------- | --- |
|     |     |     | Abstract |     |     |     |     | Volatility Forecasting |     |                |     | 0.0702 (I C | )                 |     |
(MAE)
0.037
Thesuccessoflarge-scalepre-trainingparadigm,exemplified
Price Forecasting
byLargeLanguageModels(LLMs),hasinspiredthedevel- 0.0267(RankIC)
| opmentofTimeSeriesFoundationModels(TSFMs).How- |     |     |     |     |     |     | Volatility Forecasting |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
ever, their application to financial candlestick (K-line) data (R2) 0.262 0.0330.040
0.066
remains limited, often underperforming non-pre-trained ar- 0.009
|     |     |     |     |     |     |     |     |     |     | 0.120 |     |     | Price Forecasting |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----------------- | --- |
chitectures. Moreover, existing TSFMs often overlook cru- 0.021 0.044(IC)
0.243
| cialdownstreamtaskssuchasvolatilitypredictionandsyn- |     |     |     |     |     |     |     |     |     |     | 0.964 |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
0.001
theticdatageneration.Toaddresstheselimitations,wepro- 0.305 -0.0130.066
Kline Generation
pose Kronos, a unified, scalable pre-training framework (Disc. Score) Investment Simulation
(IR)
| tailoredtofinancialK-linemodeling.Kronosintroducesa |     |     |     |     |     |     |     |     |     |     |     |     | 1.65 |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
Our Models
specialized tokenizer that discretizes continuous market in- Kronoslarge
|     |     |     |     |     |     |     |     |     | 0.0301 |     |     |     | K r o n | o s b a s e |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ------- | ----------- |
formation into token sequences, preserving both price dy- Kline Generat i o n K r o n o s sm a ll
|     |     |     |     |     |     |     |     |     | ( I C ) |     |     | 0.208 | B a s e | li n e s  (Best Results) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ----- | ------- | ------------------------ |
namicsandtradeactivitypatterns.Wepre-trainKronosusing Kline Generation0.0282 Zero-shot Time Series Models
|     |     |     |     |     |     |     |     |     |     | (RankIC) | Investment Simulation |     | Full-shot Time Series Models |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------------- | --- | ---------------------------- | --- |
anautoregressiveobjectiveonamassive,multi-marketcorpus (AER) Econometric Volatility Models
Generative Time Series Models
ofover12billionK-linerecordsfrom45globalexchanges,
enablingittolearnnuancedtemporalandcross-assetrepre-
Figure1:ComprehensiveperformanceofKronosacrosssev-
| sentations. | Kronos | excels | in a zero-shot | setting | across | a di- |      |              |     |         |        |           |            |     |
| ----------- | ------ | ------ | -------------- | ------- | ------ | ----- | ---- | ------------ | --- | ------- | ------ | --------- | ---------- | --- |
|             |        |        |                |         |        |       | eral | quantitative |     | finance | tasks. | The chart | benchmarks | our |
versesetoffinancialtasks.Onbenchmarkdatasets,Kronos
|     |     |     |     |     |     |     | Kronos | models | (blue | family) | against | several |     | categories of |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ----- | ------- | ------- | ------- | --- | ------------- |
boostspriceseriesforecastingRankICby93%overthelead-
specializedbaselines.Agreaterdistancefromthecentersig-
| ing TSFM | and | 87% over | the best | non-pre-trained | baseline. |     |     |     |     |     |     |     |     |     |
| -------- | --- | -------- | -------- | --------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
It also achieves a 9% lower MAE in volatility forecasting nifiessuperiorperformance.
| and a 22% | improvement |     | in generative | fidelity | for synthetic |     |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ------------- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
K-linesequences.TheseresultsestablishKronosasarobust,
versatilefoundationmodelforend-to-endfinancialtimese-
|                |     |                 |       |             |           |     | diverse | time      | series | analytical | tasks—from        |     | forecasting | and      |
| -------------- | --- | --------------- | ----- | ----------- | --------- | --- | ------- | --------- | ------ | ---------- | ----------------- | --- | ----------- | -------- |
| ries analysis. |     | Our pre-trained | model | is publicly | available | at  |         |           |        |            |                   |     |             |          |
|                |     |                 |       |             |           |     | anomaly | detection |        | to causal  | inference—thereby |     |             | substan- |
https://github.com/shiyu-coder/Kronos.
|     |     |     |     |     |     |     | tially | reducing | the | need | for bespoke | model | design | in each |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | ---- | ----------- | ----- | ------ | ------- |
applicationdomain.
|     |     | 1 Introduction |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Withinthisexpandingresearchlandscape,financialmar-
| The emergence |     | of Foundation |     | Models (FMs) | has | initiated |      |       |        |            |     |             |     |             |
| ------------- | --- | ------------- | --- | ------------ | --- | --------- | ---- | ----- | ------ | ---------- | --- | ----------- | --- | ----------- |
|               |     |               |     |              |     |           | kets | stand | out as | a critical | and | challenging |     | application |
aparadigmshiftacrossartificialintelligence,reshapingthe
|                  |     |                   |                |          |                |     | area      | for TSFMs, |               | given  | their inherent |         | data richness, | high-      |
| ---------------- | --- | ----------------- | -------------- | -------- | -------------- | --- | --------- | ---------- | ------------- | ------ | -------------- | ------- | -------------- | ---------- |
| methodologies    |     | of representation |                | learning | and downstream |     |           |            |               |        |                |         |                |            |
|                  |     |                   |                |          |                |     | frequency |            | observations, |        | and complex,   |         | non-stationary | tem-       |
| task adaptation. |     | This shift        | is exemplified |          | by the success | of  |           |            |               |        |                |         |                |            |
|                  |     |                   |                |          |                |     | poral     | dynamics.  |               | At the | core           | of this | domain         | are K-line |
Large Language Models (LLMs) for natural language pro- sequences, multivariate time series derived from candle-
| cessing (Brown |     | et al. 2020; | Achiam | et al. | 2023), | with par- |       |        |      |        |       |       |      |           |
| -------------- | --- | ------------ | ------ | ------ | ------ | --------- | ----- | ------ | ---- | ------ | ----- | ----- | ---- | --------- |
|                |     |              |        |        |        |           | stick | charts | that | record | Open, | High, | Low, | and Close |
allelbreakthroughsincomputervision(Radfordetal.2021;
|     |     |     |     |     |     |     | prices, | along | with | trading | Volume | and | Amount | (Turnover) |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ---- | ------- | ------ | --- | ------ | ---------- |
Kirillovetal.2023).
|                   |          |                 |          |              |          |         | over    | fixed | intervals | (OHLCVA). |                   | These     | sequences | con-        |
| ----------------- | -------- | --------------- | -------- | ------------ | -------- | ------- | ------- | ----- | --------- | --------- | ----------------- | --------- | --------- | ----------- |
| Inspired          | by       | these advances, |          | the FM       | paradigm | has re- |         |       |           |           |                   |           |           |             |
|                   |          |                 |          |              |          |         | stitute | a     | highly    | compact,  | information-dense |           |           | “language”  |
| cently been       | extended | to              | temporal | data, giving | rise     | to Time |         |       |           |           |                   |           |           |             |
|                   |          |                 |          |              |          |         | through | which | market    |           | participants      | interpret |           | price move- |
| Series Foundation |          | Models          | (TSFMs)  | (Garza,      | Challu,  | and     |         |       |           |           |                   |           |           |             |
ments,volatilityregimes,liquidityshifts,andcollectivesen-
| Mergenthaler-Canseco |     | 2023;   | Woo    | et al.   | 2024;        | Xiaoming |        |        |        |               |     |        |      |           |
| -------------------- | --- | ------- | ------ | -------- | ------------ | -------- | ------ | ------ | ------ | ------------- | --- | ------ | ---- | --------- |
|                      |     |         |        |          |              |          | timent | (Nison | 2001). | Consequently, |     | K-line | data | forms the |
| et al. 2025).        | The | central | aim is | to build | pre-trained, | task-    |        |        |        |               |     |        |      |           |
bedrockofnumerousalgorithmictradingstrategies,portfo-
agnosticarchitecturesthatserveasuniversalbackbonesfor
liooptimizationschemes,andriskmanagementsystems.
†Equalcontribution However, applying general-purpose TSFMs to financial

K-linedatapresentssignificantchallenges,duetotwoprin- Kronos establishes a new state-of-the-art in price series
cipal factors. First, K-line sequences exhibit unique statis- forecasting,significantlyoutperformingbothTSFMsand
tical properties—such as low signal-to-noise ratios, strong specialized baselines. The model’s versatility is further
non-stationarities, and intricate, high-order dependencies demonstratedbyitsstrongperformanceacrossabroader
among OHLCVA attributes (Zhang and Hua 2025; Baidya spectrum of quantitative tasks, including volatility fore-
andLee2024)—thatareoftenmisalignedwiththeinductive castingandsyntheticK-linegeneration.
biasesofgenericTSFMs.Second,thefinancialdomainhas
largelybeenunderservedbymainstreamTSFMresearch;fi- 2 Preliminary
nancialsequencesconstituteaminorfractionofpre-training
|         |          |          |       |      |        |       |     | Let D-dimensional |     | vector | x   | ∈ RD denote | the | K-line ob- |
| ------- | -------- | -------- | ----- | ---- | ------ | ----- | --- | ----------------- | --- | ------ | --- | ----------- | --- | ---------- |
| corpora | for most | existing | TSFMs | (Das | et al. | 2024; | Gao |                   |     |        | t   |             |     |            |
et al. 2024; Xiaoming et al. 2025) , and the spectrum of servation at discrete time t, comprising D key financial in-
downstreamtaskscriticaltoquantitativefinance—spanning dicators.Inthiswork,wefixthedimensionD =6torepre-
|     |     |     |     |     |     |     |     | sent OHLCVA | attributes |     | (Open, | High, | Low, Close | prices, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ------ | ----- | ---------- | ------- |
volatilityestimation,syntheticsequencegeneration,andrisk
|                    |     |     |         |              |       |         |     | trading Volume, |             | and Amount). |          | The rationale |             | for this in- |
| ------------------ | --- | --- | ------- | ------------ | ----- | ------- | --- | --------------- | ----------- | ------------ | -------- | ------------- | ----------- | ------------ |
| management—remains |     |     | largely | unaddressed. | These | factors |     |                 |             |              |          |               |             |              |
|                    |     |     |         |              |       |         |     | put choice      | is detailed | in           | Appendix | H             | (Q1). Given | a his-       |
leadtoanimportantobservation,whichweempiricallyval-
idate in this work: general-purpose TSFMs often under- torical sequence x 1:T = (x 1 ,x 2 ,...,x T ), our objective
perform specialized, non-pre-trained models (e.g., iTrans- is to predict the following H observations xˆ T+1:T+H =
former(Liuetal.2023))onfinancialtasksandfailtogener- (xˆ ,xˆ ,...,xˆ ).
|     |     |     |     |     |     |     |     | T+1 T+2 |                | T+H |        |            |         |        |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | ------ | ---------- | ------- | ------ |
|     |     |     |     |     |     |     |     | Rather  | than operating |     | on raw | continuous | inputs, | Kronos |
alizeacrossthebroaderlandscapeofquantitativefinance.
|            |     |                     |     |     |           |         |     | first quantizes | each | multivariate |     | observation | x   | into a dis- |
| ---------- | --- | ------------------- | --- | --- | --------- | ------- | --- | --------------- | ---- | ------------ | --- | ----------- | --- | ----------- |
| To address |     | these shortcomings, |     | we  | introduce | Kronos, |     |                 |      |              |     |             | t   |             |
|            |     |                     |     |     |           |         |     |                 | b    |              |     |             | C.  |             |
a unified, scalable pre-training framework designed crete token t via a learnable codebook Consequently,
specifically for financial K-line data. Kronos employs a the original sequence x 1:T = (x 1 ,...,x T ) is mapped to
|     |     |     |     |     |     |     |     | b = (b | ,...,b | ). The | forecasting |     | task then | reduces to |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------ | ----------- | --- | --------- | ---------- |
specialized tokenizer to discretize continuous, multivariate 1:T 1 T
anautoregressivetoken-sequencemodelingproblem:
K-lineinputsintoasequenceofcompacttokens,preserving
criticalprice–volumeinteractions.Itthenundergoesautore-
(cid:89) H
gressivepre-trainingonanexpansive,heterogeneouscorpus (cid:0) (cid:1)
|     |     |     |     |     |     |     |     | p(b T+1:T+H | |b  | 1:T )= |     | p b T+h | |b 1:T+h−1 | . (1) |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | --- | ------- | ---------- | ----- |
ofover12billionK-linerecordsdrawnfromover45global
h=1
marketsand7temporalgranularities.
Suchadiscreteformulationisinherentlyscalableandnat-
| We validate |     | the efficacy | of  | Kronos | through | comprehen- |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------ | --- | ------ | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
urallyextendstoothertasksthatcanbeframedgeneratively,
siveexperimentsacrossarangeofquantitativefinancetasks,
suchassyntheticdatagenerationandvolatilityforecasting.
| with a high-level |          | summary | presented    |     | in Figure | 1. On       | the |     |     |     |     |     |     |     |
| ----------------- | -------- | ------- | ------------ | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| core task         | of price | series  | forecasting, |     | Kronos    | establishes | a   |     |     |     |     |     |     |     |
3 Methodology
| new state-of-the-art, |     | boosting |     | the RankIC | by 93% | over | the |     |     |     |     |     |     |     |
| --------------------- | --- | -------- | --- | ---------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
leading TSFM and by 87% over the best-performing non- Kronos abstracts financial K-line sequences as a discrete
pre-trained baseline. Furthermore, it demonstrates strong language and implements this via a two-phase framework
versatilitybyachievinga9%lowerMAEinvolatilityfore- illustratedinFigure2:(1)K-lineTokenizationand(2)Au-
casting and a 22% improvement in generative fidelity for toregressive Pre-training. In the first phase, we design a
synthetic K-line generation. These findings highlight the specialized Transformer-based tokenizer to quantize a con-
broad effectiveness of our approach and underscore Kro- tinuous, multivariate K-line sequence into a corresponding
nos’spotentialasarobustfoundationmodelforinterpreting sequenceofdiscretetokens,viaalearnablecodebook.Each
thecomplex“language”offinancialmarkets. K-line item (OHLCVA) is treated as an individual instance
Ourmaincontributionscanbesummarizedasfollows: andquantizedintoadiscretetoken.Eachtokeniscomposed
|     |     |     |     |     |     |     |     | of a coarse-grained |     | subtoken |     | and a fine-grained |     | subtoken. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | -------- | --- | ------------------ | --- | --------- |
• WeproposeanovelmodelingframeworkforfinancialK-
|       |               |        |              |                  |           |      |      | This property | is enforced |         | via | a hierarchical | reconstruction |            |
| ----- | ------------- | ------ | ------------ | ---------------- | --------- | ---- | ---- | ------------- | ----------- | ------- | --- | -------------- | -------------- | ---------- |
| line  | data that     | learns | hierarchical | representations. |           | It   | fea- |               |             |         |     |                |                |            |
|       |               |        |              |                  |           |      |      | loss, which   | explicitly  | compels |     | the subtokens  | to             | model dis- |
| tures | a specialized |        | tokenizer    | that             | quantizes | each | mul- |               |             |         |     |                |                |            |
tinctlevelsofinformation,therebycreatingacoarse-to-fine
| tivariate | K-line | record | into | structured, | dual-component |     |     |     |     |     |     |     |     |     |
| --------- | ------ | ------ | ---- | ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
informationalhierarchy.Inthesecondphase,anautoregres-
(coarseandfine)tokens,coupledwithatailoredautore-
|          |           |      |          |       |           |         |     | sive decoder-only  |     | Transformer |     | is pre-trained | on         | these to- |
| -------- | --------- | ---- | -------- | ----- | --------- | ------- | --- | ------------------ | --- | ----------- | --- | -------------- | ---------- | --------- |
| gressive | objective | that | predicts | these | subtokens | sequen- |     |                    |     |             |     |                |            |           |
|          |           |      |          |       |           |         |     | kenized sequences, |     | using       | the | standard       | next-token | predic-   |
tially.Thiscoarse-to-finepredictionschemeallowsKro-
|     |     |     |     |     |     |     |     | tion objective | to sequentially |     |     | forecast both | subtoken | levels |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------------- | --- | --- | ------------- | -------- | ------ |
nostoexplicitlymodelmulti-scalemarketdynamics.
|     |     |     |     |     |     |     |     | at each future | time | step | conditioned | on  | the given | historical |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ---- | ----------- | --- | --------- | ---------- |
• Weconductlarge-scalepre-trainingforafamilyofKro- context. This unified discretize-and-generate paradigm en-
nosmodelswithvaryingcapacities.Thisisperformedon ablesKronostoconstructahigh-fidelity,hierarchicalrepre-
amassive,diversefinancialcorpusofover12billionK-
sentationofmarketdynamics,providingarobustfoundation
linerecordsfromover45globalexchanges,whichisfun-
fordownstreamquantitativeanalysis.
damentaltolearningtherobustandgeneralizablemarket
representationsthatunderpinthemodels’effectiveness. K-lineTokenization
• Weconductcomprehensiveempiricalevaluationsacross The first stage of Kronos transforms a continuous, D-
asetofquantitativefinancetasks.Ourresultsshowthat dimensionalK-linesequencex=(x ,...,x ),wherex ∈
|     |     |     |     |     |     |     |     |     |     |     |     | 1   | T   | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Figure 2: The two-stage framework of Kronos. (1) Instance-based K-line Tokenization: A Transformer-based autoencoder
with a dual reconstruction objective quantizes continuous K-line data into a vocabulary of hierarchical discrete tokens, each
comprisingacoarseandafinesubtoken.(2)AutoregressivePre-training:Adecoder-onlyTransformerispre-trainedtomodel
thetemporaldynamicsbysequentiallypredictingthehierarchicalsubtokensforthenexttimestep,conditionedonthepast.
RD encodes OHLCVA indicators, into a corresponding se- wetrainthetokenizerwithacompositeobjectivethatcom-
riesofdiscretetokens.ThisisachievedusingaTransformer- bines a hierarchical reconstruction loss and a commitment
| basedautoencoder(Figure3)composedofanencoderE |     |     |     |     |     | ,   | lossforBSQ: |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
enc
aquantizerQ,andadecoderE
|                    |         |     | dec .Drawinginspirationfrom |     |          |      |     | L         | =L     | +L +λL | ,     | (2) |
| ------------------ | ------- | --- | --------------------------- | --- | -------- | ---- | --- | --------- | ------ | ------ | ----- | --- |
|                    |         |     |                             |     |          |      |     | tokenizer | coarse | fine   | quant |     |
| video quantization | methods |     | in generative               |     | modeling | (Van |     |           |        |        |       |     |
whereλisabalancinghyperparameter.Thecomponentsare
| Den Oord, Vinyals | et  | al. 2017; | Yu  | et al. 2023), |     | we adapt |     |     |     |     |     |     |
| ----------------- | --- | --------- | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
definedas:
| Binary Spherical | Quantization |     | (BSQ) | (Zhao, | Xiong, | and |     |     |               |                       |            |        |
| ---------------- | ------------ | --- | ----- | ------ | ------ | --- | --- | --- | ------------- | --------------------- | ---------- | ------ |
|                  |              |     |       |        |        |     | • L | =   | E(cid:2) ∥x−E | (bc)∥2(cid:3) , which | trains the | coarse |
Kra¨henbu¨hl 2024), a variant of Look-up Free Quantization coarse dec
subtokenbctoformalow-fidelityreconstruction.
(LFQ)(Yuetal.2023),forthistask.Wediscusstherationale
|                                                   |     |     |     |     |     |     |      | E(cid:2) | (b)∥2(cid:3) |                   |     |           |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | -------- | ------------ | ----------------- | --- | --------- |
|                                                   |     |     |     |     |     |     | • L  | =        | ∥x−E         | , which evaluates |     | the high- |
| forthischoiceinAppendixH(Q2).BSQquantizesacontin- |     |     |     |     |     |     | fine |          | dec          |                   |     |           |
fidelityreconstructionusingthecompletetokenb.
| uouslatentvectorξ | intoak-bitbinarycodeb |     |     |     | ∈{−1,1}k |     |     |     |     |     |     |     |
| ----------------- | --------------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
|                   | t                     |     |     |     | t        |     |     |     |     |     |     |     |
by projecting it onto a set of learnable hyperplanes. While • L is the quantization loss from BSQ (Zhao, Xiong,
quant
a large number of bits k (e.g., k = 20) is desirable for andKra¨henbu¨hl2024)thatregularizesthelearningpro-
capturing rich financial patterns, it results in an exponen- cess.ItpenalizestheL2distancebetweencontinuousla-
|                         |     |         | 2k,   |            |     |          | tentvectorsξ |     | andtheirbinarycodesb,aligningtheen- |     |     |     |
| ----------------------- | --- | ------- | ----- | ---------- | --- | -------- | ------------ | --- | ----------------------------------- | --- | --- | --- |
| tially large vocabulary |     | of size | which | introduces |     | signifi- |              |     |                                     |     |     |     |
cant challenges for the subsequent autoregressive model in coder’soutputswiththelearnedcodebooktoensuresta-
| termsofcomputationalcostandparametersize.Tomitigate |     |     |     |     |     |     | bletraining. |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
this, we follow recent work in video quantization and gen- Thishierarchicalreconstructionobjectiveiscentraltoour
eration(Yuetal.2023;Wangetal.2025)andfactorizethe design.ByoptimizingL ,thecoarsesubtokenbclearns
coarse
k-bitcodeintonsubspaces.Motivatedbythetrade-offbe- tocapturetheprincipalstructureoftheinput.Consequently,
tween parameter savings and latency costs detailed in Ap- during the optimization of L , the fine-grained subtoken
fine
pendix H (Q3), we set n = 2. We partition the code into a bf isguidedtoencodetheresidualinformationrequiredto
coarsesubtokenbcandafinesubtokenbf refinethecoarseapproximation.Priorworkhasshownthat
|                        | t   |     |          | t ofequalbitlength, |     |     |                  |     |          |                |            |       |
| ---------------------- | --- | --- | -------- | ------------------- | --- | --- | ---------------- | --- | -------- | -------------- | ---------- | ----- |
|                        |     |     |          |                     |     |     | a coarse-to-fine |     | decoding | order improves | generation | qual- |
| k c = k f = k/2,wherek |     | =   | k c +k f | .Theresultingcodeb  |     | t   |                  |     |          |                |            |       |
is a concatenation of these two subtokens: b = (cid:2) bc, bf(cid:3) , ity (Wang et al. 2025). Instead of identifying and prioritiz-
|             |                                        |     |     |     | t   | t t |         |          |           |                 |         |        |
| ----------- | -------------------------------------- | --- | --- | --- | --- | --- | ------- | -------- | --------- | --------------- | ------- | ------ |
|             |                                        |     |     |     |     |     | ing the | decoding | of tokens | that inherently | contain | coarse |
| withbc,bf ∈ | {−1,1}k/2.Thisdecompositiontransformsa |     |     |     |     |     |         |          |           |                 |         |        |
t t information, our approach is designed to explicitly impose
| singlepredictionoveralargevocabularyofsize2k |     |     |     |     |     | intotwo |                |     |                 |                      |     |          |
| -------------------------------------------- | --- | --- | --- | --- | --- | ------- | -------------- | --- | --------------- | -------------------- | --- | -------- |
|                                              |     |     |     |     |     |         | this hierarchy |     | into the tokens | during quantization. |     | This en- |
sequentialpredictionsover2k/2entries,substantiallyreduc- sures that the first subtoken consistently represents coarse-
ingbothcomputationalandparametercomplexity.
grainedinformation,establishingthedesiredconditionalde-
To enforce a coarse-to-fine structure within each token, pendencyforthesubsequentautoregressivemodelingstage.

Layers d d Heads Vocab.(2k) Params
model ff
Kronos 8 512 1024 8 20 24.7M
small
Kronos 12 832 2048 16 20 102.3M
base
Kronos 18 1664 3072 32 20 499.2M
large
Table 1: Model configurations for the Kronos family. We
detail the number of Transformer layers, model dimension
(d ),feed-forwarddimension(d ),numberofattention
model ff
heads,vocabularysize,andthetotalnumberofparameters.
where [·;·] denotes concatenation, and W is a learnable
fuse
weightmatrixresponsibleforprojectingthecombinedrep-
resentationintothemodel’slatentspace.
Thesequenceoffusedinputs{v ,...,v }isthenpro-
1 t−1
cessed by the Transformer E , which outputs contextual-
ar
ized hidden states. The final hidden state from processing
b ,denotedash ,isthenusedtopredictthetokenb .This
<t t t
hidden state subsequently informs the autoregressive pre-
Figure 3: Architecture of the K-line Tokenizer. It employs
dictions of both coarse and fine subtokens at the next step,
a Transformer-based autoencoder with a Binary Spherical
therebyenablingthemodeltoeffectivelycapturemulti-scale
Quantization(BSQ)layer.
temporaldependenciesinherentinthedata.
Coarse Subtoken Prediction. The history vector h is
t
HierarchicalAutoregressiveModeling projectedbyalinearheadW c toproducelogitsforthefirst
subtoken’sdistribution:
Following the tokenization stage, the resulting discrete se-
quencesaremodeledusingadecoder-onlyTransformer,de- p(bc|b )=softmax(W h ) (6)
t <t c t
notedasE ,whichemployscausal-attentiontoensurethat
ar
Fine Subtoken Prediction. To model the conditional
predictions at each time step depend exclusively on histor-
dependency in Equation (4), the context needs to be up-
ical context. The primary objective is to estimate the joint
distribution over the token sequence b = {b 1 ,...,b T }. A dated with the predicted coarse subtoken,ˆbc t . During train-
simplifiedformofEquation1canbederivedas: ing, we use the model’s own prediction from the previ-
ous step,ˆbc, which is sampled from the predicted distribu-
(cid:89) T tionp(bc|b t <t),ratherthanusingtheground-truthsubtoken
p(b)= p(b |b ), (3) t
t <t (i.e.,teacher-forcing).Wefindthatthissamplingstrategyen-
t=1 hancesmodelrobustnessbymitigatingexposurebias,better
whereb denotesallprecedingtokensuptotimet−1. aligningthetrainingdistributionwiththeauto-regressivena-
<t
Giventhehierarchicaltokendesign,inwhicheachtoken ture of multi-step inference where ground-truth tokens are
isstructuredasb =[bc,bf],wefurtherdecomposethecon- unavailable.Weuseacross-attentionmechanismwherethe
ditionalprobabili t tyusi t ng t thechainruletoexplicitlycapture embedding ofˆbc t acts as the query, and the history h t pro-
theinherentcoarse-to-finedependency: videsthekeyandvalue.Theresultisprojectedbythesecond
headW :
f
p(b |b )=p(bc|b )·p(bf|b ,bc). (4)
t <t t <t t <t t hupdate =CrossAttn(q =e (ˆbc),k =v =h )
Thisformulationallowsthemodeltofirstpredictthecoarse- t c t t (7)
grained subtoken, which serves as a scaffold for subse- p(bf t |b <t ,bc t )=softmax(W f hu t pdate)
quentlygeneratingthefine-grainedresidualsubtoken.Con-
The overall training objective L is the negative log-
sequently,thepre-trainingobjectivereducestomaximizing ar
likelihoodofthedata,summedoverbothpredictionsteps:
thelog-likelihoodoftheobservedsequenceunderthishier-
archicalfactorization. T
(cid:88)(cid:104) (cid:105)
As depicted in Figure 2 (Right), the autoregressive pro- L =−E logp(bc|b )+logp(bf|b ,bc)
ar b∼D t <t t <t t
cess begins by constructing a unified input vector for each
t=1
time step. Specifically, at time i, the subtokens bc and bf (8)
i i
are independently projected into vector representations us- whereDrepresentsthedatadistribution.
ing two distinct embedding layers, resulting in representa-
ModelPre-training
tionse (bc)ande (bf),respectively.Theseembeddingsare
c i f i
thenconcatenatedandlinearlyprojectedtoproduceafused Dataset To ensure the quality of pre-training, we curate
inputvector: alarge-scale,high-qualityfinancialK-linedatasetfromthe
ground up. In contrast to foundation-model research on
v =W ([e (bc);e (bf)]), (5) generictimeseries—wherewell-curatedpublicdatasetsare
i fuse c i f i

(a) Price Series Forecasting
)
| 0.04          |     |     |     |     |     |     |     |     |     |     | Metric |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
| ( CIknaR & CI |     |     |     |     |     |     |     |     |     |     | IC     |     |
RankIC
0.02
0.00
Kronoslarge Kronosbase Kronossmall TimesNet DLinear NSTransformer PatchTST TimeMixer FEDformer iTransformer TimeXer TimeMOEbase TimeMOEsmall Chronoslarge Chronosbase TimesFM Chronossmall Moiraibase Moirailarge Momentsmall Moiraismall Momentlarge Momentbase
(b) Return Forecasting
| )                  |     |     |     |     |     |     |     |     |     |     | Metric |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
| ( CIknaR & CI 0.06 |     |     |     |     |     |     |     |     |     |     | IC     |     |
RankIC
0.04
0.02
0.00
Kronoslarge Kronosbase Kronossmall DLinear NSTransformer PatchTST TimesNet FEDformer iTransformer TimeXer TimeMixer TimeMOEsmall TimeMOEbase Moiraismall Moiraibase Momentbase Moirailarge Momentsmall Momentlarge TimesFM Chronoslarge Chronosbase Chronossmall
(c) Realized Volatility Forecasting
Metric
MAE
| ) 0.10 |     |     |     |     |     |     |     |     |     |     |     | R2 0.2 ) |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
| ( EAM  |     |     |     |     |     |     |     |     |     |     |     | ( 2R     |
| 0.05   |     |     |     |     |     |     |     |     |     |     |     | 0.1      |
0.00 Kronoslarge Kronosbase Kronossmall GARCH ARCH iTransforme r STransformer TimesNet PatchTST TimeXer FEDformer DLinear TimeMixer Momentbase Chronossmall Chronosbase Momentsmall Chronoslarge Momentlarge TimeMOEsmall TimeMOEbase Moirailarge Moiraibase TimesFM Moiraismall 0.0
N
|              | (d) Synthetic Kline Generation |                    |               |           |     |     | (e) Investment Simulation |     |     |     |        |        |
| ------------ | ------------------------------ | ------------------ | ------------- | --------- | --- | --- | ------------------------- | --- | --- | --- | ------ | ------ |
| ) 0.3        |                                |                    | 0.03 )        | 0.2       |     |     |                           |     |     |     |        |        |
|              |                                | D Metric isc.Score | ( CIknaR & CI |           |     |     |                           |     |     |     | Metric | AER    |
| ( erocS.csiD |                                | IC                 | 0.02          | )         |     |     |                           |     |     |     |        | IR 1   |
| 0.2          |                                | RankIC             | 0.01          | ( REA 0.1 |     |     |                           |     |     |     |        | )      |
|              |                                |                    |               |           |     |     |                           |     |     |     |        | 0 ( RI |
|              |                                |                    | 0.00          | 0.0       |     |     |                           |     |     |     |        |        |
0.1
|     |     |     | 0.01 |     |     |     |     |     |     |     |     | 1   |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Kronoslarge Kronosbase Kronossmall DiffusionTS TimeGAN TimeVAE 0 .1 ronoslarge Kronosbase Kronossmall PatchTST TimeXer TimesNet DLinear FEDforme r STransformer TimeMixer iTransformer Momentlarge Moirailarge TimesFM TimeMOEbase Chronoslarge
K
N
Kronos (Ours) Full-shot Time Series Models Zero-shot Time Series Models Econometric Volatility Models Generative Time Series Models
Figure 4: Main experimental results across five representative financial tasks. Subfigures (a-c) show forecasting performance
on price series, returns, and realized volatility. Subfigure (d) displays generative model performance in terms of fidelity and
usefulness.Subfigure(e)presentstheinvestmentsimulationbacktestingresults.
readilypooled—comprehensive,high-qualityfinancialdata stochasticityofthisprocessiscontrolledviastandardtech-
remain limited. Our dataset spans over 12 billion observa- niques like temperature scaling and top-p (nucleus) sam-
tionsacross7samplingfrequencies,encompassingabroad pling (Holtzman et al. 2019). The probability of sampling
spectrumofassetclassesdrawnfrom45globalexchanges. tokenifromlogitszisgivenbyp ∝exp(z /T),whereT is
|     |     |     |     |     |     |     |     |     | i   |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
To guarantee data quality, we develop a streamlined data- the temperature. For tasks requiring high precision, predic-
cleaning pipeline tailored to the unique characteristics of tionaccuracycanbeenhancedbygeneratingmultiplefuture
financial K-line data, which identifies and filters out low- trajectories(i.e.,MonteCarlorollouts)andaveragingthede-
qualitysegmentssuchasthosewithabnormalpricespikesor codedcontinuousvaluestoproduceamorestableforecast.
prolongedperiodsofinactivity.Furtherdetailsontheclean- As demonstrated in our experiments, this approach consis-
ingpipelineareavailableinAppendixB. tentlyimprovesforecastquality.
Model Training Informed by the scaling laws observed 4 Experiments
| inLLMs | (Kaplanetal.2020),wetrainedthreevariantsof |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TocomprehensivelyevaluatethecapabilitiesofKronosasa
| Kronos with | increasing parameter |     | counts, | up to | nearly 0.5 |     |     |     |     |     |     |     |
| ----------- | -------------------- | --- | ------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
foundationmodelforfinancialK-linedata,wedesignasuite
billion,toprovideatrade-offbetweenperformanceandin-
ofexperimentsspanning5representativetasks.Thesetasks
| ference budget. | The detailed | model | configurations |     | are pre- |              |             |          |             |     |         |      |
| --------------- | ------------ | ----- | -------------- | --- | -------- | ------------ | ----------- | -------- | ----------- | --- | ------- | ---- |
|                 |              |       |                |     |          | are selected | to evaluate | Kronos’s | performance |     | in both | pre- |
sentedinTable1.Consideringresourceconstraintsandprac-
|                  |            |          |     |         |         | dictive and | generative | applications, |     | thereby | demonstrating |     |
| ---------------- | ---------- | -------- | --- | ------- | ------- | ----------- | ---------- | ------------- | --- | ------- | ------------- | --- |
| tical deployment | scenarios, | we limit | the | maximum | context |             |            |               |     |         |               |     |
itsversatilityinpracticalquantitativefinancescenarios.
lengthto512tokens.Nevertheless,thisdesignremainsfully
| compatible | with arbitrary | forecasting | horizons |     | by leverag- |     |     |     |     |     |     |     |
| ---------- | -------------- | ----------- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
ExperimentalSetup
| ing K-line | data at varying     | frequencies; | for | instance, | using    |                  |     |            |            |              |     |        |
| ---------- | ------------------- | ------------ | --- | --------- | -------- | ---------------- | --- | ---------- | ---------- | ------------ | --- | ------ |
|            |                     |              |     |           |          | The experimental |     | tasks span | predictive | applications |     | (price |
| 1-minute   | data for short-term | forecasting  |     | and daily | data for |                  |     |            |            |              |     |        |
series,returnandrealizedvolatilityforecasting),generative
weeklyormonthlypredictions.Completetrainingdetailsare
capabilities(syntheticK-linegeneration),andaninvestment
providedinAppendixC.
simulationtogaugereal-worldapplicability.
Inference Atinferencetime,wegeneratefuturetokense- Forarigorouscomparison,webenchmarkKronosagainst
quencesautoregressively,analogoustotextgeneration.The a comprehensive suite of 25 baseline models. These base-

|       |                 |     |     |                   |     |     | PriceSeriesForecasting |           |     | ReturnForecasting |           |     | VolatilityForecasting |       |
| ----- | --------------- | --- | --- | ----------------- | --- | --- | ---------------------- | --------- | --- | ----------------- | --------- | --- | --------------------- | ----- |
| Model | PredictionSpace |     |     | TrainingObjective |     |     |                        |           |     |                   |           |     |                       |       |
|       |                 |     |     |                   |     |     | IC(↑)                  | RankIC(↑) |     | IC(↑)             | RankIC(↑) |     | MAE(↓)                | R2(↑) |
Direct-AR Continuous MeanSquaredError(MSE) 0.0212 0.0149 0.0416 0.0399 0.0565 0.1608
Prob-AR Continuous NegativeLog-Likelihood(NLL) 0.0179 0.0102 0.0356 0.0329 0.0464 0.1383
Kronos-Parallel Discrete Cross-Entropy 0.0345 0.0226 0.0529 0.0505 0.0461 0.1784
Kronossmall Discrete Cross-Entropy 0.0431 0.0254 0.0665 0.0622 0.0384 0.2490
Table 2: Ablation study dissecting the architectural choices of Kronos. We compare our model against variants targeting dif-
ferent Prediction Spaces (continuous vs. discrete) with corresponding Training Objectives. Direct-AR serves as a standard
regressionbaseline.Prob-ARevaluatesthebenefitofprobabilisticmodelinginthecontinuousspace.Kronos-Parallelablates
oursequentialsubtokendesignbypredictingsubtokensconcurrently.Bestresultsareinbold.
10 K r o n o s s mall K r o n o s b ase K r o n o s l arge 10 D i f f u s i o nTS T i m e V A E T i m e G A N
O r ig i n a l 10 O r ig i n a l 10 O r ig i n a l O r i g i n a l 10 O r ig in a l 10 O r ig in a l
| 5   |     | 5   |     |     | 5   |     |     | 5   |     | 5   |     |     | 5   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   |     | 0   |     |     | 0   |     |     | 0   |     | 0   |     |     | 0   |     |
|     |     | 5   |     |     | 5   |     |     |     |     | 5   |     |     | 5   |     |
| 5   |     |     |     |     |     |     |     | 5   |     |     |     |     |     |     |
10
|     |     | 10  |     |     |     |     |     | 10  |     | 10  |     |     | 10  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10
10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10
| 2.00 |          | 2.00 |     |          | 2.00 |     |          |     |          | 2.00 |     |          | 2.00 |          |
| ---- | -------- | ---- | --- | -------- | ---- | --- | -------- | --- | -------- | ---- | --- | -------- | ---- | -------- |
|      | Original |      |     | Original |      |     | Original | 3.5 | Original |      |     | Original |      | Original |
etamitsE ytisneD ataD 1.75 Kronossmall etamitsE ytisneD ataD 1.75 Kronosbase etamitsE ytisneD ataD 1.75 Kronoslarge etamitsE ytisneD ataD 3.0 DiffusionTS etamitsE ytisneD ataD 1.75 TimeVAE etamitsE ytisneD ataD 1.75 TimeGAN
| 1.50 |     | 1.50 |     |     | 1.50 |     |     |     |     | 1.50 |     |     | 1.50 |     |
| ---- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- |
2.5
| 1.25 |     | 1.25 |     |     | 1.25 |     |     |     |     | 1.25 |     |     | 1.25 |     |
| ---- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- |
| 1.00 |     | 1.00 |     |     | 1.00 |     |     | 2.0 |     | 1.00 |     |     | 1.00 |     |
1.5
| 0.75 |     | 0.75 |     |     | 0.75 |     |     |     |     | 0.75 |     |     | 0.75 |     |
| ---- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- |
| 0.50 |     | 0.50 |     |     | 0.50 |     |     | 1.0 |     | 0.50 |     |     | 0.50 |     |
| 0.25 |     | 0.25 |     |     | 0.25 |     |     | 0.5 |     | 0.25 |     |     | 0.25 |     |
| 0.00 |     | 0.00 |     |     | 0.00 |     |     | 0.0 |     | 0.00 |     |     | 0.00 |     |
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0
Data Value Data Value Data Value Data Value Data Value Data Value
Figure5:VisualcomparisonofgenerativemodelsonthedatasetofShanghaiStockExchange,15-minutefrequency.Toprow:
t-SNE embeddings of original (red) versus synthetic (blue) data. Bottom row: Kernel Density Estimates (KDE) of original
versussyntheticdata.
lines are carefully selected to represent the state-of-the- covertherealdata’sdistribution—weusetwovisualmeth-
art across four distinct paradigms: non-pre-trained full- ods: projecting original and synthetic data into a 2D space
shot models (e.g., iTransformer (Liu et al. 2023)), zero- using t-SNE, and comparing their distributions via kernel
shot time series foundation models (e.g., TimeMOE (Xi- density estimation (KDE). As shown in Figure 5 and Ap-
aoming et al. 2025)), econometric volatility models (e.g., pendixF,thet-SNEplotsshowthatKronos’ssyntheticdata
GARCH(Bollerslev1986),classicalapproachesforvolatil- better overlaps the original data space, and the KDE plots
itypredictionfromeconometrics),andgenerativetimeseries confirmahighersimilarityindistributions.
models(e.g.,DiffusionTS(YuanandQiao2024)).Taskde- Forquantitativeevaluation,weassessfidelity(i.e.,datare-
tails and baselines are in Appendix D. An overview of our alism) using the discriminative score, which measures how
| main experimental |     | results | is presented |     | in Figure | 4, with | a   |           |           |              |     |             |         |          |
| ----------------- | --- | ------- | ------------ | --- | --------- | ------- | --- | --------- | --------- | ------------ | --- | ----------- | ------- | -------- |
|                   |     |         |              |     |           |         |     | difficult | it is for | a classifier | to  | distinguish | between | original |
completeresultsbreakdowninAppendixF. andsyntheticsamples.Wealsoevaluateusefulness(thesyn-
|     |     |     |     |     |     |     |     | thetic data’s | effectiveness |     | for | training | downstream | models) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------- | --- | --- | -------- | ---------- | ------- |
MainResults via the Train-on-Synthetic, Test-on-Real (TSTR) protocol,
|                 |     |                                      |     |     |     |     |     | where a | forecasting | model | is  | trained | on synthetic | data and |
| --------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | ------- | ----------- | ----- | --- | ------- | ------------ | -------- |
| PredictionTasks |     | Figure4(a-c)presentstheresultsforthe |     |     |     |     |     |         |             |       |     |         |              |          |
three forecasting tasks. Kronos achieves consistent state- itsresultingICandRankICareevaluatedonatestsetcom-
of-the-art performance across all of them. In particular, for posedofrealdata.AsshowninFigure4(d),Kronosachieves
thebestperformanceinbothfidelityandusefulness.Thissu-
priceseriesforecasting,Kronosachievesaremarkable93%
periorityisalsoenhancedasthemodelsizescales.
| improvement         | in RankIC |          | compared  | to   | the strongest        | TSFM        |     |            |            |     |     |          |          |         |
| ------------------- | --------- | -------- | --------- | ---- | -------------------- | ----------- | --- | ---------- | ---------- | --- | --- | -------- | -------- | ------- |
| baseline,           | and an    | 87% gain | over      | the  | best non-pre-trained |             |     |            |            |     |     |          |          |         |
|                     |           |          |           |      |                      |             |     | Investment | Simulation |     | To  | validate | Kronos’s | perfor- |
| model. Furthermore, |           | as       | the model | size | scales               | up, perfor- |     |            |            |     |     |          |          |         |
manceinarealisticinvestmentscenario,wesimulatealong-
manceonthesetasksconsistentlyimproves,empiricallyval-
idating the scaling laws for time series foundation mod- onlyinvestmentstrategyontheChineseA-sharesmarketby
constructingportfolioswiththetop-kstocksrankedbyeach
els(Yaoetal.2024).
model’spredictivesignals.AsshowninFigure4(e),Kronos
GenerativeTasks Followingestablishedpractices(Yoon, outperforms all other baselines, achieving the highest An-
Jarrett,andVanderSchaar2019),weevaluatethequalityof nualizedExcessReturn(AER)andInformationRatio(IR).
syntheticdatafromthreeperspectives:diversity,fidelity,and Thisdemonstratesthatthemodelcaneffectivelytranslateits
usefulness.Toassessdiversity—howwellgeneratedsamples superiorpredictiveaccuracyintotangibleinvestmentgains.

Reconstruction Performance Price Series Forecasting Price Series Forecasting
0.083 MAE () 0.024 IC () 0.050
MSE () RankIC () IC
0.082 0.023 0.040 0.045 RankIC
0.040
0.081 0.022 0.035
0.035
0.080 Best Baseline (IC): 0.0317
0.021 0.030 0.030
0.079
0.025
0.078 0.020 0.025
0.020
0.077 0.019
14 15 16 17 18 19 20 14 15 16 17 18 19 20 0.015 Best Baseline (RankIC): 0.0138
Vocabulary Size (2k) Vocabulary Size (2k)
0.010
Return Forecasting Realized Volatility Forecasting Return Forecasting
IC () 0.045 MAE () 0.25 0.075
0.0650 RankIC () 0.044 R² () 0.24 0.070 I R C ankIC
0.0625 0.043
0.0600 0.042 0.23 0.065
0.0575 0.041 0.22 0.060
0.0550 0.040 0.21 0.055 Best Baseline (RankIC): 0.0533
0.0525 0.039 0.20 0.050 Best Baseline (IC): 0.0495
0.0500
14 15 16 17 18 19 20 14 15 16 17 18 19 20 0.045
Vocabulary Size (2k) Vocabulary Size (2k)
0.040
1 5 10 20
Figure6:Impactofvocabularysizeonmodelperformance. Number of Inference Samples (N, log scale)
We plot reconstruction quality and downstream forecasting
Figure7:Impactofthenumberofinferencesamples(N)on
performanceasvocabularysizeincreases.
forecasting performance.The lines represent the mean per-
formanceover5runswithdifferentrandomseeds,whilethe
shadedareasindicatethestandarddeviation.
AblationStudy
Test-TimeScaling
We conduct ablation studies to validate our core design
choices, focusing on two questions: (Q1) the effectiveness Anotableadvantageofourprobabilistic,generativeframe-
of our modeling paradigm compared to other alternatives, work is the ability to enhance predictive accuracy at in-
and(Q2)theimpactofvocabularysize.Anadditionalabla- ference time without retraining the model. By leveraging
tiononthetokenizerisprovidedinAppendixE. stochastic sampling, Kronos can generate multiple distinct
futuretrajectoriesfromthesamecontext.Weinvestigatethe
AnalysisofModelingParadigms.ToaddressQ1,wecom-
effectofensemblingthesepredictionsbyaveragingtheout-
pare Kronos against variants that differ in their prediction
comes from an increasing number of sampled paths. Fig-
spaces and objectives, while maintaining comparable pa-
ure 7 presents the performance on forecasting tasks as a
rametercounts.(Table2).Detaileddescriptionsofthesear-
functionofthenumberofsamples.Theresultsdemonstrate
chitecturalvariantsareprovidedinAppendixD.Wetesttwo
a consistent improvement in both IC and RankIC as more
continuous-space models: Direct-AR (a regression baseline
samples are included in the ensemble. Averaging across
withMSE)and Prob-AR.Following established work(Yao
multiple paths mitigates the stochasticity inherent in the
et al. 2024), Prob-AR uses a Student-t mixture distribu-
generation process and reduces prediction variance, yield-
tiontobettermodelheavy-taileddatadistributions.There-
ingamorerobustandstableestimate.Thiscapabilityoffers
sultsshowthatourdiscrete-spacemodelsmarkedlyoutper-
atrade-off,allowingpractitionerstobalancecomputational
formthesecontinuousalternatives.WealsofindthatKronos-
costatinferencewithdesiredlevelsofpredictiveaccuracy.
Parallel,avariantthatpredictssubtokensconcurrently,per-
forms worse than our sequential approach, demonstrating
the importance of modeling subtoken dependencies. These 5 Conclusion
findings validate our discrete, sequential modeling frame-
In this work, we introduce Kronos, a foundation model
workasamoreeffectiveapproachforthisdomain.
specificallydesignedforfinancialK-linesequences.Kronos
Impact of Vocabulary Size. To answer Q2, we investigate employs a novel two-stage framework, where an instance-
how vocabulary size affects model performance. As shown basedtokenizerfirstdiscretizescontinuousmarketdatainto
inFigure6,increasingthevocabularysizeimprovesbothre- hierarchical coarse-to-fine tokens, which are then modeled
construction quality and forecasting accuracy. A larger vo- by a large autoregressive Transformer. Comprehensive em-
cabulary provides a finer-grained representation, reducing piricalevaluationsdemonstratethatKronosestablishesnew
quantizationerror.Crucially,thisenhancedrepresentational state-of-the-art benchmarks in price series forecasting, as
precisiontranslatestobetterpredictiveoutcomes.Thisfind- well as in other relevant applications such as synthetic K-
ingalignswithobservationsinvideogeneration,wherefor line generation and volatility forecasting, significantly out-
quantization techniques like LFQ and BSQ, larger vocabu- performing existing TSFMs and other baselines. These re-
larieshavebeenshowntoleadtoimprovedgenerationqual- sults position Kronos as a robust and versatile foundation
ity(Zhao,Xiong,andKra¨henbu¨hl2024;Yuetal.2023). forarangeofapplicationsinquantitativefinance.

References Kaplan, J.; McCandlish, S.; Henighan, T.; Brown, T. B.;
|         |            |              |     |        |             |     | Chess, B.; | Child, R.; | Gray, | S.; Radford, |     | A.; Wu, | J.; and |
| ------- | ---------- | ------------ | --- | ------ | ----------- | --- | ---------- | ---------- | ----- | ------------ | --- | ------- | ------- |
| Achiam, | J.; Adler, | S.; Agarwal, | S.; | Ahmad, | L.; Akkaya, | I.; |            |            |       |              |     |         |         |
Aleman, F. L.; Almeida, D.; Altenschmidt, J.; Altman, S.; Amodei, D. 2020. Scaling laws for neural language mod-
Anadkat, S.; et al. 2023. Gpt-4 technical report. arXiv els. arXivpreprintarXiv:2001.08361.
preprintarXiv:2303.08774.
|     |     |     |     |     |     |     | Kim, O.; | and Verrecchia, | R.  | E. 1991. | Trading | volume | and |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | -------- | ------- | ------ | --- |
Ansari,A.F.;Stella,L.;Turkmen,C.;Zhang,X.;Mercado, price reactions to public announcements. Journal of ac-
P.;Shen,H.;Shchur,O.;Rangapuram,S.S.;Arango,S.P.; countingresearch,29(2):302–321.
| Kapoor,S.;etal.2024. |     | Chronos:Learningthelanguageof |     |     |     |     |           |             |           |     |      |              |     |
| -------------------- | --- | ----------------------------- | --- | --- | --- | --- | --------- | ----------- | --------- | --- | ---- | ------------ | --- |
|                      |     |                               |     |     |     |     | Kirillov, | A.; Mintun, | E.; Ravi, | N.; | Mao, | H.; Rolland, | C.; |
timeseries. arXivpreprintarXiv:2403.07815. Gustafson, L.; Xiao, T.; Whitehead, S.; Berg, A. C.; Lo,
Baidya, R.; and Lee, S.-W. 2024. Addressing the Non- W.-Y.; et al. 2023. Segment anything. In Proceedings of
StationarityandComplexityofTimeSeriesDataforLong- theIEEE/CVFinternationalconferenceoncomputervision,
| TermForecasts. |     | AppliedSciences,14(11):4436. |     |     |     |     | 4015–4026. |     |     |     |     |     |     |
| -------------- | --- | ---------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Baker,M.;andWurgler,J.2006. Investorsentimentandthe Kohli,R.K.;andKohers,T.1992. Theweek-of-the-month
cross-sectionofstockreturns.ThejournalofFinance,61(4):
effectinstockreturns:TheevidencefromtheS&Pcompos-
1645–1680. iteindex.Journalofeconomicsandfinance,16(2):129–137.
| Bollerslev,T.1986.  |     | Generalizedautoregressiveconditional |                  |     |        |      |              |                                       |            |     |        |         |          |
| ------------------- | --- | ------------------------------------ | ---------------- | --- | ------ | ---- | ------------ | ------------------------------------- | ---------- | --- | ------ | ------- | -------- |
|                     |     |                                      |                  |     |        |      | Li, J.; Liu, | Y.; Liu,                              | W.; Fang,  | S.; | Wang,  | L.; Xu, | C.; and  |
| heteroskedasticity. |     | Journal                              | of econometrics, |     | 31(3): | 307– |              |                                       |            |     |        |         |          |
|                     |     |                                      |                  |     |        |      | Bian,J.2024. | MarS:aFinancialMarketSimulationEngine |            |     |        |         |          |
| 327.                |     |                                      |                  |     |        |      | Powered      | by Generative                         | Foundation |     | Model. | arXiv   | preprint |
Brown,T.;Mann,B.;Ryder,N.;Subbiah,M.;Kaplan,J.D.; arXiv:2409.07486.
Dhariwal,P.;Neelakantan,A.;Shyam,P.;Sastry,G.;Askell,
|     |     |     |     |     |     |     | Liu, Y.; | Hu, T.; Zhang, | H.; | Wu, | H.; Wang, | S.; | Ma, L.; |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | --- | --------- | --- | ------- |
A.;etal.2020. Languagemodelsarefew-shotlearners. Ad- and Long, M. 2023. itransformer: Inverted transformers
vancesinneuralinformationprocessingsystems,33:1877– are effective for time series forecasting. arXiv preprint
| 1901. |     |     |     |     |     |     | arXiv:2310.06625. |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
Brownlees,C.T.;andGallo,G.M.2006. Financialecono- Liu, Y.; Qin, G.; Shi, Z.; Chen, Z.; Yang, C.; Huang, X.;
metricanalysisatultra-highfrequency:Datahandlingcon-
|        |               |            |     |        |           |        | Wang,J.;andLong,M.2025. |             |            | Sundial:AFamilyofHighly |     |       |          |
| ------ | ------------- | ---------- | --- | ------ | --------- | ------ | ----------------------- | ----------- | ---------- | ----------------------- | --- | ----- | -------- |
| cerns. | Computational | statistics |     | & data | analysis, | 51(4): |                         |             |            |                         |     |       |          |
|        |               |            |     |        |           |        | Capable                 | Time Series | Foundation | Models.                 |     | arXiv | preprint |
2232–2245.
arXiv:2502.00816.
| Da,Z.;Engelberg,J.;andGao,P.2011. |     |     |     | Insearchofatten- |     |     |          |               |     |           |     |       |      |
| --------------------------------- | --- | --- | --- | ---------------- | --- | --- | -------- | ------------- | --- | --------- | --- | ----- | ---- |
|                                   |     |     |     |                  |     |     | Liu, Y.; | Wu, H.; Wang, | J.; | and Long, | M.  | 2022. | Non- |
tion. Thejournaloffinance,66(5):1461–1499.
|     |     |     |     |     |     |     | stationary | transformers: | Exploring |     | the stationarity |     | in time |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --------- | --- | ---------------- | --- | ------- |
Das,A.;Kong,W.;Sen,R.;andZhou,Y.2024. Adecoder- seriesforecasting. Advancesinneuralinformationprocess-
onlyfoundationmodelfortime-seriesforecasting. InForty- ingsystems,35:9881–9893.
firstInternationalConferenceonMachineLearning.
|     |     |     |     |     |     |     | Liu, Y.; | Zhang, H.; Li, | C.; | Huang, | X.; Wang, | J.; and | Long, |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------ | --------- | ------- | ----- |
Desai, A.; Freeman, C.; Wang, Z.; and Beaver, I. 2021. M. 2024. Timer: Generative pre-trained transformers are
Timevae: A variational auto-encoder for multivariate time largetimeseriesmodels. arXivpreprintarXiv:2402.02368.
| seriesgeneration. |     | arXivpreprintarXiv:2111.08095. |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Loshchilov,I.;andHutter,F.2017.Decoupledweightdecay
Ding,X.;Mittal,A.;andGopal,A.2025. DELPHYNE:A regularization. arXivpreprintarXiv:1711.05101.
| Pre-Trained | Model | for General | and | Financial | Time | Series. |                          |     |     |                             |     |     |     |
| ----------- | ----- | ----------- | --- | --------- | ---- | ------- | ------------------------ | --- | --- | --------------------------- | --- | --- | --- |
|             |       |             |     |           |      |         | Mandelbrot,B.;etal.1963. |     |     | Thevariationofcertainspecu- |     |     |     |
arXivpreprintarXiv:2506.06288.
|                 |     |                                        |     |     |     |     | lativeprices. | Journalofbusiness,36(4):394. |     |               |     |          |     |
| --------------- | --- | -------------------------------------- | --- | --- | --- | --- | ------------- | ---------------------------- | --- | ------------- | --- | -------- | --- |
| Engle,R.F.1982. |     | Autoregressiveconditionalheteroscedas- |     |     |     |     |               |                              |     |               |     |          |     |
|                 |     |                                        |     |     |     |     | McKibbin,     | W.; Noland,                  | M.; | and Shuetrim, |     | G. 2025. | The |
ticitywithestimatesofthevarianceofUnitedKingdomin-
|           |               |                     |     |                 |       |          | globaleconomiceffectsofTrump’s2025tariffs.         |            |               |     |         | Technical   |     |
| --------- | ------------- | ------------------- | --- | --------------- | ----- | -------- | -------------------------------------------------- | ---------- | ------------- | --- | ------- | ----------- | --- |
| flation.  | Econometrica: | Journal             | of  | the econometric |       | society, |                                                    |            |               |     |         |             |     |
| 987–1007. |               |                     |     |                 |       |          | report,PetersonInstituteforInternationalEconomics. |            |               |     |         |             |     |
|           |               |                     |     |                 |       |          | Nie, Y.;                                           | Nguyen, N. | H.; Sinthong, |     | P.; and | Kalagnanam, | J.  |
| Flannery, | M. J.;        | and Protopapadakis, |     | A. A.           | 2002. | Macroe-  |                                                    |            |               |     |         |             |     |
conomic factors do influence aggregate stock returns. The 2022. Atimeseriesisworth64words:Long-termforecast-
reviewoffinancialstudies,15(3):751–782. ingwithtransformers. arXivpreprintarXiv:2211.14730.
Gao,S.;Koker,T.;Queen,O.;Hartvigsen,T.;Tsiligkaridis, Nison, S. 2001. Japanese candlestick charting techniques:
T.;andZitnik,M.2024.Units:Buildingaunifiedtimeseries a contemporary guide to the ancient investment techniques
| model. | arXive-prints,arXiv–2403. |     |     |     |     |     | oftheFarEast. | Penguin. |     |     |     |     |     |
| ------ | ------------------------- | --- | --- | --- | --- | --- | ------------- | -------- | --- | --- | --- | --- | --- |
Garza,A.;Challu,C.;andMergenthaler-Canseco,M.2023. Ozenbas,D.;etal.2008. Intra-daytradingvolumepatterns
TimeGPT-1. arXivpreprintarXiv:2310.03589. ofequitymarkets:AstudyofUSandEuropeanstockmar-
Goswami,M.;Szafer,K.;Choudhry,A.;Cai,Y.;Li,S.;and kets.InternationalBusiness&EconomicsResearchJournal
(IBER),7(8).
| Dubrawski,A.2024. |     | Moment:Afamilyofopentime-series |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
foundationmodels. arXivpreprintarXiv:2402.03885. Podobnik, B.; Horvatic, D.; Petersen, A. M.; and Stanley,
Holtzman, A.; Buys, J.; Du, L.; Forbes, M.; and Choi, Y. H.E.2009. Cross-correlationsbetweenvolumechangeand
2019. The curious case of neural text degeneration. arXiv pricechange. ProceedingsoftheNationalAcademyofSci-
| preprintarXiv:1904.09751. |     |     |     |     |     |     | ences,106(52):22079–22084. |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |

Rabanser, S.; Januschowski, T.; Flunkert, V.; Salinas, D.; on Learning Representations. International Conference on
andGasthaus,J.2020. Theeffectivenessofdiscretizationin LearningRepresentations.
forecasting:Anempiricalstudyonneuraltimeseriesmod- Xiong, R.; Yang, Y.; He, D.; Zheng, K.; Zheng, S.; Xing,
els. arXivpreprintarXiv:2005.10111. C.; Zhang, H.; Lan, Y.; Wang, L.; and Liu, T. 2020. On
|     |     |     |     |     |     |     | layer normalization |     | in the | transformer |     | architecture. |     | In In- |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------ | ----------- | --- | ------------- | --- | ------ |
Radford,A.;Kim,J.W.;Hallacy,C.;Ramesh,A.;Goh,G.;
Agarwal, S.; Sastry, G.; Askell, A.; Mishkin, P.; Clark, J.; ternationalconferenceonmachinelearning,10524–10533.
| et al. 2021.  | Learning     | transferable | visual           | models | from       | nat- | PMLR.        |     |          |     |           |         |        |     |
| ------------- | ------------ | ------------ | ---------------- | ------ | ---------- | ---- | ------------ | --- | -------- | --- | --------- | ------- | ------ | --- |
| ural language | supervision. |              | In International |        | conference | on   |              |     |          |     |           |         |        |     |
|               |              |              |                  |        |            |      | Xu, Y.; Liu, | A.; | Hao, J.; | Li, | Z.; Meng, | S.; and | Zhang, | G.  |
machinelearning,8748–8763.PmLR.
|     |     |     |     |     |     |     | 2024. PLUTUS: |     | A Well | Pre-trained |     | Large Unified |     | Trans- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ----------- | --- | ------------- | --- | ------ |
Rasul, K.; Ashok, A.; Williams, A. R.; Khorasani, A.; formercanUnveilFinancialTimeSeriesRegularities.arXiv
Adamopoulos, G.; Bhagwatkar, R.; Bilosˇ, M.; Ghonia, H.; preprintarXiv:2408.10111.
| Hassen,N.;Schneider,A.;etal.2023. |     |     |     | Lag-llama:Towards |     |     |           |          |       |     |           |          |       |       |
| --------------------------------- | --- | --- | --- | ----------------- | --- | --- | --------- | -------- | ----- | --- | --------- | -------- | ----- | ----- |
|                                   |     |     |     |                   |     |     | Yang, X.; | Liu, W.; | Zhou, | D.; | Bian, J.; | and Liu, | T.-Y. | 2020. |
InR0-FoMo:
foundationmodelsfortimeseriesforecasting. Qlib:Anai-orientedquantitativeinvestmentplatform.arXiv
Robustness of Few-shot and Zero-shot Learning in Large preprintarXiv:2009.11189.
FoundationModels.
|     |     |     |     |     |     |     | Yao, Q.; | Yang, | C.-H. H.; | Jiang, | R.; | Liang, Y.; | Jin, M.; | and |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --------- | ------ | --- | ---------- | -------- | --- |
Shi, F.; Luo, Z.; Ge, Y.; Yang, Y.; Shan, Y.; and Wang, L. Pan,S.2024. TowardsNeuralScalingLawsforTimeSeries
2025. ScalableImageTokenizationwithIndexBackpropa- FoundationModels. arXivpreprintarXiv:2410.12360.
| gationQuantization. |     | arXiv:2412.02692. |     |     |     |     |           |          |         |     |             |     |       |       |
| ------------------- | --- | ----------------- | --- | --- | --- | --- | --------- | -------- | ------- | --- | ----------- | --- | ----- | ----- |
|                     |     |                   |     |     |     |     | Yoon, J.; | Jarrett, | D.; and | Van | der Schaar, | M.  | 2019. | Time- |
Su,J.;Ahmed,M.;Lu,Y.;Pan,S.;Bo,W.;andLiu,Y.2024. series generative adversarial networks. Advances in neural
Roformer: Enhanced transformer with rotary position em- informationprocessingsystems,32.
bedding. Neurocomputing,568:127063.
|     |     |     |     |     |     |     | Yu, L.; Lezama, |     | J.; Gundavarapu, |     | N.  | B.; Versari, | L.; | Sohn, |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------------- | --- | --- | ------------ | --- | ----- |
Talukder, S.; Yue, Y.; and Gkioxari, G. 2024. Totem: Tok- K.;Minnen,D.;Cheng,Y.;Birodkar,V.;Gupta,A.;Gu,X.;
enizedtimeseriesembeddingsforgeneraltimeseriesanal- etal.2023. LanguageModelBeatsDiffusion–Tokenizeris
ysis. arXivpreprintarXiv:2402.16412.
KeytoVisualGeneration.arXivpreprintarXiv:2310.05737.
Van Den Oord, A.; Vinyals, O.; et al. 2017. Neural dis- Yuan,X.;andQiao,Y.2024. Diffusion-ts:Interpretabledif-
crete representation learning. Advances in neural informa- arXiv preprint
|     |     |     |     |     |     |     | fusion for | general | time | series | generation. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ---- | ------ | ----------- | --- | --- | --- |
tionprocessingsystems,30.
arXiv:2403.01742.
Wang,S.;Wu,H.;Shi,X.;Hu,T.;Luo,H.;Ma,L.;Zhang, Zeng,A.;Chen,M.;Zhang,L.;andXu,Q.2023. Aretrans-
| J.Y.;andZhou,J.2024a. |     |     | Timemixer:Decomposablemul- |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
formerseffectivefortimeseriesforecasting?InProceedings
| tiscale mixing | for time | series | forecasting. |     | arXiv | preprint |     |     |     |     |     |     |     |     |
| -------------- | -------- | ------ | ------------ | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
oftheAAAIconferenceonartificialintelligence,9,11121–
arXiv:2405.14616.
11128.
| Wang, Y.; | Lin, Z.;       | Teng,    | Y.; Zhu,    | Y.; Ren, | S.;          | Feng, J.; |                              |     |                                       |     |                     |     |     |     |
| --------- | -------------- | -------- | ----------- | -------- | ------------ | --------- | ---------------------------- | --- | ------------------------------------- | --- | ------------------- | --- | --- | --- |
|           |                |          |             |          |              |           | Zhang,B.;andSennrich,R.2019. |     |                                       |     | Rootmeansquarelayer |     |     |     |
| and Liu,  | X. 2025.       | Bridging | continuous  |          | and discrete | to-       |                              |     |                                       |     |                     |     |     |     |
|           |                |          |             |          |              |           | normalization.               |     | AdvancesinNeuralInformationProcessing |     |                     |     |     |     |
| kens for  | autoregressive | visual   | generation. |          | arXiv        | preprint  | Systems,32.                  |     |                                       |     |                     |     |     |     |
arXiv:2503.16430.
|     |     |     |     |     |     |     | Zhang, L.; | and | Hua, | L. 2025. | Major | Issues | in  | High- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | -------- | ----- | ------ | --- | ----- |
Wang,Y.;Wu,H.;Dong,J.;Liu,Y.;Long,M.;andWang,J.
FrequencyFinancialDataAnalysis:ASurveyofSolutions.
2024b. Deep time series models: A comprehensive survey Mathematics,13(3):347.
| andbenchmark. | arXivpreprintarXiv:2407.13278. |     |     |     |     |     |           |        |         |               |     |          |       |     |
| ------------- | ------------------------------ | --- | --- | --- | --- | --- | --------- | ------ | ------- | ------------- | --- | -------- | ----- | --- |
|               |                                |     |     |     |     |     | Zhao, Y.; | Xiong, | Y.; and | Kra¨henbu¨hl, |     | P. 2024. | Image | and |
Wang, Y.; Wu, H.; Dong, J.; Qin, G.; Zhang, H.; Liu, Y.; videotokenizationwithbinarysphericalquantization. arXiv
Qiu,Y.;Wang,J.;andLong,M.2024c. Timexer:Empower- preprintarXiv:2406.07548.
ingtransformersfortimeseriesforecastingwithexogenous
|            |                                |     |     |     |     |     | Zhou, T.;        | Ma, Z.; | Wen,      | Q.; Wang, | X.;      | Sun, L.;   | and | Jin, R. |
| ---------- | ------------------------------ | --- | --- | --- | --- | --- | ---------------- | ------- | --------- | --------- | -------- | ---------- | --- | ------- |
| variables. | arXivpreprintarXiv:2402.19072. |     |     |     |     |     |                  |         |           |           |          |            |     |         |
|            |                                |     |     |     |     |     | 2022. Fedformer: |         | Frequency |           | enhanced | decomposed |     | trans-  |
Wheeler,A.;andVarner,J.D.2024. MarketGPT:Develop- former for long-term series forecasting. In International
ingaPre-trainedtransformer(GPT)forModelingFinancial conferenceonmachinelearning,27268–27286.PMLR.
| TimeSeries. | arXivpreprintarXiv:2411.16585. |     |     |     |     |     |                                   |     |     |     |     |                  |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- |
|             |                                |     |     |     |     |     | Zhu,Y.;Li,B.;Xin,Y.;andXu,L.2024. |     |     |     |     | Addressingrepre- |     |     |
Woo, G.; Liu, C.; Kumar, A.; Xiong, C.; Savarese, S.; and sentationcollapseinvectorquantizedmodelswithonelin-
Sahoo,D.2024. UnifiedTrainingofUniversalTimeSeries arXivpreprintarXiv:2411.02038.
earlayer.
| Forecasting | Transformers. |     | In International |     | Conference | on  |     |     |     |     |     |     |     |     |
| ----------- | ------------- | --- | ---------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MachineLearning,53140–53164.PMLR.
| Wu, H.;                    | Hu, T.; Liu, | Y.; Zhou,                      | H.; Wang,              | J.;      | and Long,  | M.       |     |     |     |     |     |     |     |     |
| -------------------------- | ------------ | ------------------------------ | ---------------------- | -------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2022. Timesnet:            | Temporal     |                                | 2d-variation           | modeling |            | for gen- |     |     |     |     |     |     |     |     |
| eraltimeseriesanalysis.    |              | arXivpreprintarXiv:2210.02186. |                        |          |            |          |     |     |     |     |     |     |     |     |
| Xiaoming,                  | S.; Shiyu,   | W.;                            | Yuqi, N.;              | Dianqi,  | L.; Zhou,  | Y.;      |     |     |     |     |     |     |     |     |
| Qingsong,W.;andJin,M.2025. |              |                                | Time-MoE:Billion-Scale |          |            |          |     |     |     |     |     |     |     |     |
| Time Series                | Foundation   | Models                         | with                   | Mixture  | of         | Experts. |     |     |     |     |     |     |     |     |
| In ICLR                    | 2025: The    | Thirteenth                     | International          |          | Conference |          |     |     |     |     |     |     |     |     |

OverviewofAppendix Chronos (Ansari et al. 2024)), or treating consecutive time
|     |     |     |     |     |     |     | points as | tokens | (e.g., Timer | (Liu | et al. | 2024)). Several | of  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ------------ | ---- | ------ | --------------- | --- |
Thisappendixprovidessupplementarymaterialstosupport
the main paper. We detail our data preprocessing pipeline, these models also extend to probabilistic forecasting (e.g.,
model and training configurations, experimental setups for Lag-Llama (Rasul et al. 2023), Moirai (Woo et al. 2024),
Chronos(Ansarietal.2024)andSumdial(Liuetal.2025)).
| all tasks, | and present | additional | results | including | hyperpa- |     |             |     |                    |     |                    |     |     |
| ---------- | ----------- | ---------- | ------- | --------- | -------- | --- | ----------- | --- | ------------------ | --- | ------------------ | --- | --- |
|            |             |            |         |           |          |     | However,the |     | verygeneralitythat |     | drivestheirsuccess |     | on  |
rametersensitivityanalyses,fullresulttables,andforecast-
|     |     |     |     |     |     |     | broad benchmarks |     | becomes | a limitation |     | in specialized | do- |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ------------ | --- | -------------- | --- |
ingshowcases.
|     |     |     |     |     |     |     | mains. To | provide | a concrete | comparison, |     | we summarize |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---------- | ----------- | --- | ------------ | --- |
A RelatedWork keyattributesofprominentTSFMsinTable3.Aimportant
observationfromthetableistheminusculeproportionoffi-
TimeSeriesTokenization
nancialdatawithinthepre-trainingcorporaofthesegeneral-
Therecentsuccessoflarge,token-basedmodelshasspurred purposemodels,withmostdedicatinglessthan1%oftheir
a growing interest in discretizing continuous time series. data to this domain. This data imbalance means that the
Thistokenizationprocessispivotalforadaptingsucharchi- unique structural properties, non-stationarity, and complex
tectures for time series analysis, yet dedicated research in dynamics of financial K-line sequences are largely over-
thisarearemainssparse.EarlyeffortslikeChronos(Ansari looked or averaged out during pre-training, often resulting
etal.2024)employscalinganduniformquantization,while in suboptimal performance for financial tasks. To address
TOTEM (Talukder, Yue, and Gkioxari 2024) utilizes a this fundamental gap in pre-training, we introduce Kronos,
VectorQuantizedVariationalAutoencoder(VQ-VAE)(Van a foundation model built from the ground up on a massive
Den Oord, Vinyals et al. 2017)—a seminal approach that corpuscomposedexclusivelyoffinancialK-linedata.
| maps encoder | outputs | to learned |     | discrete latent | codes—for |     |     |     |     |     |     |     |     |
| ------------ | ------- | ---------- | --- | --------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
codebook-basedtokenization.Giventhisnascentlandscape, FinancialTimeSeriesFoundationModels
wedrawinspirationfromthemorematurefieldofvisualto- The development of foundation models specifically for fi-
kenization. Beyond the foundational VQ-VAE, innovations nance time series is a nascent but rapidly growing field.
| include Lookup-Free |               | Quantization   |        | (LFQ) (Yu | et al.    | 2023), |               |     |                   |      |              |               |     |
| ------------------- | ------------- | -------------- | ------ | --------- | --------- | ------ | ------------- | --- | ----------------- | ---- | ------------ | ------------- | --- |
|                     |               |                |        |           |           |        | These efforts |     | can be divided    | into | two          | main streams. | The |
| achieving           | high-fidelity | reconstruction |        | via an    | implicit  | code-  |               |     |                   |      |              |               |     |
|                     |               |                |        |           |           |        | first focuses | on  | general financial |      | time series, | including     | K-  |
| book without        | explicit      | lookups.       | Binary | Spherical | Quantiza- |        |               |     |                   |      |              |               |     |
linedata.Forinstance,PLUTUS(Xuetal.2024)introduces
| tion (BSQ) | (Zhao, | Xiong, | and Kra¨henbu¨hl |     | 2024) advances |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------ | ---------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
aninvertibleembeddingandmulti-scaletemporalattention,
implicit codebooks using spherical projection for an expo- pre-trained on massive datasets to uncover market regular-
nentially growing vocabulary, offering bounded quantiza- ities. DELPHYNE (Ding, Mittal, and Gopal 2025) is de-
| tion error          | and improved | trainability |     | over LFQ.  | Further, | In-   |                   |     |               |     |              |          |      |
| ------------------- | ------------ | ------------ | --- | ---------- | -------- | ----- | ----------------- | --- | ------------- | --- | ------------ | -------- | ---- |
|                     |              |              |     |            |          |       | signed explicitly |     | to counteract |     | the negative | transfer | from |
| dex Backpropagation |              | Quantization |     | (IBQ) (Shi | et al.   | 2025) |                   |     |               |     |              |          |      |
non-financialdata.Whilepromising,neitheroftheseworks
| tackles codebook |     | collapse | by making | all code | entries | dif- |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | --------- | -------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
hasreleasedtheircodeormodels,precludingdirectempiri-
ferentiable,enablingstablejointoptimizationoflarge-scale cal comparison. The second stream targets order flow data,
codebooksandthevisualencoder.Whileprimarilydesigned where models like MarketGPT (Wheeler and Varner 2024)
| for visual | data, these | methods | can | also be | applied | to dis- |     |     |     |     |     |     |     |
| ---------- | ----------- | ------- | --- | ------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
andMarS(Lietal.2024)actasgenerativeenginesforreal-
cretizegeneralmultivariatetimeseries.
isticmarketsimulation.Thesepioneeringeffortsvalidatethe
valueofdomain-specificpre-training.However,K-linedata
General-PurposeTimeSeriesFoundationModels
possessesbroaderapplicabilitythanorderflow,asitisread-
The paradigm of time series analysis has recently been re- ilyavailableacrossallmarketsandsuitablefordiversetime
shapedbyTimeSeriesFoundationModels(TSFMs),draw-
horizonswhereorderflowdataisofteninaccessible.Despite
inginspirationfromthesuccessofLargeLanguageModels its central importance, a versatile and open-source founda-
inleveragingmassivepre-trainedTransformers.Thesemod- tion model for K-line analysis remains a notable gap. We
els are trained on vast, multi-domain corpora—some with introduceKronostofillthisvoid,offeringaunified,scalable
over a hundred billion data points—to achieve remarkable frameworkdesignedspecificallyforfinancialK-linedata.
| zero-shot | or few-shot | performance |     | on general | forecasting |     |     |     |     |     |     |     |     |
| --------- | ----------- | ----------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
benchmarks.Thisversatilityisenabledbydiversearchitec- B DatasetDetails
| tures, including | decoder-only |     | models | like Lag-Llama |     | (Ra- |     |     |     |     |     |     |     |
| ---------------- | ------------ | --- | ------ | -------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
DataPreprocessingandCleaning
| sul et al. | 2023), | TimesFM | (Das | et al. 2024), | Timer | (Liu |     |     |     |     |     |     |     |
| ---------- | ------ | ------- | ---- | ------------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
et al. 2024), Time-MoE (Xiaoming et al. 2025), and Sum- Thissectiondetailsthepreprocessingandcleaningpipeline
dial (Liu et al. 2025); encoder-only frameworks like MO- applied to the large-scale K-line dataset used for pre-
MENT (Goswami et al. 2024) and Moirai (Woo et al. training.Thedatasetisaggregatedfromover40exchanges
2024);encoder-decoderstructuressuchasTimeGPT(Garza, across more than 30 countries, comprising a diverse range
Challu,andMergenthaler-Canseco2023);andmodelswith of asset classes at multiple temporal frequencies (1-minute
modified Transformer blocks for multi-task learning like to weekly). A statistical overview is provided in Table 13.
UniTS (Gao et al. 2024). At the input level, they employ The integrity of large-scale pre-training is contingent upon
generic representations such as direct value patching (e.g., high-qualityinputdata.RawK-lineseries,however,arefre-
TimesFM (Das et al. 2024), MOMENT (Goswami et al. quently contaminated by artifacts stemming from low liq-
2024)), value quantization into a fixed vocabulary (e.g., uidity, price limits, or data feed errors. To mitigate the im-

Model Architecture Tokenization Probabilistic FinancialDataRatio(Est.) PrimaryDomain
Kronos(Ours) Decoder-only Discrete(BSQ) Yes 100% FinancialK-lines
Sundial(Liuetal.2025) Decoder-only Continuous Yes 1.02% General
Time-MoE(Xiaomingetal.2025) Decoder-only Continuous No <0.01% General
Moirai(Wooetal.2024) Encoder-only Continuous Yes 0.10% General
MOMENT(Goswamietal.2024) Encoder-only Continuous No 1.60% General
Chronos(Ansarietal.2024) Encoder-Decoder Discrete(Quantization) Yes 0.45% General
| Timer(Liuetal.2024) |     |     | Decoder-only |     | Continuous |     |     | No  |     |     | 0.03% | General |     |
| ------------------- | --- | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | ----- | ------- | --- |
TimesFM(Dasetal.2024) Decoder-only Continuous No <0.01% General
UniTS(Gaoetal.2024) Encoder-only Continuous No Unknown General
Lag-Llama(Rasuletal.2023) Decoder-only Continuous Yes 0.01% General
Table3:Comparisonoftimeseriesfoundationmodels.Thetablehighlightsarchitecturalchoices,tokenizationmethods,prob-
abilisticforecastingcapabilities,andtheestimatedproportionoffinancialdataintheirpre-trainingcorpora.
Algorithm1:Low-QualitySegmentFilteringPipeline
Max.ConsecutiveBars
Min.Length PriceJump Input: Raw K-line series S , Parameter set Θ for a
| Frequency |        |     |           | Illiquid | Stagnant |     |     |     |     |     | raw |     |     |
| --------- | ------ | --- | --------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|           | (bars) |     | Threshold |          |          |     |     |     |     |     |     |     |     |
givenfrequency(fromTable4)
| 1min | 2048 |     | 0.10 | 15  |     | 45  |     | Output:AsetofcleanK-linesegmentsC |     |     |     |     |     |
| ---- | ---- | --- | ---- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
5min 1024 0.15 3 10 1: functionFILTERLOWQUALITYSEGMENTS(S ,Θ)
raw
10min 512 0.15 3 6 2: C ←∅ ▷Initializethesetoffinalcleansegments
1 5 m i n 5 1 2 0 . 1 5 2 5 S ←PartitionByPriceJumps(S ,Θ ) ▷
|           |       |     |         |     |     |     | 3:  |     | initial |     |     | raw | jump |
| --------- | ----- | --- | ------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | ---- |
| 2 0 m i n | 5 1 2 |     | 0 . 1 5 | 2   |     | 5   |     |     |         |     |     |     |      |
Splitbystructuralbreaks
| 30min  | 512 |     | 0.20 | 2   |     | 3   |     |                             |          |                              |          |             |          |
| ------ | --- | --- | ---- | --- | --- | --- | --- | --------------------------- | -------- | ---------------------------- | -------- | ----------- | -------- |
|        |     |     |      |     |     |     | 4:  | forallsegmentS              |          |                              | inS do   |             |          |
| 40min  | 256 |     | 0.20 | 1   |     | 3   |     |                             |          |                              | initial  |             |          |
| 60min  | 256 |     | 0.20 | 1   |     | 3   | 5:  |                             | M        | ←FlagConsecutiveIlliquid(S,Θ |          |             | )        |
|        |     |     |      |     |     |     |     |                             | illiquid |                              |          |             | illiquid |
| 2H     | 128 |     | 0.25 | 1   |     | 3   |     | ▷Identifyilliquidperiods    |          |                              |          |             |          |
| 4H     | 128 |     | 0.25 | 1   |     | 3   |     |                             | M        |                              |          |             | ←        |
|        |     |     |      |     |     |     | 6:  |                             | stagnant |                              |          |             |          |
| Daily  | 128 |     | 0.30 | 1   |     | 3   |     |                             |          |                              |          |             |          |
|        |     |     |      |     |     |     |     | FlagConsecutiveStagnant(S,Θ |          |                              | stagnant | ) ▷Identify |          |
| Weekly | 16  |     | 0.50 | 0   |     | 2   |     |                             |          |                              |          |             |          |
stagnantperiods
|     |     |     |     |     |     |     | 7:  |     | M   | ←M  | ∨M  | ▷Combine |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
Table 4: Frequency-specific parameters for the low-quality invalid illiquid stagnant
masksforallinvalidpoints
datafilteringpipeline.Thresholdsareadjustedtoreflectthe
|     |     |     |     |     |     |     |     |     | S     | ←ExtractValidSubsequences(S,M |     |     | )       |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------------------------- | --- | --- | ------- |
|     |     |     |     |     |     |     | 8:  |     | clean |                               |     |     | invalid |
distinctdynamicsofdifferenttimefrequencies.
▷Splitsegmentoninvalidboundaries
|     |     |     |     |     |     |     | 9:  |     | forallsubsequenceS |     | sub inS | clean do |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------- | -------- | --- |
|     |     |     |     |     |     |     | 10: |     | ifLength(S         |     | )≥Θ     | then     |     |
pact of such issues, we implement a rigorous, two-stage sub minlen
|     |     |     |     |     |     |     | 11: |     |     | C ←C∪{S | }   | ▷Addvalid, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ---------- | --- |
pipeline designed to process missing values and filter out sub
sufficientlylongsegment
low-qualitydatasegments.
endif
12:
Missing Value Processing We employ a field-specific 13: endfor
| strategy to                                   | handle | missing | values, | which are | typically | rep- | 14: | endfor  |     |     |     |     |     |
| --------------------------------------------- | ------ | ------- | ------- | --------- | --------- | ---- | --- | ------- | --- | --- | --- | --- | --- |
| resentedas‘NaN’(NotaNumber)or‘Inf’(Infinity). |        |         |         |           |           |      | 15: | returnC |     |     |     |     |     |
16: endfunction
| • Price Fields | (Open, |     | High, | Low, Close): | For | price- |     |     |     |     |     |     |     |
| -------------- | ------ | --- | ----- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
relatedfields,wetreatmissingvaluesashardboundaries.
InspiredbyTimeMOE(Xiaomingetal.2025),weparti-
|     |     |     |     |     |     |     | Low-Quality |     | Segment | Filtering | Beyond | addressing | dis- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | --------- | ------ | ---------- | ---- |
tionthetimeseriesintocontiguous,validsub-sequences
|         |            |     |           |       |        |          | crete | missing | values, | our | pipeline systematically | identifies |     |
| ------- | ---------- | --- | --------- | ----- | ------ | -------- | ----- | ------- | ------- | --- | ----------------------- | ---------- | --- |
| at each | occurrence | of  | a missing | price | value. | This ap- |       |         |         |     |                         |            |     |
proachensuresthateachresultingsegmentmaintainsits and removes entire segments of low-quality data. This is
internaltemporalintegritywithoutunwarrantedimputa- achieved through a multi-stage filtering process where tol-
erancethresholdsaredynamicallyadjustedaccordingtothe
tion.
|          |            |     |         |              |     |        | data’s | temporal | frequency, |     | as detailed in | Table 4. The | pro- |
| -------- | ---------- | --- | ------- | ------------ | --- | ------ | ------ | -------- | ---------- | --- | -------------- | ------------ | ---- |
| • Volume | and Amount |     | Fields: | In contrast, | for | volume |        |          |            |     |                |              |      |
cedure,formalizedinAlgorithm1,consistsofthefollowing
| and amount | fields, | which | primarily | serve | as  | auxiliary |     |     |     |     |     |     |     |
| ---------- | ------- | ----- | --------- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
steps:
| covariates, | we impute |     | missing | values with | zero. | To en- |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ------- | ----------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
hancemodelrobustnesstosparseorunavailablevolumet- • Structural Break Segmentation. The initial filtering
ricdata,weintroducearegularizationtechnique:during stagepartitionstheseriesbasedonsignificantpricedis-
training, both volume and amount are randomly set to continuities.Weidentifythesebreaksbycalculatingthe
zero for 5% of the input samples. This encourages the relativepricejumpbetweenthepreviousbar’scloseand
model to learn to make effective predictions from price thecurrentbar’sopen(|open /close t−1 −1|).Ifthisjump
t
informationalone. exceeds a frequency-specific threshold, the sequence is

split. This step effectively isolates artifacts arising from a feed-forward network dimension of 512, and 4 attention
eventssuchascontractrollovers,stocksplits,ordividend heads.Followingtheofficialopen-sourceimplementationof
distributions. BSQ,weconfigurethekeyquantizationhyperparametersas
• FilteringofIlliquidPeriods.Withineachsegmentfrom follows: a commitment weight β = 0.05, entropy penalty
thepreviousstep,wescreenforperiodsofsustainedilliq- weightsγ 0 =1.0andγ =1.1,andanoverallentropyscale
uidity. A bar is deemed illiquid if its trading volume is ζ =0.05.Thebalancinghyperparameterλforthequantiza-
zero or near-zero. If the number of consecutive illiquid tionlossinourobjectiveissetto1.Thequantizationgroup
barsexceedsafrequency-dependentthreshold,thecorre- sizeissetto5fortractableentropycomputation.
spondingperiodisflaggedasinvalid.
TransformerBlockArchitecture. Toencodethesequen-
• Filtering of Price Stagnation. We apply a similar tialnatureofthedata,weemploycausalself-attentionwith
method to filter periods of price stagnation, where the RotaryPositionEmbeddings(RoPE)(Suetal.2024),which
closingpriceremainsconstantoveranextendedduration. injects relative positional information. The attention opera-
Thisoftenindicatespotentialdatafeedissuesormarket tionisformulatedasfollows:
inactivity.Ifthelengthofastagnantstreaksurpassesits
frequency-specific tolerance, it is also flagged as an in-
(cid:18) Q′(K′)T(cid:19)
Attention(Q,K,V)=CausalMask √ V (9)
validperiod. d
k
• FinalSegmentValidation.Afterflaggingallilliquidand
where d is the dimension of the key vectors, and
stagnant periods, the initial segments are further split at k
CausalMaskpreventsattendingtofuturepositions.Thema-
theboundariesoftheseflaggedregions.Finally,onlythe
trices Q′ and K′ represent the original query and key
resulting sub-segments that meet the frequency-specific
matrices with RoPE transformations applied. Furthermore,
minimumlengthrequirement(Θ inTable4)arere-
minlen we adopt the Pre-Layer Normalization (Pre-LN) (Xiong
tainedforthefinalpre-trainingdataset.Thisensureseach
et al. 2020) to improve training stability, specifically
sampleissufficientlylongtosupportmeaningfulmodel
utilizing Root Mean Square Layer Normalization (RM-
learning.
SNorm) (Zhang and Sennrich 2019) for its computational
efficiencyandperformance.
C ImplementationDetails
Inthissection,weprovidefurtherdetailsontheimplemen- TrainingConfiguration
tationofKronos,coveringdatapreprocessing,modelarchi-
Thetraininghyperparametersarecarefullyselectedforeach
tecture,andconfigurationsfortrainingandinference.
modelsizetoensureastablepre-trainingprocess.Asmodel
scale increases, we decrease the peak learning rate and
InputPreprocessing
dropout probability while increasing the weight decay. We
Each input K-line sequence x = (x 1 ,x 2 ,...,x T ), where employtheAdamWoptimizer(LoshchilovandHutter2017)
x t ∈ RD,isnormalizedinatwo-stepprocedurebeforebe- and a cosine learning rate schedule with a linear warm-up
ingpassedtothetokenizer.First,weapplyz-scorenormal- phase. The learning rate warms up from 10% of its peak
ization independently to each of the D feature dimensions valueoverthefirst15,000trainingsteps.Table5detailsthe
(e.g., Open, High, Low, Close, Volume and Amount). Sec- specifichyperparametersettingsforeachmodelvariant.
ond,tomitigatethepotentialimpactofextremeoutlierson
training stability, the normalized values are clipped to the InferenceHyperparameters
range [−5,5]. This process ensures that all input features
The generation process at inference time is controlled by
haveaconsistentscalewhilepreservingthemodel’srobust-
temperature scaling (T) and nucleus (top-p) sampling. The
nessagainstanomalousdatapoints.
optimalchoiceofthesehyperparametersistask-dependent.
ModelArchitecture Forexample,forecastingtasksgenerallybenefitfromlower
temperatures to reduce randomness, whereas generative
Temporal Embeddings. To capture cyclical patterns in-
tasksmayrequirehighertemperaturestoincreasediversity.
herent in financial markets, such as intraday, weekly, and
Adetailedanalysisofhyperparametersensitivityisavailable
monthly seasonality (Ozenbas et al. 2008; Kohli and Ko-
inAppendixE.Theinferencehyperparametersusedforeach
hers 1992), we incorporate learnable temporal embed-
taskaredetailedinTable6.
dings. We extract five time-related features for each K-
line entry: minute-of-day, hour-of-day, day-of-week, day-
Pre-trainingDataRebalancing
of-month, and month-of-year. Each feature is mapped to a
dense vector via a dedicated embedding layer. These tem- The raw pre-training corpus exhibits a natural imbalance
poral embeddings are summed and then added to the input across asset classes, with equities being more prevalent
representation of each corresponding token, providing the thancryptocurrencies,futures,andforeignexchange(forex)
modelwithexplicittemporalcontext. assets. To prevent potential underfitting on these less-
represented classes, we apply strategic resampling to the
K-line Tokenization. The tokenizer’s autoencoder is de- trainingdata.Specifically,weincreasethesamplingweights
signedtobelightweight.Theencoderanddecodereachcon-
sistof3Transformerlayers,withamodeldimensionof256, https://github.com/zhaoyue-zephyrus/bsq-vit

Model FFNDropout ResidualDropout AttentionDropout TokenDropout LearningRate WeightDecay
|     | Kronos |     | 0.25 | 0.25 |     |     | 0.1 |     | 0.1 |     | 1×10−3 |     | 0.01 |     |
| --- | ------ | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | ------ | --- | ---- | --- |
small
|     | Kronos |     | 0.20 | 0.20 |     |     | 0.0 |     | 0.0 |     | 5×10−4 |     | 0.05 |     |
| --- | ------ | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | ------ | --- | ---- | --- |
base
|     | Kronos |     | 0.00 | 0.00 |     |     | 0.0 |     | 0.0 |     | 2×10−4 |     | 0.10 |     |
| --- | ------ | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | ------ | --- | ---- | --- |
large
Table5:HyperparameterconfigurationsfortheKronosmodelseries.AllmodelsaretrainedwiththeAdamWoptimizer.
|     |     | Task                          |     |     | Temperature(T) |     |     | Top-p | NumberofInferenceSamples(N) |     |     |     |     |     |
| --- | --- | ----------------------------- | --- | --- | -------------- | --- | --- | ----- | --------------------------- | --- | --- | --- | --- | --- |
|     |     | PriceSeriesForecasting        |     |     |                | 0.6 |     | 0.90  |                             |     | 10  |     |     |     |
|     |     | ReturnForecasting             |     |     |                | 0.6 |     | 0.90  |                             |     | 10  |     |     |     |
|     |     | RealizedVolatilityForecasting |     |     |                | 0.9 |     | 0.90  |                             |     | 1   |     |     |     |
|     |     | SyntheticK-lineGeneration     |     |     |                | 1.0 |     | 0.95  |                             |     | 1   |     |     |     |
|     |     | InvestmentSimulation          |     |     |                | 0.6 |     | 0.90  |                             |     | 10  |     |     |     |
Table 6: Inference hyperparameters for downstream tasks. T denotes the temperature for sampling, Top-p controls nucleus
sampling,andNisthenumberofinferencesamplesgeneratedforeachtestinstance.
fordatafromcrypto,futures,andforexmarkets.Thisrebal- usefulness, evaluating if synthetic data is as effective as
ancing ensures the model gains more balanced exposure to realdatafordownstreampredictivetasks(i.e.,theTrain-
thediversedynamicsacrossdifferentfinancialinstruments. on-Synthetic,Test-on-Realparadigm).
• InvestmentSimulation:Tomeasurethepracticalappli-
D ExperimentalDesignandImplementation
cabilityofthemodel’sforecasts,weperformbacktesting
Inthissection,wepresentthecomprehensiveexperimental simulations.TheperformanceisreportedusingAnnual-
izedExcessReturn(AER)andInformationRatio(IR).
designandimplementationfortheevaluationofKronos.We
beginbyoutliningthecoreevaluationtasksandtheircorre-
BaselinesandConfigurations
| sponding |     | metrics. Next, | we introduce | the | suite of | baseline |     |     |     |     |     |     |     |     |
| -------- | --- | -------------- | ------------ | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
modelsusedforcomparisonanddetailtheirspecificconfig-
|     |     |     |     |     |     |     |     | For a rigorous |     | evaluation, | we benchmark |     | Kronos | against a |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | ------------ | --- | ------ | --------- |
urations.Finally,weprovideadetailedaccountoftheimple-
|     |     |     |     |     |     |     |     | comprehensive |     | suite | of 25 baseline | models. | These | models |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | -------------- | ------- | ----- | ------ |
mentationforeachexperimentaltask,coveringthedatasets, are selected from prior works (e.g., (Xiaoming et al. 2025;
parameters,andspecificprotocolsusedinourevaluation. Wangetal.2024b;YuanandQiao2024))torepresentadi-
|     |     |     |     |     |     |     |     | verse range | of  | established | and | state-of-the-art |     | approaches |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | --- | ---------------- | --- | ---------- |
TasksandEvaluationMetrics
acrossdifferentparadigms.Theyareorganizedintofourdis-
| WeevaluateKronosonadiversesetoftasksthatarecentral |     |     |     |     |     |     |     | tinctgroups: |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
toquantitativefinance.Thetasksandtheirrespectiveevalu-
|     |     |     |     |     |     |     |     | • Full-shot | Time | Series | Models: | This | category | con- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------ | ------- | ---- | -------- | ---- |
ationmetricsareasfollows:
|     |     |     |     |     |     |     |     | sists | of modern, | non-pre-trained |     | time | series | models that |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --------------- | --- | ---- | ------ | ----------- |
• PriceSeriesForecasting:Weassessthemodel’sability are trained from scratch on the specific downstream
|     |     |     |     |     |     |     |     | task. | It includes | TimeXer | (Wang | et  | al. 2024c), | Times- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | ------- | ----- | --- | ----------- | ------ |
topredictfuturepriceseries.Performanceismeasuredby
the Information Coefficient (IC) and Rank Information Net (Wu et al. 2022), TimeMixer (Wang et al. 2024a),
Coefficient (RankIC) between the predicted and actual PatchTST(Nieetal.2022),Non-stationaryTransformer
|     | values. |     |     |     |     |     |     | (NSTransformer)(Liuetal.2022),DLinear(Zengetal. |           |     |       |               |     |         |
| --- | ------- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --------- | --- | ----- | ------------- | --- | ------- |
|     |         |     |     |     |     |     |     | 2023),                                          | FEDformer |     | (Zhou | et al. 2022), | and | iTrans- |
• ReturnForecasting:Similarly,weevaluatethemodel’s
former(Liuetal.2023).
proficiencyinforecastingassetreturns,alsousingICand
RankICasthemetricstogaugepredictiveaccuracy. • Zero-shot Time Series Models: This group com-
|     |          |            |              |     |         |         |     | prises | large-scale, |     | pre-trained | foundation |     | models de- |
| --- | -------- | ---------- | ------------ | --- | ------- | ------- | --- | ------ | ------------ | --- | ----------- | ---------- | --- | ---------- |
| •   | Realized | Volatility | Forecasting: | We  | use the | model’s |     |        |              |     |             |            |     |            |
high-frequency forecasts to estimate realized volatility. signedforgeneraltimeseriesanalysis.Thebaselinesare
|     |              |     |                   |     |           |       |     | TimeMOE | (Xiaoming |      | et al. | 2025),        | Moirai | (Woo et al. |
| --- | ------------ | --- | ----------------- | --- | --------- | ----- | --- | ------- | --------- | ---- | ------ | ------------- | ------ | ----------- |
|     | The accuracy | of  | these estimations | is  | evaluated | using |     |         |           |      |        |               |        |             |
|     |              |     |                   |     |           |       |     | 2024),  | TimesFM   | (Das | et al. | 2024), Moment |        | (Goswami    |
MeanAbsoluteError(MAE)andtheCoefficientofDe-
etal.2024),andChronos(Ansarietal.2024),whichwe
termination(R2).
evaluateinazero-shotsetting.
| •   | Synthetic | K-line | Generation: | Following | established |     |     |     |     |     |     |     |     |     |
| --- | --------- | ------ | ----------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• EconometricVolatilityModels:Forthevolatilityfore-
|     | practices | in time | series generation | (Yoon, | Jarrett, | and |     |         |       |            |             |     |             |      |
| --- | --------- | ------- | ----------------- | ------ | -------- | --- | --- | ------- | ----- | ---------- | ----------- | --- | ----------- | ---- |
|     |           |         |                   |        |          |     |     | casting | task, | we include | established |     | econometric | mod- |
VanderSchaar2019),weassessthequalityofsynthetic
K-line sequences from three perspectives: diversity, as- elsasspecializedbaselines,namelyARCH(Engle1982)
sessinghowwellthegeneratedsamplescoverthedistri- andGARCH(Bollerslev1986).
bution of the real data; fidelity, assessing whether syn- • Generative Time Series Models: For the K-line
thetic samples are indistinguishable from real data; and generation task, we compare Kronos against mod-

els representing three mainstream generative architec- forecasting.TheBICpenalizesmodelcomplexity,help-
tures: DiffusionTS (diffusion-based) (Yuan and Qiao ingtopreventoverfitting.
2024), TimeVAE (VAE-based) (Desai et al. 2021), and • GARCH: We perform a grid search over the lag orders
TimeGAN (GAN-based) (Yoon, Jarrett, and Van der forboththeautoregressiveterm(p)andthemovingaver-
|     | Schaar2019). |     |     |     |     |     |     |     | ageterm(q),withp,q |     |     | ∈{1,2,3}.SimilartoARCH,the |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | -------------------------- | --- | --- | --- |
Full-shotTimeSeriesModels.Forallnon-pre-traineddeep GARCH(p,q)modelwiththeminimumBICischosenas
learning models, we employ a composite loss function that thefinalmodelforthatseries.
| combines |     | Mean Squared |     | Error (MSE) |     | with an | Information |     |     |     |     |     |     |     |     |
| -------- | --- | ------------ | --- | ----------- | --- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Coefficient(IC)term.Wefindthisobjectiveempiricallyim- TaskImplementationDetails
Below,wedescribethespecificsetupsforeachofoureval-
| proves                                             | predictive | performance |     | on  | financial | tasks | compared |     |              |     |     |     |     |     |     |
| -------------------------------------------------- | ---------- | ----------- | --- | --- | --------- | ----- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
| tousingMSEalone,asitdirectlyrewardsthemodelforcap- |            |             |     |     |           |       |          |     | uationtasks. |     |     |     |     |     |     |
turingthedirectionalaccuracyofpricemovements.Theloss
|     |     |     |     |     |     |     |     |     | ForecastingTaskSetup |     |     | Thepre-trainingdataforKronos |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ---------------------------- | --- | --- | --- |
functionisdefinedas:
|     |     |                   |     |     |     |            |     |     | extends up                                          | to June | 2024. | Consequently, |     | our test period | for |
| --- | --- | ----------------- | --- | --- | --- | ---------- | --- | --- | --------------------------------------------------- | ------- | ----- | ------------- | --- | --------------- | --- |
|     |     | M                 | H   |     |     |            | M   |     | alltasksbeginsinJuly2024toensureastricttemporalsep- |         |       |               |     |                 |     |
|     | 1   | (cid:88) (cid:88) |     |     |     | 1 (cid:88) |     |     |                                                     |         |       |               |     |                 |     |
L= (y −yˆ )2−λ· IC(y ,yˆ ) arationbetweentrainingandevaluation.Weselectadiverse
|     | M   | ·H  | i,j | i,j |     | M   |     | i i |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i=1j=1 i=1 setofassetsandK-linefrequenciestorigorouslytestmodel
(10)
generalization.
| wherey                     | i andyˆ | i arethetrueandpredictedsequencesforthe |     |                         |     |     |     |     |        |                                     |     |     |     |     |     |
| -------------------------- | ------- | --------------------------------------- | --- | ----------------------- | --- | --- | --- | --- | ------ | ----------------------------------- | --- | --- | --- | --- | --- |
| i-thfeature,respectively,M |         |                                         |     | isthenumberoffeatures,H |     |     |     | is  |        |                                     |     |     |     |     |     |
|                            |         |                                         |     |                         |     |     |     |     | Assets | Weevaluateonthreemajorassetclasses: |     |     |     |     |     |
thepredictionhorizon,andλisabalancinghyperparameter,
|     |     |     |     |     |     |     |     |     | • Stocks: | To  | test both | in-distribution |     | and | out-of- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | --------------- | --- | --- | ------- |
setto4inourexperiments.
All models are trained with a batch size of 256 and an distributiongeneralization,weusedatafromnineglobal
Adamoptimizerwithalearningrateof5×10−4.Wetrain stockexchanges.
for a maximum of 12 epochs, employing an early stopping – In-distribution exchanges: Shanghai (XSHG), NAS-
mechanism with a patience of 3 epochs based on the val- DAQ (XNAS), Japan (XJPX), India (XNSE), Korea
idation loss. For each model, we test two sets of hyperpa- (XKRX),andHongKong(XHKG).
rameterscorrespondingtosmallerandlargermodelsizesto – Out-of-distribution exchanges: Indonesia (XIDX),
ensureafairandrobustcomparison.Theconfigurationthat
Malaysia(XKLS),andTaiwan(XTAI).
yieldsthebestperformanceonthevalidationsetisselected • Cryptocurrency:Allspottradingpairsavailableonthe
| for | final evaluation. |     | For DLinear, |     | instead | of varying |     | model |     |     |     |     |     |     |     |
| --- | ----------------- | --- | ------------ | --- | ------- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
Binanceexchange.
dimensions,weevaluatetwoconfigurationsbasedonits‘in-
|     |     |     |     |     |     |     |     |     | • Forex: | A comprehensive |     | dataset | of over | 1,000 | foreign |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ------- | ------- | ----- | ------- |
dividual’parameter:onewhereasinglelinearlayerisshared
exchangepairs.
| across | all      | variates     | (‘individual=False’) |         |          | and another |            | where |                    |     |     |               |     |               |     |
| ------ | -------- | ------------ | -------------------- | ------- | -------- | ----------- | ---------- | ----- | ------------------ | --- | --- | ------------- | --- | ------------- | --- |
|        |          |              |                      |         |          |             |            |       | For cryptocurrency |     | and | forex assets, | we  | intentionally | ex- |
| a      | separate | linear layer | is                   | trained | for each | variate     | (‘individ- |       |                    |     |     |               |     |               |     |
cludevolumeandamountfields,providingonlytheOHLC
| ual=True’). |     | The specific | hyperparameter |     |     | configurations |     | are |     |     |     |     |     |     |     |
| ----------- | --- | ------------ | -------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
priceseries.Thissetupteststhemodels’abilitytomakepre-
detailedinTable7.
dictionsbasedsolelyonpricedynamics,acommonscenario
| Model    |     |     | Layers | d       |     | d       |     | Heads | wherereliablevolumedataisunavailable. |     |     |                        |     |     |     |
| -------- | --- | --- | ------ | ------- | --- | ------- | --- | ----- | ------------------------------------- | --- | --- | ---------------------- | --- | --- | --- |
|          |     |     |        | model   |     | ff      |     |       |                                       |     |     |                        |     |     |     |
| TimeXer  |     |     | 3/5    | 128/256 |     | 256/512 |     | 4/8   |                                       |     |     |                        |     |     |     |
|          |     |     |        |         |     |         |     |       | FrequenciesandHorizons                |     |     | WetestonarangeofK-line |     |     |     |
| TimesNet |     |     | 3/5    | 128/256 |     | 256/512 |     | —     |                                       |     |     |                        |     |     |     |
frequencies,againincludingbothin-distributionandout-of-
| TimeMixer |     |     | 3/5 | 128/256 |     | 256/512 |     | 4/8 |              |           |     |                 |     |           |       |
| --------- | --- | --- | --- | ------- | --- | ------- | --- | --- | ------------ | --------- | --- | --------------- | --- | --------- | ----- |
|           |     |     |     |         |     |         |     |     | distribution | settings. | For | each frequency, |     | we define | look- |
| PatchTST  |     |     | 3/5 | 128/256 |     | 256/512 |     | 4/8 |              |           |     |                 |     |           |       |
backandforecasthorizonsthatarerelevanttopracticalap-
| NSTransformer |     |     | 2/3 | 128/256 |     | 256/512 |     | 4/8 |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
plicationsinquantitativefinance.Thesesettingsaredetailed
| FEDformer    |     |                | 2/3 | 128/256        |     | 256/512 |              | 4/8 |           |     |     |     |     |     |     |
| ------------ | --- | -------------- | --- | -------------- | --- | ------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- |
| iTransformer |     |                | 3/5 | 128/256        |     | 256/512 |              | 4/8 | inTable8. |     |     |     |     |     |     |
| Table        | 7:  | Hyperparameter |     | configurations |     | for     | the baseline |     |           |     |     |     |     |     |     |
MetricCalculationDetails
models. Values for the two evaluated sets are separated by • Price Series Forecasting: For each sample, the IC and
aslash(/).Wedetailthenumberoflayers,modeldimension RankICarecalculatedbetweenthepredictedandtruese-
| (d  | ), feed-forward |     | dimension |     | (d ), | and the | number | of  |                                                  |     |     |     |     |     |     |
| --- | --------------- | --- | --------- | --- | ----- | ------- | ------ | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|     | model           |     |           |     | ff    |         |        |     | riesforeachofthefourpricechannels(Open,High,Low, |     |     |     |     |     |     |
attentionheads.
Close).Thefinalreportedmetricsaretheaverageacross
thesefourchannels.
EconometricVolatilityModels.Forthespecializedvolatil-
|     |             |            |     |           |          |     |             |     | • Return | Forecasting: |            | We define | the       | predicted   | return rˆ |
| --- | ----------- | ---------- | --- | --------- | -------- | --- | ----------- | --- | -------- | ------------ | ---------- | --------- | --------- | ----------- | --------- |
| ity | forecasting | baselines, |     | we follow | standard |     | econometric |     |          |              |            |           |           |             |           |
|     |             |            |     |           |          |     |             |     | based    | on the       | last value | of the    | predicted | close price | se-       |
practicesformodelselection. quence pˆ and the last value of the historical close
t+H
• ARCH:Foreachtimeseries,wefitARCHmodelswith pricesequencep :
t
|     | lag orders                                        | p   | ∈ {1,2,3}. |     | The model | with | the | low- |     |     |     | pˆ t+H |     |     |      |
| --- | ------------------------------------------------- | --- | ---------- | --- | --------- | ---- | --- | ---- | --- | --- | --- | ------ | --- | --- | ---- |
|     |                                                   |     |            |     |           |      |     |      |     |     |     | rˆ=    | −1  |     | (11) |
|     | estBayesianInformationCriterion(BIC)isselectedfor |     |            |     |           |      |     |      |     |     |     | p      |     |     |      |
t

Frequency Look-backWindow ForecastHorizon • Usefulness(TSTR):Tomeasurethepracticalusefulness
|       |     |     |     |     |     |     |     | of the       | synthetic  | data,  | we adopt     | the      | Train-on-Synthetic, |            |          |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | ------ | ------------ | -------- | ------------------- | ---------- | -------- |
| 5min  |     |     | 480 |     |     | 96  |     |              |            |        |              |          |                     |            |          |
|       |     |     |     |     |     |     |     | Test-on-Real |            | (TSTR) | methodology. |          | We                  | train a    | post-hoc |
| 10min |     |     | 240 |     |     | 48  |     |              |            |        |              |          |                     |            |          |
|       |     |     |     |     |     |     |     | LSTM         | prediction | model  | to           | forecast | a future            | K-timestep |          |
| 15min |     |     | 160 |     |     | 32  |     |              |            |        |              |          |                     |            |          |
windowgivenahistoricalone.Thismodelcomprisestwo
| 20min |     |     | 120 |     |     | 24  |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
LSTMlayerswithahiddendimensionof64.Itistrained
| 40min |     |     | 90  |     |     | 24  |     |             |     |          |           |           |     |           |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | --------- | --------- | --- | --------- | --- |
|       |     |     |     |     |     |     |     | exclusively |     | on 6,000 | generated | synthetic |     | sequences | for |
1-hour 80 12 20 epochs using the Adam optimizer (learning rate =
| 2-hour |     |     | 60  |     |     | 12  |     | 0.001)andabatchsizeof64,withtheMeanSquaredEr-   |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| 4-hour |     |     | 90  |     |     | 18  |     | ror(MSE)lossastheobjectivefunction.Thelook-back |     |     |     |     |     |     |     |
Daily 40 12 and horizon windows are set to (80, 16) for 15-minute
|     |     |     |     |     |     |     |     | data | and (30, | 5) for | daily data, | respectively. |     | The | trained |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ------ | ----------- | ------------- | --- | --- | ------- |
Table 8: Look-back and forecast horizon settings for each modelisthenevaluatedontheoriginal,realtestdata.The
K-linefrequencyintheforecastingtasks. finalusefulnessscoreisreportedastheaverageInforma-
|     |     |     |     |     |     |     |     | tion | Coefficient | (IC) | and Rank | Information |     | Coefficient |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | ---- | -------- | ----------- | --- | ----------- | --- |
(RankIC)ofthepredictedpriceseries.
TheICandRankICarethencomputedbetweenthevec-
|        |           |         |     |            |     |        |         | Investment    | Simulation |        | Setup     | To        | evaluate | the           | practical |
| ------ | --------- | ------- | --- | ---------- | --- | ------ | ------- | ------------- | ---------- | ------ | --------- | --------- | -------- | ------------- | --------- |
| tor of | predicted | returns | and | the vector | of  | actual | returns |               |            |        |           |           |          |               |           |
|        |           |         |     |            |     |        |         | profitability | of         | Kronos | and other | baselines |          | in real-world |           |
forallsampleswithinagivenassetclassandfrequency.
|            |            |     |              |     |          |     |       | markets, | we conduct | an  | investment | simulation |     | on  | the Chi- |
| ---------- | ---------- | --- | ------------ | --- | -------- | --- | ----- | -------- | ---------- | --- | ---------- | ---------- | --- | --- | -------- |
| • Realized | Volatility |     | Forecasting: | We  | estimate | the | real- |          |            |     |            |            |     |     |          |
neseA-sharemarket.Forsimplicity,regardingtheZero-shot
ized volatility from a high-frequency price series. Us- TimeSeriesModels,weonlyselectthelargest-sizedmodel
ingthemodel’spredictedclosingprices{pˆ}H
|     |     |     |     |     |     | i overthe |     | fromeachfamilyforcomparison. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
i=1
| forecast | horizon, | the | realized | volatility | is  | calculated | as  |     |     |     |     |     |     |     |     |
| -------- | -------- | --- | -------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thesumofsquaredlogreturns:
|     |     |     |     |     |     |     |     | Data | Our empirical |     | analysis | utilizes | daily | market | data |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------- | --- | -------- | -------- | ----- | ------ | ---- |
H −1
|     |     | (cid:88) |         |             |     |     |      | fortheChineseA-sharemarket,sourcedfromtheQlibplat- |          |            |         |              |     |           |        |
| --- | --- | -------- | ------- | ----------- | --- | --- | ---- | -------------------------------------------------- | -------- | ---------- | ------- | ------------ | --- | --------- | ------ |
|     | σˆ2 | =        | (log(pˆ | )−log(pˆ))2 |     |     | (12) |                                                    |          |            |         |              |     |           |        |
|     |     |          |         | i+1         | i   |     |      | form (Yang                                         | et       | al. 2020), | an      | open-source  |     | framework | for    |
|     |     | i=1      |         |             |     |     |      | quantitative                                       | finance. | To         | promote | transparency |     | and       | repro- |
We then compute the Mean Absolute Error (MAE) and ducibility,weapplynoadditionalfilteringorpreprocessing
CoefficientofDetermination(R2)betweenthepredicted
tothedata,usingitinitsoriginal,unprocessedstate.Further-
andactualrealizedvolatilitiesacrossallsamples. more,weconductallbacktestingsimulationswithintheQlib
framework.Thisapproachleveragesitsintegratedbacktest-
SyntheticK-lineGenerationSetup
ingenginetoensureastandardizedandconsistentevaluation
protocolforallmodelsunderreview.
| Datasets | and   | Generation |                  | Parameters |      | We use | data |          |     |     |     |              |     |     |     |
| -------- | ----- | ---------- | ---------------- | ---------- | ---- | ------ | ---- | -------- | --- | --- | --- | ------------ | --- | --- | --- |
| from two | stock | exchanges  | (in-distribution |            | XSHG | and    | out- |          |     |     |     |              |     |     |     |
|          |       |            |                  |            |      |        |      | Strategy |     |     |     | top-k/drop-n |     |     |     |
of-distribution XTAI), as well as the cryptocurrency and We employ the portfolio con-
structionstrategy.Oneachtradingday,allstocksinthein-
| forex datasets. | We  | evaluate | generation |     | on two | frequencies: |     |     |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ---------- | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vestmentuniversearerankedbasedontheirpredictedreturn
15-minuteanddaily.Forthe15-minutefrequency,weusea
|     |     |     |     |     |     |     |     | signal. An | equal-weight |     | portfolio | is formed |     | by taking | long |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | --------- | --------- | --- | --------- | ---- |
look-backwindowof120andgenerateafuturesequenceof
|            |         |       |            |     |           |     |        | positionsinthetopk |     | stocks.Tomanageturnoverandtrad- |     |     |     |     |     |
| ---------- | ------- | ----- | ---------- | --- | --------- | --- | ------ | ------------------ | --- | ------------------------------- | --- | --- | --- | --- | --- |
| length 96. | For the | daily | frequency, | the | look-back | is  | 96 and |                    |     |                                 |     |     |     |     |     |
ingcosts,amaximumofnstocksareboughtorsolddaily,
thegenerationhorizonis35.Foreachasset-frequencypair,
andaminimumholdingperiodof5daysisenforcedforall
wegenerate6,000syntheticsequencesforevaluation.
positions.
EvaluationMetrics
|     |     |     |     |     |     |     |     | Signal | and | Backtest | The | predictive | signal | is  | formu- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------- | --- | ---------- | ------ | --- | ------ |
• DiscriminativeScore:Toassessthefidelityofthegen-
|     |     |     |     |     |     |     |     | lated as | an expected | return | derived | from | a   | multi-step | price |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------ | ------- | ---- | --- | ---------- | ----- |
erateddata,weemployapost-hocLSTM-basedclassifier forecast over a horizon of H days. This signal generation
todistinguishbetweenrealandsyntheticsequences.The
pipelineisapplieduniformlytoallmodelsunderevaluation,
classifierconsistsofasingleLSTMlayerwithahidden
|           |     |         |           |     |           |            |     | including | Kronos | and | the baselines, |     | to ensure | a fair | com- |
| --------- | --- | ------- | --------- | --- | --------- | ---------- | --- | --------- | ------ | --- | -------------- | --- | --------- | ------ | ---- |
| dimension | of  | 32. For | training, | we  | construct | a balanced |     |           |        |     |                |     |           |        |      |
parison.Foranygivenstockontradingdayt,asequenceof
datasetof6,000samples(3,000real,3,000synthetic)and
forecastedclosingpricesforthesubsequentHdays,denoted
aheld-outtestsetofthesamesizeandcomposition.The
|     |     |     |     |     |     |     |     | as{pˆ | }H ,isfirstgeneratedbytherespectivemodel.The |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
t+i i=1
model is trained for 20 epochs with a batch size of 64, H-day
|            |               |           |       |           |           |         |      | signal, which | we         | term       | the | average      |     | expected       | return |
| ---------- | ------------- | --------- | ----- | --------- | --------- | ------- | ---- | ------------- | ---------- | ---------- | --- | ------------ | --- | -------------- | ------ |
| using the  | Adam          | optimizer |       | (learning | rate =    | 0.0005) | and  |               |            |            |     |              |     |                |        |
|            |               |           |       |           |           |         |      | (R t→t+H      | ), is then | calculated |     | by comparing |     | the arithmetic |        |
| the binary | cross-entropy |           | (BCE) | loss      | function. | The     | Dis- |               |            |            |     |              |     |                |        |
meanoftheseforecastedpricestothecurrentclosingprice
criminativeScoreisdefinedastheclassificationerroron
|                                                   |     |     |     |     |     |     |     | p : |     |     |                    |     |          |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | --- | --- |
| thetestset.Ascoreapproaching0.5indicateshigherfi- |     |     |     |     |     |     |     | t   |     |     |                    |     |          |     |     |
|                                                   |     |     |     |     |     |     |     |     |     |     | (cid:16) (cid:80)H |     | (cid:17) |     |     |
|                                                   |     |     |     |     |     |     |     |     |     |     | 1                  | pˆ  | −p       |     |     |
delity,signifyingthattheclassifierstrugglestodifferen- H i=1 t+i t
|                                 |     |     |     |     |     |     |     |     | R     | =   |     |     |     |     | (13) |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | ---- |
| tiategenerateddatafromrealdata. |     |     |     |     |     |     |     |     | t→t+H |     |     | p   |     |     |      |
t

Price Series Forecasting Return Forecasting Realized Volatility Forecasting Synthetic Kline Generation
|       |     |     | 0.068 |     |          | 0.046 |       |     | 0.250 |               |     |       |
| ----- | --- | --- | ----- | --- | -------- | ----- | ----- | --- | ----- | ------------- | --- | ----- |
| 0.042 |     |     |       |     | IC ( )   |       | MAE ( | )   |       | Disc. Score ( | )   |       |
|       |     |     |       |     | RankIC ( | )     | R² (  | )   |       |               |     |       |
|       |     |     | 0.065 |     |          |       |       |     |       |               |     | 0.250 |
|       |     |     |       |     |          | 0.044 |       |     | 0.225 |               |     |       |
0.036
|     |     | IC ( | )   |     |     |     |     |     |     |     |     | 0.200 |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
0.062
| 0.030 |     | RankIC ( | )   |     |     | 0.042 |     |     | 0.200 |     |     |     |
| ----- | --- | -------- | --- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- |
0.150
0.060
| 0.024 |     |     |     |     |     | 0.040 |     |     | 0.175 |     |     |     |
| ----- | --- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- |
0.100
| 0.018 |     |     | 0.058 |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.150
0.3 0.5 0.7 0.9 1.1 0.3 0.5 0.7 0.9 1.1 0.3 0.5 0.7 0.9 1.1 0.3 0.5 0.7 0.9 1.1
(a) Temperature Sensitivity (varying T, p=0.9)
Price Series Forecasting Return Forecasting Realized Volatility Forecasting Synthetic Kline Generation
0.042
|       |     |     |       |     |     |     |     |     |       | Disc. Score ( | )   |     |
| ----- | --- | --- | ----- | --- | --- | --- | --- | --- | ----- | ------------- | --- | --- |
| 0.040 |     |     | 0.065 |     |     |     |     |     | 0.240 |               |     |     |
0.270
0.041
| 0.035 |     |     | 0.063 |     |     |     |     |     |     |     |     |     |
| ----- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.240
|       |     | IC (     | )     | IC ( )     |     | 0.040 |     |     | 0.225 |     |     |       |
| ----- | --- | -------- | ----- | ---------- | --- | ----- | --- | --- | ----- | --- | --- | ----- |
| 0.030 |     | RankIC ( | )     | RankIC ( ) |     |       |     |     |       |     |     |       |
|       |     |          | 0.062 |            |     |       |     |     |       |     |     | 0.210 |
0.039
0.210
| 0.025 |     |     | 0.060 |     |     |       |     | MAE ( | )   |     |     | 0.180 |
| ----- | --- | --- | ----- | --- | --- | ----- | --- | ----- | --- | --- | --- | ----- |
|       |     |     |       |     |     | 0.038 |     | R² (  | )   |     |     |       |
0.5 0.6 0.7 0.8 0.9 0.5 0.6 0.7 0.8 0.9 0.5 0.6 0.7 0.8 0.9 0.5 0.6 0.7 0.8 0.9
(b) Top-p Sensitivity (varying p, T=1.0)
Figure8:SensitivityanalysisofKronos’sperformanceondownstreamtaskswithrespecttoinferencesamplinghyperparame-
ters.(a)VaryingtemperatureT whilekeepingtop-p = 0.9fixed.(b)Varyingtop-pwhilekeepingtemperatureT = 1.0fixed.
Optimalvalues,indicatedbyreddashedlines,aretask-dependent,highlightingdifferentrequirementsforprecisionversusdi-
versity.
Inourexperiments,wesettheforecasthorizontoH = 10. variant targets a different modeling paradigm, allowing us
AllpriceforecastsaregeneratedusingdailyK-linedatawith to isolate the benefits of our proposed discrete, sequential
a90-daylook-backwindow.Thismethodologyisdesigned framework.Belowweprovideadetaileddescriptionofeach
| toproducearobustsignalbyaveragingtheforecastedprice |     |     |     |     |     |     | model. |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
path, thereby mitigating the influence of short-term predic- Direct-AR. This model serves as a standard autoregressive
tion noise and capturing the underlying trend more effec- forecasting baseline in the continuous space. Given a se-
tively.
|     |     |     |     |     |     |     | quence | of input features | {x  | 1 ,...,x | T }, each feature | vector |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------------- | --- | -------- | ----------------- | ------ |
RD
Backtests are performed on the constituents of the CSI x ∈ is first mapped to a higher-dimensional embed-
t
300 and CSI 800 indices. These indices are chosen as they ding via a linear projection. The sequence of embeddings
representtwokeysegmentsoftheChineseA-sharemarket: isthenprocessedbyaTransformerdecoderbackbone.The
theCSI300compriseslarge-cap,highlyliquidstocks,while modelistrainedtodirectlypredictthevalueofthenexttime
theCSI800providesbroadermarketcoveragebyincluding
|     |     |     |     |     |     |     | step,xˆ T+1 | ,fromthehistoricalcontext.Thetrainingobjec- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------------------------------- | --- | --- | --- | --- |
both large- and mid-cap stocks. This allows for a compre- tiveistominimizetheMeanSquaredError(MSE)between
hensive assessment of the model’s performance across dif- the predicted and ground-truth values. This approach rep-
ferentmarketsegments. resents the most common regression-based formulation for
timeseriesforecasting.
|            |         |        |             |                |     |     | Prob-AR. | This is        | a probabilistic | forecasting | model       | oper- |
| ---------- | ------- | ------ | ----------- | -------------- | --- | --- | -------- | -------------- | --------------- | ----------- | ----------- | ----- |
| Parameters | and     | Costs  | For the     | CSI 300 index, | we  | set |          |                |                 |             |             |       |
|            |         |        |             |                |     |     | ating in | the continuous | space.          | Following   | established | prac- |
| k = 50     | and n = | 5. For | the broader | CSI 800 index, | we  | set |          |                |                 |             |             |       |
tices(Yaoetal.2024),insteadofapointestimate,Prob-AR
| k = 200 | and n | = 10. | The relatively | large portfolio | sizes |     |          |                |     |               |              |         |
| ------- | ----- | ----- | -------------- | --------------- | ----- | --- | -------- | -------------- | --- | ------------- | ------------ | ------- |
|         |       |       |                |                 |       |     | predicts | the parameters | of  | a probability | distribution | for the |
arechosentoensurediversificationandproducemorestable
backtesting results, reducing the influence of idiosyncratic next time step. We use a mixture of four Student-t distri-
butionstomodelthepredicteddistribution.Theprobability
stockmovements.Toensurearealisticperformanceassess-
densityfunction(PDF)forarandomvariablexfollowinga
ment,aconservativetransactioncostof0.15%isappliedto
singleStudent-tdistributionis:
eachtrade.
|     |     |     |     |     |     |     |     |     |     | (cid:32) |     | (cid:33)−ν+ 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- |
DetailsofAblationStudyBaselines Γ(ν+1) 1 (cid:18) x−µ (cid:19)2 2
√2
|                                                       |     |     |     |     |     |     | p(x|ν,µ,σ)= |      |     | 1+  |     |      |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | ---- | --- | --- | --- | ---- |
|                                                       |     |     |     |     |     |     |             | Γ(ν) | πνσ |     | ν σ |      |
| ToinvestigatethearchitecturalchoicesofKronos,wedesign |     |     |     |     |     |     |             |      | 2   |     |     |      |
| threebaselinevariantsforourablationstudy(Table2).Each |     |     |     |     |     |     |             |      |     |     |     | (14) |

|     | 40%                                     | Kronossmall   |     |     |     |     |     | Kronossmall                                  |     |     |     |     |     |     |
| --- | --------------------------------------- | ------------- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |                                         | Kronosbase    |     |     |     |     |     | Kronosbase                                   |     |     |     |     |     |     |
|     |                                         | Kronoslarge   |     |     |     |     |     | 30% Kronoslarge                              |     |     |     |     |     |     |
|     | 30%                                     | TimeXer       |     |     |     |     |     | TimeXer                                      |     |     |     |     |     |     |
|     | nruteR evitalumuC                       | iTransformer  |     |     |     |     |     | nruteR evitalumuC iTransformer               |     |     |     |     |     |     |
|     |                                         | DLinear       |     |     |     |     |     | 20% DLinear                                  |     |     |     |     |     |     |
|     | 20%                                     | FEDformer     |     |     |     |     |     | FEDformer                                    |     |     |     |     |     |     |
|     |                                         | NSTransformer |     |     |     |     |     | NSTransformer                                |     |     |     |     |     |     |
|     |                                         | PatchTST      |     |     |     |     |     | PatchTST                                     |     |     |     |     |     |     |
|     | 10%                                     | TimeMixer     |     |     |     |     |     | 10% TimeMixer                                |     |     |     |     |     |     |
|     |                                         | TimesNet      |     |     |     |     |     | TimesNet                                     |     |     |     |     |     |     |
|     |                                         | Moirailarge   |     |     |     |     |     | Moirailarge                                  |     |     |     |     |     |     |
|     | 0%                                      | TimeMOEbase   |     |     |     |     |     | 0% TimeMOEbase                               |     |     |     |     |     |     |
|     |                                         | Momentlarge   |     |     |     |     |     | Momentlarge                                  |     |     |     |     |     |     |
|     |                                         | Chronoslarge  |     |     |     |     |     | Chronoslarge                                 |     |     |     |     |     |     |
|     | 10%                                     | TimesFM       |     |     |     |     |     | TimesFM                                      |     |     |     |     |     |     |
|     |                                         | CSI300 Index  |     |     |     |     |     | 10% CSI800 Index                             |     |     |     |     |     |     |
|     |                                         | Kronossmall   |     |     |     |     |     | 20.0% Kronossmall                            |     |     |     |     |     |     |
|     | )003ISC( nruteR ssecxE evitalumuC 20.0% | Kronosbase    |     |     |     |     |     | )008ISC( nruteR ssecxE evitalumuC Kronosbase |     |     |     |     |     |     |
|     |                                         | Kronoslarge   |     |     |     |     |     | Kronoslarge                                  |     |     |     |     |     |     |
|     |                                         | TimeXer       |     |     |     |     |     | 15.0% TimeXer                                |     |     |     |     |     |     |
|     | 15.0%                                   | iTransformer  |     |     |     |     |     | iTransformer                                 |     |     |     |     |     |     |
|     |                                         | DLinear       |     |     |     |     |     | DLinear                                      |     |     |     |     |     |     |
|     | 10.0%                                   | FEDformer     |     |     |     |     |     | 10.0% FEDformer                              |     |     |     |     |     |     |
|     |                                         | NSTransformer |     |     |     |     |     | NSTransformer                                |     |     |     |     |     |     |
|     |                                         | PatchTST      |     |     |     |     |     | PatchTST                                     |     |     |     |     |     |     |
|     | 5.0%                                    | TimeMixer     |     |     |     |     |     | 5.0% TimeMixer                               |     |     |     |     |     |     |
|     |                                         | TimesNet      |     |     |     |     |     | TimesNet                                     |     |     |     |     |     |     |
|     | 0.0%                                    | Moirailarge   |     |     |     |     |     | Moirailarge                                  |     |     |     |     |     |     |
|     |                                         | TimeMOEbase   |     |     |     |     |     | 0.0% TimeMOEbase                             |     |     |     |     |     |     |
|     |                                         | Momentlarge   |     |     |     |     |     | Momentlarge                                  |     |     |     |     |     |     |
|     | 5.0%                                    | Chronoslarge  |     |     |     |     |     | Chronoslarge                                 |     |     |     |     |     |     |
|     |                                         | TimesFM       |     |     |     |     |     | TimesFM                                      |     |     |     |     |     |     |
|     | 10.0%                                   |               |     |     |     |     |     | 5.0%                                         |     |     |     |     |     |     |
2024-07 2024-08 2024-10 2024-12 2025-02 2025-04 2025-06 2024-07 2024-08 2024-10 2024-12 2025-02 2025-04 2025-06
|     |     |     | (a)CSI300Index |     |     |     |     |     | (b)CSI800Index |     |     |     |     |     |
| --- | --- | --- | -------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
Figure9:Cumulativereturncurvesofbacktestusingsignalsgeneratedbydifferentmodels.
R,
where ν > 0, µ ∈ and σ > 0 are the degrees of • OperatingSystem:Ubuntu24.04.1LTS
| freedom, | location, | and             | scale parameters, |       | respectively, |          | and |            |           |        |         |     |         |        |
| -------- | --------- | --------------- | ----------------- | ----- | ------------- | -------- | --- | ---------- | --------- | ------ | ------- | --- | ------- | ------ |
|          |           |                 |                   |       |               |          |     | • Software | versions: | Python | 3.13.2, |     | PyTorch | 2.7.0, |
| Γ(·)     | is the    | gamma function. | The               | model | employs       | indepen- |     |            |           |        |         |     |         |        |
NumPy1.26.2,Pandas2.2.2,Matplotlib3.9.3,Hugging
| dent      | linear             | layers to predict       | the     | parameters |           | for each  | of the  |                      |                     |             |     |     |     |     |
| --------- | ------------------ | ----------------------- | ------- | ---------- | --------- | --------- | ------- | -------------------- | ------------------- | ----------- | --- | --- | --- | --- |
|           |                    |                         |         |            |           |           |         | FaceHub(‘huggingface |                     | hub’)1.57.4 |     |     |     |     |
| four      | components—degrees |                         | of      | freedom    | (ν k ),   | location  | (µ k ), |                      |                     |             |     |     |     |     |
| scale     | (σ ),              | and mixture             | weights | (w ).      | To ensure | parameter |         |                      |                     |             |     |     |     |     |
|           | k                  |                         |         | k          |           |           |         |                      | E AdditionalResults |             |     |     |     |     |
| validity, | a                  | softplus transformation |         | is         | applied   | to ν      | and σ   |                      |                     |             |     |     |     |     |
|           |                    |                         |         |            |           | k         | k       |                      |                     |             |     |     |     |     |
to enforce positivity, and a softmax function is applied to ImpactofInferenceSamplingHyperparameters
| the | weights | w to ensure | they | form a | valid | probability | dis- |                    |            |     |         |     |        |         |
| --- | ------- | ----------- | ---- | ------ | ----- | ----------- | ---- | ------------------ | ---------- | --- | ------- | --- | ------ | ------- |
|     |         | k           |      |        |       |             |      | The autoregressive | generation |     | process | of  | Kronos | is gov- |
tribution.ThemodelistrainedbyminimizingtheNegative erned by sampling strategies that introduce controlled
Log-Likelihood(NLL)ofthetruevalueunderthepredicted stochasticity, namely temperature scaling (T) and top-p
mixturedistribution.
|                  |     |                     |         |           |        |          |         | (nucleus)         | sampling. The | choice | of          | these | hyperparameters |           |
| ---------------- | --- | ------------------- | ------- | --------- | ------ | -------- | ------- | ----------------- | ------------- | ------ | ----------- | ----- | --------------- | --------- |
| Kronos-Parallel. |     | This                | variant | is a      | direct | ablation | of the  |                   |               |        |             |       |                 |           |
|                  |     |                     |         |           |        |          |         | can significantly | influence     | model  | performance |       | on              | different |
| sequential       |     | subtoken generation |         | mechanism |        | within   | Kronos. |                   |               |        |             |       |                 |           |
downstreamtasks.Toprovideguidanceontheiroptimalset-
Whileitsharesthesameinputquantizationanddiscretepre- tings,weconduct asensitivityanalysis.Figure8 illustrates
dictionspaceasKronos,itremovestheintra-blockmodule. theperformanceofKronosacrossourfourmaintaskswhile
After the Transformer backbone produces a context vector varyingonehyperparameterandholdingtheotherconstant.
| from | the input | history, | a single | prediction | head | is  | used to |     |     |     |     |     |     |     |
| ---- | --------- | -------- | -------- | ---------- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
AsshowninFigure8,theoptimalsamplinghyperparam-
concurrentlypredictthelogitsforbothsubtokensofthenext
etersaretask-dependent.Forforecastingtasks(priceseries
time step. The training objective is the sum of the cross- and return), which demand precision, lower temperatures
entropylossesforeachsubtoken,optimizedjointly. (e.g.,T ≈ 0.6)arepreferable.Thissharpensthenext-token
distribution,compellingthemodeltowardsmoredetermin-
ExperimentalEnvironment
|     |     |     |     |     |     |     |     | istic and high-confidence |     | predictions. |     | Conversely, |     | realized |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | ------------ | --- | ----------- | --- | -------- |
All experiments are conducted within a Kubernetes (k8s) volatilityforecastingandsyntheticK-linegenerationbenefit
cluster. For all computational tasks, we utilize three iden- fromgreaterstochasticity,achievingoptimalperformanceat
tical pods. Each pod is provisioned with a dedicated set of temperaturescloserto1.0.Ahighertemperatureencourages
resourcescomprising96CPUcores(IntelXeonGold6330 the generation of more diverse sequences, which is essen-
@2.00GHz),200GBofsystemmemory(RAM),andeight tial for capturing the probabilistic nature of volatility and
NVIDIA GeForce RTX 4090D GPUs. This configuration forproducingrealistic,non-repetitivemarketdata.
provides a total of 24 GPUs, which are collectively em- The analysis of top-p sampling reveals a similar pattern:
ployedformodeltrainingandallsubsequentevaluations. forecasting tasks favor smaller p values to restrict the sam-
Thesoftwareenvironmentiscontainerizedandstandard- pling pool, whereas generative tasks perform better with a
izedacrossallpods.Theprimarycomponentsandtheirver- larger nucleus (p ≥ 0.9) to preserve diversity. When com-
sionsaredetailedbelow: paringthetwotechniques,weobservethattemperaturescal-

ing generally offers more effective and nuanced control, CSI300Index CSI800Index Average
Model
| leading       | to slightly | better     | peak        | performance |           | across | tasks.  |         |               |        |        |        |        |
| ------------- | ----------- | ---------- | ----------- | ----------- | --------- | ------ | ------- | ------- | ------------- | ------ | ------ | ------ | ------ |
|               |             |            |             |             |           |        |         |         | AER           | IR AER | IR     | AER    | IR     |
| This suggests | that        | the global | probability |             | rescaling |        | of tem- |         |               |        |        |        |        |
|               |             |            |             |             |           |        |         | TimeXer | 0.1035 0.7988 | 0.1509 | 1.5471 | 0.1272 | 1.1730 |
peraturemaybeamoresuitabletuningmechanismthanthe TimeMixer −0.0600−0.5721 0.0705 0.8113 0.0053 0.1196
hardtruncationofnucleussampling. iTransformer −0.1202−1.4441−0.0525−0.8558−0.0864−1.1500
|     |     |     |     |     |     |     |     | PatchTST | 0.1289 0.9895 | 0.1620 | 1.5033 | 0.1455 | 1.2464 |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | ------ | ------ | ------ | ------ |
AblationonTokenizerArchitecture TimesNet 0.1441 0.6558 0.0634 0.7225 0.1038 0.6892
|     |     |     |     |     |     |     |     | DLinear | −0.0066−0.0605 | 0.1112 | 1.2003 | 0.0523 | 0.5699 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | ------ | ------ | ------ | ------ |
We perform an ablation study on the tokenizer architec- FEDformer 0.0362 0.2943 0.0539 0.5602 0.0451 0.4273
ture to justify our design choices. We compare our pro- NSTransformer−0.0343−0.2889 0.0664 0.6979 0.0161 0.2045
posedTransformer-basedtokenizerusingahierarchicalloss
|                  |               |                  |       |                   |     |     |           | Time-MOEbase | 0.0985 0.8230 | 0.1315 | 1.3726 | 0.1150 | 1.0978 |
| ---------------- | ------------- | ---------------- | ----- | ----------------- | --- | --- | --------- | ------------ | ------------- | ------ | ------ | ------ | ------ |
| against two      | alternatives: |                  | (1) a | Transformer-based |     |     | tokenizer |              |               |        |        |        |        |
|                  |               |                  |       |                   |     |     |           | Moirailarge  | 0.1470 0.9747 | 0.1683 | 1.5215 | 0.1577 | 1.2481 |
|                  |               |                  |       |                   |     |     |           | TimesFM      | 0.0788 0.7357 | 0.1355 | 1.6427 | 0.1072 | 1.1892 |
| with a standard, |               | non-hierarchical |       | reconstruction    |     |     | loss and  |              |               |        |        |        |        |
|                  |               |                  |       |                   |     |     |           | Momentlarge  | 0.1655 1.1993 | 0.1707 | 1.5361 | 0.1681 | 1.3677 |
(2)aCNN-basedarchitecturewithacomparableparameter
|     |     |     |     |     |     |     |     | Chronoslarge | −0.0659−0.7670 | 0.0056 | 0.0902−0.0302−0.3384 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | ------ | -------------------- | --- | --- |
count.Allmodelsaretrainedwithavocabularysizeof218.
|     |     |     |     |     |     |     |     | Kronossmall | 0.1805 1.2394 | 0.1772 | 1.6050 | 0.1789 | 1.4222 |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | ------ | ------ | ------ | ------ |
|     |     |     |     |     |     |     |     | Kronosbase  | 0.1911 1.3782 | 0.1867 | 1.6652 | 0.1889 | 1.5217 |
TokenizerArchitecture MAE(↓) MSE(↓) Kronoslarge 0.2193 1.4177 0.1974 1.8805 0.2084 1.6491
| Transformerw/HierarchicalLoss(Ours) |     |     |     |     | 0.0785 |     | 0.0203 |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- |
Transformerw/StandardLoss 0.0781 0.0202 Table 10: Full results of investment simulation. We re-
portAnnualizedExcessReturn(AER)andInformationRa-
| CNN-based |     |     |     |     | 0.0916 |     | 0.0251 |           |                 |      |         |            |      |
| --------- | --- | --- | --- | --- | ------ | --- | ------ | --------- | --------------- | ---- | ------- | ---------- | ---- |
|           |     |     |     |     |        |     |        | tio (IR). | Best and second | best | results | are marked | with |
redunderlineandblueunderline,respectively.
Table9:AblationstudyontheK-linetokenizerarchitecture.
| We compare    | our | proposed       | Transformer-based |                |     |       | tokenizer, |     |     |     |     |     |     |
| ------------- | --- | -------------- | ----------------- | -------------- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
| which employs |     | a hierarchical |                   | reconstruction |     | loss, | against    |     |     |     |     |     |     |
twokeyvariants:aTransformer-basedtokenizerwithastan- tiontask.Fortheforecastingtasks,wereporttheresultsfor
dardreconstructionlossandaCNN-basedarchitecture.All each asset, averaged over all tested frequencies. Tables 14
modelsaretrainedwithavocabularysizeof218.Thetable and15showtheresultsofthepriceseriesforecastingexper-
iments.Theoutcomesforreturnforecastingarepresentedin
reportsreconstructionqualitymeasuredbyMAEandMSE.
Tables16and17,whilethoseforrealizedvolatilityforecast-
|     |     |     |     |     |     |     |     | ing are in | Tables 18 and | 19. Furthermore, |     | for the | synthetic |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | ---------------- | --- | ------- | --------- |
AsshowninTable9,theresultsindicatethatTransformer-
basedarchitecturesoutperformtheCNN-basedmodelinre- K-linegenerationtask,Figures13and14providevisualiza-
tionsofthediversityofthegeneratedsequencesbydifferent
| construction | quality, | highlighting |     | the | effectiveness |     | of self- |     |     |     |     |     |     |
| ------------ | -------- | ------------ | --- | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
models.Theresultsforthediscriminativescoreandpredic-
| attention    | for capturing | dependencies |                   |     | in K-line | data.    | More      |                 |                      |     |                |           |            |
| ------------ | ------------- | ------------ | ----------------- | --- | --------- | -------- | --------- | --------------- | -------------------- | --- | -------------- | --------- | ---------- |
|              |               |              |                   |     |           |          |           | tive usefulness | are presented        | in  | Table 20       | and Table | 21, re-    |
| importantly, | our           | model        | with hierarchical |     | loss      | achieves | re-       |                 |                      |     |                |           |            |
|              |               |              |                   |     |           |          |           | spectively.     | Finally, the results | of  | the investment |           | simulation |
| construction | quality       | nearly       | identical         |     | to that   | of       | the stan- |                 |                      |     |                |           |            |
dard loss variant. This confirms that our approach suc- experimentarepresentedinTable10.
| cessfully | engineers | a coarse-to-fine |     | structure |     | within | the to- |     |     |     |     |     |     |
| --------- | --------- | ---------------- | --- | --------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- |
G ForecastShowcases
| kens—a | property | beneficial | for | the subsequent |     | autoregres- |     |     |     |     |     |     |     |
| ------ | -------- | ---------- | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
sivemodel—withoutanotabletrade-offinrepresentational Figures 15 to 19 present the forecasting results of our pro-
fidelity. posedmodel,Kronos,againstseveralbaselines.Weselecta
|     |     |     |     |     |     |     |     | few representative | assets | and showcase |     | the predictions | for |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ------ | ------------ | --- | --------------- | --- |
K-lineReconstructionVisualizations
|     |     |     |     |     |     |     |     | two key features: | closing | price and | trading | volume. | As ob- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | --------- | ------- | ------- | ------ |
Figure 10 visualizes our tokenizer’s reconstruction results served,theforecastsfromKronosnotonlyachievecompet-
onadiversesetoffinancialinstruments.Theplotsshowthat itive predictive performance but also exhibit a strong qual-
thereconstructed‘ClosePrice’and‘Volume’seriesclosely itative resemblance to the ground-truth series. Notably, our
modeladeptlycapturesthecharacteristicdynamicsandpat-
| track the | ground | truth, confirming |     | that | our | tokenizer | effec- |     |     |     |     |     |     |
| --------- | ------ | ----------------- | --- | ---- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- |
tively preserves the essential dynamics of the original con- terns of the actual price and volume sequences, producing
tinuousdatawithinitsdiscretetokenrepresentation. forecaststhatarenotonlyaccuratebutalsovisuallyplausi-
ble.
CumulativeReturnCurveVisualizations
|     |     |     |     |     |     |     |     |     | H   | Discussion |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
Figure9presentsthecumulativereturncurvesderivedfrom
backtestingusingpredictivesignalsbydifferentmodels.As HasK-linedataembeddedenoughinformationto
| illustrated, | Kronos | consistently |     | demonstrates |     | superior | per- |     |     |     |     |     |     |
| ------------ | ------ | ------------ | --- | ------------ | --- | -------- | ---- | --- | --- | --- | --- | --- | --- |
drivethepricemovementofcapitalmarketin
| formance, | achieving | the | highest | cumulative |     | returns | among |     |     |     |     |     |     |
| --------- | --------- | --- | ------- | ---------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- |
shortterm?(Q1)
theevaluatedmodels.
|     |     |     |     |     |     |     |     | In capital | markets, the determinants |     | of price | dynamics | are |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------------- | --- | -------- | -------- | --- |
conventionallybifurcatedinto:
F FullExperimentResults
Inthissection,wepresentthecompleteexperimentalresults • Long-termdrivingfactors,whichmanifestaspersistent
for three forecasting tasks and the synthetic K-line genera- trendsandexertalastinginfluenceonintrinsicvalue;

• Short-term driving factors, which are typified by ele- space,adownstreammodellikeaTransformerlearnsto
vatedvolatilityandimmediatemarketimpact. predicttransitionsandpatternsamongafinitesetofab-
|           |         |         |           |     |     |          |          | stract    | states | (tokens).    | This | simplifies | the   | learning | task.  |
| --------- | ------- | ------- | --------- | --- | --- | -------- | -------- | --------- | ------ | ------------ | ---- | ---------- | ----- | -------- | ------ |
| Long-term | driving | factors | establish |     | the | market’s | prevail- |           |        |              |      |            |       |          |        |
|           |         |         |           |     |     |          |          | Different | but    | semantically |      | similar    | input | vectors  | can be |
ingtrajectoryandvaluationbenchmarks,whereasshort-term
|     |     |     |     |     |     |     |     | mapped | to  | the same | token, | effectively |     | increasing | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------- | ------ | ----------- | --- | ---------- | --- |
onesintroducetransientvolatilityandgeneratediscretetrad-
|     |     |     |     |     |     |     |     | number | of  | observations | for | each | discrete | state. | This al- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------------ | --- | ---- | -------- | ------ | -------- |
ingopportunities.
lowsthemodeltolearnrobustpatternsfromfewerexam-
Extensiveempiricalevidencedemonstratesthatklinedata
ples,whichisparticularlycriticalformodelingraremar-
| (OHLCVA, | including |     | price | and trading |     | volume) | (Kim |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | ----- | ----------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
ketphenomenalikeresponsestoliquidityshocks,where
andVerrecchia1991),whenanalyzedintandem,effectively
dataissparse.
| encapsulate | the | informational |     | content | of  | short-term | driv- |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------- | --- | ------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
ing factors—such as macroeconomic data releases (Flan- • Reduced Overfitting: The quantization process inher-
nery and Protopapadakis 2002), corporate event disclo- ently discards fine-grained, potentially noisy variations
|     |     |     |     |     |     |     |     | within | each | quantization |     | cell. This | prevents |     | the model |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | ------------ | --- | ---------- | -------- | --- | --------- |
sures(KimandVerrecchia1991),andshiftsininvestorsen-
fromfittingtospuriousartifactsinthetrainingdata.
| timent (Baker |     | and Wurgler | 2006; | Da, | Engelberg, |     | and Gao |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | ----- | --- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
2011).
Thedetaildiscussionabouttheaboveempiricalevidences
|     |     |     |     |     |     |     |     |     | CodebookType |     |     |     | Size |     | Usage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | ---- | --- | ----- |
isbeyondthescopeofthispaper.
|                                    |     |     |     |     |     |     |     | Coarse-Level-SubtokenCodebook |     |     |     |     | 210 |     | 97.66% |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | ------ |
| WhatmakesKrono’stokenizerwork?(Q2) |     |     |     |     |     |     |     |                               |     |     |     |     | 210 |     |        |
|                                    |     |     |     |     |     |     |     | Fine-Level-SubtokenCodebook   |     |     |     |     |     |     | 85.25% |
Theeffectivenessofourvision-inspiredquantization(BSQ)
|     |     |     |     |     |     |     |     | Table 11: | Codebook | usage | for | coarse-level |     | subtoken | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----- | --- | ------------ | --- | -------- | --- |
tokenizercanbeanalyzedfromtwokeyperspectives:itsin-
fine-levelsubtoken.
herentnoisesuppressionanditsabilitytocreateastructured,
discretestatespacesuitableforsequencemodeling.
Theeffectivenessofourtokenizerisfurtherevidencedby
| Noise Suppression |     | and | Stability |     | Financial | time-series |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
itscodebookutilization.AsshowninTable11,thecodeus-
| data is | often corrupted |     | by noise | and | subject | to  | extreme |     |     |     |     |     |     |     |     |
| ------- | --------------- | --- | -------- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ageofBSQreaches97.66%atthecoarseleveland85.25%
| outliers,        | such as   | “flash-crash” |       | events               | caused | by            | anomalous |             |             |               |         |             |           |             |          |
| ---------------- | --------- | ------------- | ----- | -------------------- | ------ | ------------- | --------- | ----------- | ----------- | ------------- | ------- | ----------- | --------- | ----------- | -------- |
|                  |           |               |       |                      |        |               |           | at the fine | level.      | Such          | high    | utilization | indicates |             | that our |
| trades.          | A primary | challenge     |       | for regression-based |        |               | models    |             |             |               |         |             |           |             |          |
|                  |           |               |       |                      |        |               |           | method      | creates     | an expressive |         | vocabulary, |           | effectively | parti-   |
| is that such     | outliers  | can           | lead  | to unbounded         |        | approximation |           |             |             |               |         |             |           |             |          |
|                  |           |               |       |                      |        |               |           | tioning     | the feature | space         | without | suffering   |           | from        | codebook |
| errors, severely |           | degrading     | model | stability            |        | (Brownlees    | and       |             |             |               |         |             |           |             |          |
|                  |           |               |       |                      |        |               |           | collapse    | (where      | many          | codes   | are left    | unused)   | (Zhu        | et al.   |
Gallo2006).
2024).Thisexpressivenessprovidestherichfoundationnec-
| Our approach |     | addresses | this | by  | transforming |     | the rep- |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ---- | --- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
essaryforamodeltocapturethenuancedanddiversestates
| resentation | learning | into | a more | robust, | classification-like |     |     |     |     |     |     |     |     |     |     |
| ----------- | -------- | ---- | ------ | ------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofmarketmicrostructure.
framework.Byquantizingcontinuousprice-volumeembed-
|           |             |     |     |           |     |            |      | Additionally, |       | the vocabulary |            | is stratified |                     | into | three cat- |
| --------- | ----------- | --- | --- | --------- | --- | ---------- | ---- | ------------- | ----- | -------------- | ---------- | ------------- | ------------------- | ---- | ---------- |
| dings, we | effectively | cap | the | influence | of  | any single | data |               |       |                |            |               |                     |      |            |
|           |             |     |     |           |     |            |      | egories       | based | on usage       | frequency: |               | (a) high-frequency, |      | (b)        |
point. Specifically, BSQ’s projection of embeddings onto low-frequency, and (c) unused tokens. To investigate their
| a unit sphere     | prior | to binarization |               |     | guarantees | that   | the ex- |                  |         |                  |             |     |            |     |          |
| ----------------- | ----- | --------------- | ------------- | --- | ---------- | ------ | ------- | ---------------- | ------- | ---------------- | ----------- | --- | ---------- | --- | -------- |
|                   |       |                 |               |     |            |        |         | representational |         | characteristics, |             | we  | conduct    | an  | analysis |
| pected distortion |       | is strictly     | upper-bounded |     |            | (Zhao, | Xiong,  |                  |         |                  |             |     |            |     |          |
|                   |       |                 |               |     |            |        |         | where we         | replace | the              | final token | of  | an encoded |     | sequence |
andKra¨henbu¨hl2024):
|     |     |     |     |     |     |     |     | with a token | from | each | category | and | then | decode | it back |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ---- | -------- | --- | ---- | ------ | ------- |
(cid:113) √ √ toaK-line.Figure12presentstheresultsofthisprocedure.
E (cid:13) (cid:13)
(cid:13)u−u (cid:13) < 2−2/ L < 2. Weobserveaclearcorrespondencebetweentokenfrequency
u (cid:98)
|     |     |     |     |     |     |     |     | and pattern | typicality. |     | High-frequency |     | tokens | (a) | map to |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | -------------- | --- | ------ | --- | ------ |
ThisboundtightensasthecodebookdimensionLincreases.
|                |               |            |        |                  |           |              |            | common             | K-bar         | shapes,       | indicative   | of      | stable     | market          | condi-     |
| -------------- | ------------- | ---------- | ------ | ---------------- | --------- | ------------ | ---------- | ------------------ | ------------- | ------------- | ------------ | ------- | ---------- | --------------- | ---------- |
| In contrast,   | simpler       | methods    |        | like sign-based  |           | quantization |            |                    |               |               |              |         |            |                 |            |
|                |               |            |        |                  |           |              |            | tions. Conversely, |               | low-frequency |              | (b)     | and unused |                 | (c) tokens |
| without        | normalization |            | (e.g., | LFQ)             | lack such | a            | guarantee, |                    |               |               |              |         |            |                 |            |
|                |               |            |        |                  |           |              |            | generate           | more          | extreme       | and atypical |         | K-bars,    | such            | as those   |
| leaving        | them          | vulnerable | to     | arbitrarily      | large     | errors       | from       |                    |               |               |              |         |            |                 |            |
|                |               |            |        |                  |           |              |            | with long          | bodies        | or wicks,     | signifying   |         | rare,      | high-volatility |            |
| outlier inputs | (Zhao,        | Xiong,     |        | and Kra¨henbu¨hl |           | 2024).       | This       |                    |               |               |              |         |            |                 |            |
|                |               |            |        |                  |           |              |            | events.            | This suggests |               | that the     | learned | codebook   |                 | captures   |
boundederrorpropertyiscrucialforbuildingreliablefinan-
|     |     |     |     |     |     |     |     | a meaningful | semantic |     | hierarchy, | effectively |     | distinguishing |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ---------- | ----------- | --- | -------------- | --- |
cialforecastingmodels.
|                                         |              |        |             |      |                   |     |         | between         | common | and      | significant | market | patterns    |     | based on  |
| --------------------------------------- | ------------ | ------ | ----------- | ---- | ----------------- | --- | ------- | --------------- | ------ | -------- | ----------- | ------ | ----------- | --- | --------- |
| LearninginaCompactandDiscreteStateSpace |              |        |             |      |                   |     | High-   | tokenfrequency. |        |          |             |        |             |     |           |
| frequency                               | financial    | data   | exists      | in a | high-dimensional, |     | con-    |                 |        |          |             |        |             |     |           |
|                                         |              |        |             |      |                   |     |         | Hyperspherical  |        | geometry | for         | tail   | sensitivity |     | In finan- |
| tinuous                                 | state space, | posing | significant |      | challenges        |     | for se- |                 |        |          |             |        |             |     |           |
cialcontexts,marketreturnsandpricechangesoftenexhibit
quencemodels.Ourtokenizermapstheseinfinitestatesinto
heavytails(orfattails)(Mandelbrotetal.1963).Theheavy-
| a finite, | discrete | vocabulary | of  | tokens. | This | discretization |     |     |     |     |     |     |     |     |     |
| --------- | -------- | ---------- | --- | ------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
taildistributionofpricechangesisoneofthekeysourcesof
| serves as | a powerful | form | of  | regularization |     | with | two main |         |         |                 |     |            |     |        |        |
| --------- | ---------- | ---- | --- | -------------- | --- | ---- | -------- | ------- | ------- | --------------- | --- | ---------- | --- | ------ | ------ |
|           |            |      |     |                |     |      |          | trading | profits | in quantitative |     | investment | and | cannot | be ig- |
benefits(Rabanseretal.2020):
nored.
• Improved Sample Efficiency and Generalization: In- Unlike standard vector-quantization on the Euclidean
stead of learning a complex function over a continuous sphere, BSQ’s binary encoding preserves angular informa-

Setup Splits(n) Sub-Vocab(2k/n) CoreParams(M) VocabParams(M) FusionParams(M) TotalParams(M) InferenceStepsperToken
| NoSplit    |     | 1   | 1,048,576 |     |     | 97.5 |     | 1744.8 | 0.0 | 1842.3 | 1×  |
| ---------- | --- | --- | --------- | --- | --- | ---- | --- | ------ | --- | ------ | --- |
| Ours       |     | 2   | 1,024     |     |     | 97.5 |     | 3.4    | 1.4 | 102.3  | 2×  |
| MoreSplits |     | 4   | 32        |     |     | 97.5 |     | 0.2    | 2.8 | 100.5  | 4×  |
|            |     | 5   | 16        |     |     | 97.5 |     | 0.1    | 3.5 | 101.1  | 5×  |
Table 12: Trade-off analysis for factorizing a k = 20 bit token into n subtokens, based on the Kronos architecture. The
base
model’scoreTransformerblockshave≈97.5Mparameters.
tionveryefficiently,makingitmoresensitivetofat-taildata cially, these marginal or negative parameter benefits come
that manifest as sharp directional changes in feature space. atadirectandsubstantiallatencycost:movingfromn = 2
This aligns well with how microstructure events often ap- ton = 4doublesthenumberofsequentialgenerationsteps
pear as abrupt shifts in the “direction” of the joint price- requiredpertoken.
n = 2
volumevector(Podobniketal.2009). In summary, our choice of represents an effec-
Figure 11 illustrates the tokenizer’s ability to capture tivebalance.Itcapturesthevastmajorityoftheparameter-
and reconstruct the long-tailed market microstructure un- reduction benefits, making our large vocabulary practical,
dershort-termhighvolatilityandduringextremegapevents whileavoidingthesignificantlatencypenaltiesandgrowing
(intheeconomiccontextofTrump’sTradeWar(McKibbin, architecturaloverheadassociatedwithfiner-grainedsplits.
Noland,andShuetrim2025)).
Aboveall,wesummarizetheconcreteadvantagesofBSQ
forK-linetimeseriesdata,leveragingitsabilitytopreserve
| angular   | information | and | capture  | sharp     | directional |        | changes, |     |     |     |     |
| --------- | ----------- | --- | -------- | --------- | ----------- | ------ | -------- | --- | --- | --- | --- |
| which are | crucial     | for | modeling | financial | time        | series | with     |     |     |     |     |
heavytailsandabruptshiftsduetomicrostructureevents.
AnalysisofSubtokenFactorization(Q3)
| Our methodology |         | factorizes |          | a k-bit token | into          | n subtokens |           |     |     |     |     |
| --------------- | ------- | ---------- | -------- | ------------- | ------------- | ----------- | --------- | --- | --- | --- | --- |
| to manage       | a large | vocabulary |          | size. A       | key design    |             | choice is |     |     |     |     |
| the number      | of      | factors,   | n. While | further       | factorization |             | (e.g.,    |     |     |     |     |
n > 2)couldreducesub-vocabularysizesevenmore(e.g.,
| from 210   | to 25 | for a k   | = 20    | token),   | we argue | that       | n = | 2   |     |     |     |
| ---------- | ----- | --------- | ------- | --------- | -------- | ---------- | --- | --- | --- | --- | --- |
| offers the | best  | trade-off | between | parameter |          | efficiency | and |     |     |     |     |
inferencelatency.
Thisfactorizationintroducesafundamentaltrade-off.On
| one hand,                                         | it significantly |     | reduces                      | the | size | of vocabulary- |     |     |     |     |     |
| ------------------------------------------------- | ---------------- | --- | ---------------------------- | --- | ---- | -------------- | --- | --- | --- | --- | --- |
| dependentparameters                               |                  |     | intheinputembeddingandoutput |     |      |                |     |     |     |     |     |
| projectionlayers,replacingasinglelargetablefora2k |                  |     |                              |     |      |                | vo- |     |     |     |     |
2k/n
| cabulary | with | n smaller | tables | for | sub-vocabularies. |     |     |     |     |     |     |
| -------- | ---- | --------- | ------ | --- | ----------------- | --- | --- | --- | --- | --- | --- |
Ontheotherhand,itintroducestwocosts:(1)anewfusion
| layer(W | inEquation5),whoseparameters(n×d |     |     |     |     |     | )×    |     |     |     |     |
| ------- | -------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
|         | fuse                             |     |     |     |     |     | model |     |     |     |     |
d growlinearlywithn,and(2)increasedinferencela-
model
n
| tency, as | generating | a   | full token | requires |     | sequential | au- |     |     |     |     |
| --------- | ---------- | --- | ---------- | -------- | --- | ---------- | --- | --- | --- | --- | --- |
toregressivesteps.
| Table | 12 quantifies |     | this | trade-off | for | our Kronos |     |     |     |     |     |
| ----- | ------------- | --- | ---- | --------- | --- | ---------- | --- | --- | --- | --- | --- |
base
model.Themostsignificantparameterreductionisachieved
| by moving   | from  | no factorization |                      | (n        | = 1) to   | a 2-way    | split.    |     |     |     |     |
| ----------- | ----- | ---------------- | -------------------- | --------- | --------- | ---------- | --------- | --- | --- | --- | --- |
| This single | step  | reduces          | vocabulary-dependent |           |           | parameters |           |     |     |     |     |
| by over     | 99.8% | (from            | ≈1.7B                | to 3.4M), | shrinking |            | the total |     |     |     |     |
modelsizebynearly95%andmakingalargeeffectivevo-
cabularycomputationallyfeasible.
However,furtherfactorizationyieldsdiminishingreturns
| whileincurringrisingcosts.Movingfromn |     |     |     |     |     | = 2ton | =   | 4   |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
reducesvocabularyparametersbyonly3.2M,asavingthat
ispartiallyoffsetbya1.4Mincreaseinfusionlayerparam-
| eters. This | results | in             | a marginal | total     | parameter |     | reduction |     |     |     |     |
| ----------- | ------- | -------------- | ---------- | --------- | --------- | --- | --------- | --- | --- | --- | --- |
| of just     | ≈2%.    | As n increases |            | to 5, the | overhead  |     | from the  |     |     |     |     |
fusionlayeroutweighsthesavingsfromthesmallervocab-
| ularies, | causing | the total | parameter | count | to  | increase. | Cru- |     |     |     |     |
| -------- | ------- | --------- | --------- | ----- | --- | --------- | ---- | --- | --- | --- | --- |

Exchange/Country AssetTypes Timeframes #Assets #Observations StartDate
Binance Crypto,PerpetualSwap T,5T,15T,30T,H,D,W 997 1,237,002,843 2021/1/31
| AthensStockExchange | Stock,ETF | D,W | 180 | 226,315 2023/4/11 |
| ------------------- | --------- | --- | --- | ----------------- |
BeijingStockExchange Stock 5T,15T,30T,H,D,W 272 10,197,628 2021/11/19
| BrazilStockExchange | Stock,ETF | D,W | 2,058 | 1,315,290 2020/1/31 |
| ------------------- | --------- | --- | ----- | ------------------- |
| MoscowExchange      | Stock,ETF | D,W | 514   | 567,351 2020/1/31   |
| EuronextAmsterdam   | Stock,ETF | D,W | 514   | 602,083 2020/1/31   |
AustralianSecuritiesExchange Stock,ETF 5T,15T,30T,H,D,W 3,381 86,613,897 2020/1/31
StockExchangeofThailand Stock,ETF 5T,15T,30T,H,D,W 1,664 49,590,394 2020/1/31
BombayStockExchange Stock,ETF 5T,15T,30T,H,D,W 5,491 284,428,211 2020/1/31
| EuronextBrussels         | Stock,ETF | D,W | 166 | 195,491 2020/1/31 |
| ------------------------ | --------- | --- | --- | ----------------- |
| BucharestStockExchange   | Stock,ETF | D,W | 247 | 176,080 2020/1/31 |
| BudapestStockExchange    | Stock,ETF | D,W | 50  | 57,586 2022/1/14  |
| BuenosAiresStockExchange | Stock     | D,W | 183 | 225,352 2020/1/31 |
| ColomboStockExchange     | Stock     | D,W | 292 | 372,627 2020/1/31 |
| CopenhagenStockExchange  | Stock     | D,W | 825 | 617,464 2020/1/31 |
FrankfurtStockExchange Stock,ETF D,W 17,054 21,547,744 2020/1/31
| GhanaStockExchange | Stock | D,W | 44  | 57,690 2020/1/31 |
| ------------------ | ----- | --- | --- | ---------------- |
HongKongStockExchange Stock,ETF 5T,15T,30T,H,D,W 3,500 359,434,220 2020/1/31
JapanExchangeGroup Stock,ETF 5T,15T,30T,H,D,W 4,467 280,601,980 2020/1/31
IndonesiaStockExchange Stock 5T,15T,30T,H,D,W 935 38,627,125 2020/1/31
| BorsaIstanbul | Stock | D,W | 627 | 784,147 2020/1/31 |
| ------------- | ----- | --- | --- | ----------------- |
JohannesburgStockExchange Stock,ETF D,W 562 681,587 2020/1/31
| PakistanStockExchange | Stock,ETF | D,W | 660 | 595,505 2020/1/31 |
| --------------------- | --------- | --- | --- | ----------------- |
KualaLumpurStockExchange Stock,ETF 5T,15T,30T,H,D,W 1,150 45,938,559 2020/1/31
KoreaExchange Stock,ETF 5T,15T,30T,H,D,W 2,928 205,061,301 2020/1/31
| LimaStockExchange | Stock,ETF | D,W | 166 | 63,503 2020/1/31 |
| ----------------- | --------- | --- | --- | ---------------- |
| EuronextLisbon    | Stock,ETF | D,W | 60  | 65,753 2020/1/31 |
LondonStockExchange Stock,ETF 5T,15T,30T,H,D,W 8,660 177,947,624 2020/1/31
| LuxembourgStockExchange | Stock     | D,W | 5   | 7,598 2020/1/31   |
| ----------------------- | --------- | --- | --- | ----------------- |
| MadridStockExchange     | Stock,ETF | D,W | 309 | 331,745 2020/1/31 |
| MexicanStockExchange    | Stock,ETF | D,W | 775 | 937,637 2020/1/31 |
NasdaqStockExchange Stock,ETF T,5T,15T,30T,H,D,W 8,725 2,478,662,459 2000/1/1
NationalStockExchangeofIndia Stock,ETF 5T,15T,30T,H,D,W 2,554 242,429,169 2020/1/31
NewYorkStockExchange Stock,ETF T,5T,15T,30T,H,D,W 7,073 2,133,143,549 2000/1/1
| EuronextParis | Stock,ETF | D,W | 1,781 | 1,981,059 2020/1/31 |
| ------------- | --------- | --- | ----- | ------------------- |
PhilippineStockExchange Stock,ETF 5T,15T,30T,H,D,W 351 4,388,378 2020/1/31
| PragueStockExchange   | Stock | D,W | 50  | 62,666 2020/1/31  |
| --------------------- | ----- | --- | --- | ----------------- |
| SantiagoStockExchange | Stock | D,W | 225 | 160,638 2020/1/31 |
ShenzhenStockExchange Stock,ETF T,5T,15T,30T,H,D,W 3,519 1,754,519,331 1990/12/19
ShenzhenStockExchange(B-shares) Stock 5T,15T,30T,H,D,W 46 4,198,702 2020/2/3
ShanghaiStockExchange Stock,ETF T,5T,15T,30T,H,D,W 3,064 1,967,996,343 1990/12/19
ShanghaiStockExchange(B-shares) Stock 5T,15T,30T,H,D,W 50 4,526,152 2020/2/3
StockholmStockExchange Stock,ETF D,W 1,305 1,463,722 2020/1/31
| SIXSwissExchange | Stock,ETF | D,W | 1,981 | 2,451,675 2020/1/31 |
| ---------------- | --------- | --- | ----- | ------------------- |
TaiwanStockExchange Stock,ETF 5T,15T,30T,H,D,W 1,252 71,619,260 2020/1/31
| TorontoStockExchange | Stock,ETF | D,W        | 3,035 | 3,356,561 2020/1/31 |
| -------------------- | --------- | ---------- | ----- | ------------------- |
| ViennaStockExchange  | Stock     | D,W        | 98    | 123,643 2020/1/31   |
| China                | Future    | T,5T,15T,D | 75    | 63,318,960 2010/1/1 |
\ ForeignExchange 5T,15T,30T,H,D,W 1,023 462,434,562 2020/1/31
| Australia | StockIndex | 5T,15T,30T,H,D,W | 40  | 183,158 2020/1/31   |
| --------- | ---------- | ---------------- | --- | ------------------- |
| Belgium   | StockIndex | D,W              | 5   | 8,109 2020/1/31     |
| Brazil    | StockIndex | D,W              | 3   | 4,766 2020/1/31     |
| Canada    | StockIndex | D,W              | 18  | 27,622 2020/1/31    |
| China     | StockIndex | 5T,15T,30T,H,D,W | 597 | 55,884,065 2020/2/3 |
| Germany   | StockIndex | D,W              | 18  | 28,622 2020/1/31    |
| Spain     | StockIndex | D,W              | 2   | 3,257 2020/1/31     |
| France    | StockIndex | D,W              | 38  | 55,945 2020/1/31    |
| Britain   | StockIndex | 5T,15T,30T,H,D,W | 51  | 5,355,869 2020/1/31 |
| Greece    | StockIndex | D,W              | 1   | 1,589 2020/1/31     |
HongKong,China StockIndex 5T,15T,30T,H,D,W 4 453,016 2020/1/31
| Hungary | StockIndex | D,W | 1   | 1,602 2020/1/31 |
| ------- | ---------- | --- | --- | --------------- |
Continuedonnextpage

Table13–Continuedfrompreviouspage
Exchange/Country AssetTypes Timeframes #Assets #Observations StartDate
| Indonesia         | StockIndex | 5T,15T,30T,H,D,W | 2     | 47,816 2020/1/31     |
| ----------------- | ---------- | ---------------- | ----- | -------------------- |
| India             | StockIndex | 5T,15T,30T,H,D,W | 113   | 3,189,450 2020/1/31  |
| Japan             | StockIndex | 5T,15T,30T,H,D,W | 9     | 125,024 2020/1/31    |
| Korea             | StockIndex | 5T,15T,30T,H,D,W | 5     | 274,292 2020/1/31    |
| Mexico            | StockIndex | D,W              | 1     | 1,619 2020/1/31      |
| Malaysia          | StockIndex | D,W              | 2     | 3,145 2020/1/31      |
| Netherlands       | StockIndex | D,W              | 4     | 6,475 2020/1/31      |
| Pakistan          | StockIndex | D,W              | 3     | 3,184 2020/1/31      |
| Philippines       | StockIndex | D,W              | 2     | 3,187 2020/1/31      |
| Portugal          | StockIndex | D,W              | 1     | 1,632 2020/1/31      |
| Romania           | StockIndex | D,W              | 5     | 7,726 2020/1/31      |
| Russia            | StockIndex | D,W              | 15    | 19,079 2020/1/31     |
| Sweden            | StockIndex | D,W              | 11    | 16,389 2020/1/31     |
| Thailand          | StockIndex | D,W              | 4     | 5,005 2020/1/31      |
| Taiwan,China      | StockIndex | 5T,15T,30T,H,D,W | 1     | 85,318 2020/1/31     |
| America           | StockIndex | 5T,15T,30T,H,D,W | 670   | 37,887,535 2020/1/31 |
| ApproximateTotals |            |                  | 96569 | 12.11B –             |
Table13:Descriptivestatisticsofthemulti-exchange,multi-assetK-linedataset.Thetimeframeabbreviationsare:T(1-min),
H(1-hour),D(1-day),W(1-week).

| 11.3        |     |     | 90          |     |     |
| ----------- | --- | --- | ----------- | --- | --- |
| 11.2        |     |     | 88          |     |     |
| ecirP esolC |     |     | ecirP esolC |     |     |
11.1
86
11.0
84
10.9
| 10.8                |     |     | Ground Truth   |     |     |
| ------------------- | --- | --- | -------------- | --- | --- |
| Ground Truth        |     |     | 82             |     |     |
| 10.7 Reconstruction |     |     | Reconstruction |     |     |
| 7000                |     |     | 500000         |     |     |
| Ground Truth        |     |     | Ground Truth   |     |     |
| 6000 Reconstruction |     |     | Reconstruction |     |     |
400000
5000
| emuloV |     | emuloV | 300000 |     |     |
| ------ | --- | ------ | ------ | --- | --- |
4000
3000
200000
2000
100000
1000
| 0   |     |     | 0   |     |     |
| --- | --- | --- | --- | --- | --- |
0 50 100 150 200 250 300 350 400 0 50 100 150 200 250 300 350 400
| (a)ChinaFilmCo.,Ltd.(SSE:600977) |     |     |     | (b)PopMart(HKEX:09992) |     |
| -------------------------------- | --- | --- | --- | ---------------------- | --- |
140
| 135             |     |             | 45000 |     |     |
| --------------- | --- | ----------- | ----- | --- | --- |
| ecirP esolC 130 |     | ecirP esolC |       |     |     |
| 125             |     |             | 44000 |     |     |
120
43000
115
110
| Ground Truth       |     |     | 42000 Ground Truth |     |     |
| ------------------ | --- | --- | ------------------ | --- | --- |
| 105 Reconstruction |     |     | Reconstruction     |     |     |
1e8
17500 Ground Truth
1.4 Ground Truth
| Reconstruction |     |     | 15000 Reconstruction |     |     |
| -------------- | --- | --- | -------------------- | --- | --- |
1.2
| emuloV 1.0 |     | emuloV | 12500 |     |     |
| ---------- | --- | ------ | ----- | --- | --- |
10000
0.8
7500
0.6
5000
| 0.4 |     |     | 2500 |     |     |
| --- | --- | --- | ---- | --- | --- |
0.2
0
| 0 50 | 100 150                | 200 250 | 0 50                                  | 100 150 200 | 250 300 350 |
| ---- | ---------------------- | ------- | ------------------------------------- | ----------- | ----------- |
|      | (c)NVIDIA(NASDAQ:NVDA) |         | (d)BTC/USDTPerpetual(Binance:BTCUSDT) |             |             |
3620
90
3600
85
| ecirP esolC |     | ecirP esolC | 3580 |     |     |
| ----------- | --- | ----------- | ---- | --- | --- |
80
3560
75
3540
70
| Ground Truth |     |     | 3520 Ground Truth |     |     |
| ------------ | --- | --- | ----------------- | --- | --- |
3500
| 65 Reconstruction |     |     | Reconstruction |     |     |
| ----------------- | --- | --- | -------------- | --- | --- |
140000
| Ground Truth          |     |     | 300000 Ground Truth |     |     |
| --------------------- | --- | --- | ------------------- | --- | --- |
| 120000 Reconstruction |     |     | Reconstruction      |     |     |
250000
100000
| emuloV |     | emuloV | 200000 |     |     |
| ------ | --- | ------ | ------ | --- | --- |
80000
| 60000 |     |     | 150000 |     |     |
| ----- | --- | --- | ------ | --- | --- |
| 40000 |     |     | 100000 |     |     |
| 20000 |     |     | 50000  |     |     |
0
| 0 50 | 100 150         | 200 250 | 0 50                          | 100 150 200 | 250 300 350 |
| ---- | --------------- | ------- | ----------------------------- | ----------- | ----------- |
|      | (e)BMW(FWB:BMW) |         | (f)RebarSteelFutures(SHFE:RB) |             |             |
Figure 10: Visualization of reconstruction results for the ‘Close Price’ and ‘Volume’ from our K-line Tokenizer. Blue lines
denotethegroundtruth,whileredlinesindicatethereconstructionsgeneratedbyourmodel.

|     | Stock: CATL (interval = 5 min) |                |             | Focus View |                |
| --- | ------------------------------ | -------------- | ----------- | ---------- | -------------- |
|     |                                | Ground Truth   |             |            | Ground Truth   |
|     |                                | Reconstruction | 240         |            | Reconstruction |
|     |                                | Focus Area     | ecirP esolC |            |                |
230
250
220
|     |     |     | 0402 14:35 0403 10:45 | 0403 13:55 0407 10:05 | 0407 13:15 |
| --- | --- | --- | --------------------- | --------------------- | ---------- |
Time
| 240 |     |     |     | GroundTruth Kline Chart |     |
| --- | --- | --- | --- | ----------------------- | --- |
240
ecirP esolC
ecirP
230
230
220
|     |     |     | 0403 13:55 0403 14:25 | 0403 14:55 0407 09:55 | 0407 10:25 |
| --- | --- | --- | --------------------- | --------------------- | ---------- |
Time
Reconstruction Kline Chart
220
240
ecirP
230
| 210 |     |     | 220 |     |     |
| --- | --- | --- | --- | --- | --- |
0331 13:25 0402 10:35 0403 14:45 0408 13:25 0410 10:35 0411 14:45 0403 13:55 0403 14:25 0403 14:55 0407 09:55 0407 10:25
Time Time
(a)StockK-lineReconstruction,PricePart
| 1e7 | Stock: CATL (interval = 5 min) |                | 1e7 | Focus View |                |
| --- | ------------------------------ | -------------- | --- | ---------- | -------------- |
|     |                                | Ground Truth   | 1.0 |            | Ground Truth   |
|     |                                | Reconstruction |     |            | Reconstruction |
0.8
|     |     | Focus Area | emuloV |     |     |
| --- | --- | ---------- | ------ | --- | --- |
0.6
1.0
0.4
0.2
|     |     |     | 0402 14:35 0403 10:45 | 0403 13:55 0407 10:05   | 0407 13:15 |
| --- | --- | --- | --------------------- | ----------------------- | ---------- |
| 0.8 |     |     |                       | Time                    |            |
|     |     |     | 1e7                   | GroundTruth Kline Chart |            |
1.0
| emuloV |     |     | emuloV 0.8 |     |     |
| ------ | --- | --- | ---------- | --- | --- |
0.6
0.6
0.4
0.2
0.4
|     |     |     | 0403 13:55 0403 14:25 | 0403 14:55 0407 09:55 | 0407 10:25 |
| --- | --- | --- | --------------------- | --------------------- | ---------- |
Time
Reconstruction Kline Chart
1e7
1.0
0.2
0.8
emuloV
0.6
0.4
| 0.0 |     |     | 0.2 |     |     |
| --- | --- | --- | --- | --- | --- |
0331 13:25 0402 10:35 0403 14:45 0408 13:25 0410 10:35 0411 14:45 0403 13:55 0403 14:25 0403 14:55 0407 09:55 0407 10:25
Time Time
(b)StockK-lineReconstruction,VolumePart
Figure11:Illustrationofthereconstructionperformanceof5-minuteK-linedataforCATL(ContemporaryAmperexTechnol-
ogyCo.,Limited)onApril7th,2025,intheeconomiccontextofTrump’sTradeWar(McKibbin,Noland,andShuetrim2025).
In the visualization, the candlesticks follow a “red for up, green for down” convention (where up/down is determined by the
closepricerelativetotheopenprice),andthevolumebarsarecoloredaccordingly.

| 29.0        | 29.0        |     | 29.0        |
| ----------- | ----------- | --- | ----------- |
| 28.5        | 28.5        |     | 28.5        |
| 28.0        | 28.0        |     | 28.0        |
| 27.5        | 27.5        |     | 27.5        |
| ecirP 27.0  | ecirP 27.0  |     | ecirP 27.0  |
| 26.5        | 26.5        |     | 26.5        |
| 26.0        | 26.0        |     | 26.0        |
| 25.5        | 25.5        |     | 25.5        |
| 25.0        | 25.0        |     | 25.0        |
| 10000       | 10000       |     | 10000       |
| emuloV 7500 | emuloV 7500 |     | emuloV 7500 |
| 5000        | 5000        |     | 5000        |
| 2500        | 2500        |     | 2500        |
0 0 3 6 9 12 15 18 21 24 27 30 33 0 0 3 6 9 12 15 18 21 24 27 30 33 0 0 3 6 9 12 15 18 21 24 27 30 33
(a)Examplesofhigh-frequencytokens.
| 29.0        | 29.0        |     | 29.0        |
| ----------- | ----------- | --- | ----------- |
| 28.5        | 28.5        |     | 28.5        |
| 28.0        | 28.0        |     | 28.0        |
| 27.5        | 27.5        |     | 27.5        |
| ecirP 27.0  | ecirP 27.0  |     | ecirP 27.0  |
| 26.5        | 26.5        |     | 26.5        |
| 26.0        | 26.0        |     | 26.0        |
| 25.5        | 25.5        |     | 25.5        |
| 25.0        | 25.0        |     | 25.0        |
| 10000       | 10000       |     | 10000       |
| emuloV 7500 | emuloV 7500 |     | emuloV 7500 |
| 5000        | 5000        |     | 5000        |
| 2500        | 2500        |     | 2500        |
| 0           | 0           |     | 0           |
0 3 6 9 12 15 18 21 24 27 30 33 0 3 6 9 12 15 18 21 24 27 30 33 0 3 6 9 12 15 18 21 24 27 30 33
(b)Examplesoflow-frequencytokens.
| 29  | 29.0 |     | 29  |
| --- | ---- | --- | --- |
| 28  | 28.5 |     |     |
28.0 28
| 27    | 27.5  |     |          |
| ----- | ----- | --- | -------- |
| ecirP | ecirP |     | ecirP 27 |
| 26    | 27.0  |     |          |
26.5
| 25  | 26.0 |     | 26  |
| --- | ---- | --- | --- |
24
25.5 25
| 23     | 25.0        |     |             |
| ------ | ----------- | --- | ----------- |
| 15000  | 10000       |     | 10000       |
| emuloV | emuloV 7500 |     | emuloV 7500 |
10000
| 5000 | 5000 |     | 5000 |
| ---- | ---- | --- | ---- |
|      | 2500 |     | 2500 |
| 0    | 0    |     | 0    |
0 3 6 9 12 15 18 21 24 27 30 33 0 3 6 9 12 15 18 21 24 27 30 33 0 3 6 9 12 15 18 21 24 27 30 33
(c)Examplesofunusedtokensfromthevocabulary.
29.0
28.5
28.0
27.5
ecirP
27.0
26.5
26.0
25.5
25.0
10000
emuloV 7500
5000
2500
0
|     | 0 3 6 9 | 12 15 18 21 24 | 27 30 33 |
| --- | ------- | -------------- | -------- |
(d)Asampleofanoriginaltokensequence.
Figure12:Visualizationoftokenusagepatterns.Thefigureillustratestokencategoriesbasedontheiroccurrencefrequencyin
thecorpus:(a)high-frequency,(b)low-frequency,and(c)unused(zero-frequency)tokens.Asamplefromanoriginalsequence
(d)isshownforreference.Thesequencesin(a),(b),and(c)areconstructedbyreplacingthelasttokenof(d)witharandomly
sampled token from the corresponding category. In the visualization, the candlesticks follow a “red for up, green for down”
convention (where up/down is determined by the close price relative to the open price), and the volume bars are colored
accordingly.

10 K r o n o s s mall K r o n o s b ase K r o n o s l arge D i f f u s i o nTS T i m e V A E 10 T i m e G A N
O r ig i n a l 10 O r ig i n a l 10 O r ig i n a l 10 O r i g i n a l 10 O r ig in a l O r ig in a l
| 5   | 5   | 5   | 5   | 5   | 5   |     |
| --- | --- | --- | --- | --- | --- | --- |
|     | 0   | 0   | 0   | 0   | 0   |     |
0
5
| 5   |     | 5   | 5   | 5   | 5   |     |
| --- | --- | --- | --- | --- | --- | --- |
|     | 10  | 10  | 10  | 10  | 10  |     |
10
10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10
1.4 O r ig i n a l 1.4 O r ig i n a l 1.4 Original O r i g i n a l 1.4 Original 1.75 Original
etamitsE ytisneD ataD Kr o n o s s mall etamitsE ytisneD ataD Kr o n o s b ase etamitsE ytisneD ataD Kronoslarge etamitsE ytisneD ataD Di f f u s i o nTS etamitsE ytisneD ataD TimeVAE etamitsE ytisneD ataD 1.50 TimeGAN
| 1.2 | 1.2 | 1.2 | 2.0 | 1.2 |      |     |
| --- | --- | --- | --- | --- | ---- | --- |
| 1.0 | 1.0 | 1.0 |     | 1.0 | 1.25 |     |
1.5
| 0.8 | 0.8 | 0.8 |     | 0.8 | 1.00 |     |
| --- | --- | --- | --- | --- | ---- | --- |
|     |     |     | 1.0 |     | 0.75 |     |
| 0.6 | 0.6 | 0.6 |     | 0.6 |      |     |
| 0.4 | 0.4 | 0.4 |     | 0.4 | 0.50 |     |
0.5
| 0.2 | 0.2 | 0.2 |     | 0.2 | 0.25 |     |
| --- | --- | --- | --- | --- | ---- | --- |
| 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.00 |     |
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0
Data Value Data Value Data Value Data Value Data Value Data Value
(a)ShanghaiStockExchange(XSHG),Dailyfrequency
K r o n o s s mall K r o n o s b ase K r o n o s l arge D i f f u s i o nTS T i m e V A E 10 T i m e G A N
10 O r ig i n a l 10 O r ig i n a l 10 O r ig i n a l 10 O r i g i n a l 10 O r ig in a l O r ig in a l
| 5   | 5   | 5   |     | 5   | 5   |     |
| --- | --- | --- | --- | --- | --- | --- |
5
| 0   | 0   | 0   | 0   | 0   | 0   |     |
| --- | --- | --- | --- | --- | --- | --- |
| 5   | 5   | 5   | 5   | 5   | 5   |     |
| 10  |     |     | 10  | 10  |     |     |
|     | 10  | 10  |     |     | 10  |     |
10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10
|     | Original | Original | Original 5 | Original | Original | Original |
| --- | -------- | -------- | ---------- | -------- | -------- | -------- |
2.5 Kronossmall 2.5 Kronosbase 2.5 Kronoslarge DiffusionTS 2.5 TimeVAE 2.5 TimeGAN
etamitsE ytisneD ataD etamitsE ytisneD ataD etamitsE ytisneD ataD etamitsE ytisneD ataD 4 etamitsE ytisneD ataD etamitsE ytisneD ataD
| 2.0 | 2.0 | 2.0 |     | 2.0 | 2.0 |     |
| --- | --- | --- | --- | --- | --- | --- |
| 1.5 | 1.5 | 1.5 | 3   | 1.5 | 1.5 |     |
2
| 1.0 | 1.0 | 1.0 |     | 1.0 | 1.0 |     |
| --- | --- | --- | --- | --- | --- | --- |
1
| 0.5 | 0.5 | 0.5 |     | 0.5 | 0.5 |     |
| --- | --- | --- | --- | --- | --- | --- |
0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0 0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0
Data Value Data Value Data Value Data Value Data Value Data Value
(b)TaiwanStockExchange(XTAI),15-minutefrequency
15
10 K r o n o s s mall K r o n o s b ase 10 K r o n o s l arge D i f f u s i o nTS T i m e V A E T i m e G A N
O r ig i n a l 10 O r ig i n a l O r ig i n a l 10 O r i g i n a l 10 O r ig in a l 10 O r ig in a l
| 5   | 5   | 5   | 5   | 5   | 5   |     |
| --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   | 0   |     |
|     | 5   |     |     | 5   |     |     |
| 5   |     | 5   | 5   |     | 5   |     |
10
|     | 10  | 10  | 10  |     | 10  |     |
| --- | --- | --- | --- | --- | --- | --- |
| 10  |     |     |     | 15  |     |     |
10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10
1.4 Original 1.4 Original 1.4 Original 3.5 O r i g i n a l 1.4 O r ig in a l 2.00 Original
etamitsE ytisneD ataD Kronossmall etamitsE ytisneD ataD Kronosbase etamitsE ytisneD ataD Kronoslarge etamitsE ytisneD ataD 3.0 Di f f u s i o nTS etamitsE ytisneD ataD Ti m e V A E etamitsE ytisneD ataD TimeGAN
| 1.2 | 1.2 | 1.2 |     | 1.2 | 1.75 |     |
| --- | --- | --- | --- | --- | ---- | --- |
| 1.0 | 1.0 | 1.0 | 2.5 | 1.0 | 1.50 |     |
1.25
| 0.8 | 0.8 | 0.8 | 2.0 | 0.8 |      |     |
| --- | --- | --- | --- | --- | ---- | --- |
| 0.6 | 0.6 | 0.6 | 1.5 | 0.6 | 1.00 |     |
0.75
| 0.4 | 0.4 | 0.4 | 1.0 | 0.4 | 0.50 |     |
| --- | --- | --- | --- | --- | ---- | --- |
| 0.2 | 0.2 | 0.2 | 0.5 | 0.2 | 0.25 |     |
| 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.00 |     |
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0
Data Value Data Value Data Value Data Value Data Value Data Value
(c)TaiwanStockExchange(XTAI),Dailyfrequency
K r o n o s s mall K r o n o s b ase K r o n o s l arge 1 5 D i f f u s i o nTS T i m e V A E T i m e G A N
10 O r ig i n a l 10 O r ig i n a l 10 O r ig i n a l O r i g i n a l 10 O r ig in a l 10 O r ig in a l
1 0
| 5   | 5   | 5   |     | 5   | 5   |     |
| --- | --- | --- | --- | --- | --- | --- |
5
| 0   |     |     |     |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- |
|     | 0   | 0   | 0   | 0   |     |     |
| 5   | 5   | 5   | 5   | 5   | 5   |     |
| 10  | 10  | 10  | 10  | 10  | 10  |     |
10 5 0 5 10 15 10 5 0 5 10 15 15 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 15 10 5 0 5 10
1.2 Original 1.2 Original Original Original 1.2 Original 1.2 Original
Kronossmall Kronosbase 1.2 Kronoslarge 1.4 DiffusionTS TimeVAE TimeGAN
etamitsE ytisneD ataD 1.0 etamitsE ytisneD ataD 1.0 etamitsE ytisneD ataD etamitsE ytisneD ataD 1.2 etamitsE ytisneD ataD 1.0 etamitsE ytisneD ataD 1.0
1.0
| 0.8 | 0.8 |     | 1.0 | 0.8 | 0.8 |     |
| --- | --- | --- | --- | --- | --- | --- |
|     |     | 0.8 | 0.8 |     |     |     |
| 0.6 | 0.6 | 0.6 |     | 0.6 | 0.6 |     |
0.6
| 0.4 | 0.4 | 0.4 |     | 0.4 | 0.4 |     |
| --- | --- | --- | --- | --- | --- | --- |
0.4
| 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |     |
| --- | --- | --- | --- | --- | --- | --- |
0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0
Data Value Data Value Data Value Data Value Data Value Data Value
(d)Cryptocurrency(Crypto),15-minutefrequency
Figure 13: Visual comparison of generative models on different datasets. Top row in each subfigure: t-SNE embeddings of
original(red)versussynthetic(blue)data.Bottomrowineachsubfigure:KernelDensityEstimates(KDE)oforiginalversus
syntheticdata.

|     |     | 1 5 |     | 1 5 |     |
| --- | --- | --- | --- | --- | --- |
K r o n o s s mall K r o n o s b ase K r o n o s l arge D i f f u s i o nTS T i m e V A E T i m e G A N
10 O r ig i n a l 10 O r ig i n a l 1 0 O r ig i n a l 10 O r i g i n a l 1 0 O r ig in a l 10 O r ig in a l
| 5   | 5   | 5   | 5   | 5   | 5   |
| --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   |     |
0
| 5   | 5   | 5   | 5   | 5   |     |
| --- | --- | --- | --- | --- | --- |
5
| 1 0 | 1 0 | 1 0 | 10  | 1 0 |     |
| --- | --- | --- | --- | --- | --- |
10
|     | 1 5 | 1 5 |     | 1 5 |     |
| --- | --- | --- | --- | --- | --- |
1 5 10 5 0 5 10 15 15 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 15 15 10 5 0 5 10 15 10 5 0 5 10
1.4
1.2 Original 1.2 Original 1.2 Original 1.6 O r i g i n a l 1.4 Original Original
etamitsE ytisneD ataD Kronossmall etamitsE ytisneD ataD Kronosbase etamitsE ytisneD ataD Kronoslarge etamitsE ytisneD ataD 1.4 Di f f u s i o nTS etamitsE ytisneD ataD TimeVAE etamitsE ytisneD ataD 1.2 TimeGAN
| 1.0 | 1.0 | 1.0 |     | 1.2 |     |
| --- | --- | --- | --- | --- | --- |
|     |     |     | 1.2 | 1.0 | 1.0 |
| 0.8 | 0.8 | 0.8 | 1.0 |     |     |
|     |     |     |     | 0.8 | 0.8 |
| 0.6 | 0.6 | 0.6 | 0.8 |     | 0.6 |
|     |     |     | 0.6 | 0.6 |     |
| 0.4 | 0.4 | 0.4 |     | 0.4 | 0.4 |
0.4
| 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |
| --- | --- | --- | --- | --- | --- |
| 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0
Data Value Data Value Data Value Data Value Data Value Data Value
(a)Cryptocurrency(Crypto),Dailyfrequency
Kronossmall Kronosbase Kronoslarge DiffusionTS TimeVAE TimeGAN
10 Original 10 Original 10 Original 10 Original 10 Original Original
10
|     | 5   | 5   |     | 5   |     |
| --- | --- | --- | --- | --- | --- |
| 5   |     |     | 5   |     | 5   |
| 0   | 0   | 0   | 0   | 0   | 0   |
| 5   | 5   | 5   | 5   | 5   | 5   |
| 10  | 10  | 10  | 10  | 10  | 10  |
10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 15 10 5 0 5 10 10 5 0 5 10
1.2 Original 1.2 Original 1.2 O r ig i n a l Original 1.2 Original Original
Kronossmall Kronosbase Kr o n o s l arge 1.4 DiffusionTS TimeVAE 1.0 TimeGAN
etamitsE ytisneD ataD 1.0 etamitsE ytisneD ataD 1.0 etamitsE ytisneD ataD 1.0 etamitsE ytisneD ataD 1.2 etamitsE ytisneD ataD 1.0 etamitsE ytisneD ataD
| 0.8 | 0.8 | 0.8 | 1.0 | 0.8 | 0.8 |
| --- | --- | --- | --- | --- | --- |
0.8
| 0.6 | 0.6 | 0.6 |     | 0.6 | 0.6 |
| --- | --- | --- | --- | --- | --- |
0.6
| 0.4 | 0.4 | 0.4 |     | 0.4 | 0.4 |
| --- | --- | --- | --- | --- | --- |
0.4
| 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |
| --- | --- | --- | --- | --- | --- |
0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0
Data Value Data Value Data Value Data Value Data Value Data Value
(b)ForeignExchange(Forex),15-minutefrequency
15
Kronossmall Kronosbase Kronoslarge DiffusionTS 15 TimeVAE TimeGAN
10 Original 10 Original 10 Original 10 Original Original 10 Original
10
| 5   | 5   | 5   | 5   |     | 5   |
| --- | --- | --- | --- | --- | --- |
5
| 0   | 0   | 0   | 0   |     | 0   |
| --- | --- | --- | --- | --- | --- |
0
| 5   | 5   | 5   | 5   | 5   | 5   |
| --- | --- | --- | --- | --- | --- |
| 10  |     |     | 10  | 10  | 10  |
|     | 10  | 10  |     |     |     |
10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 10 5 0 5 10 15 10 5 0 5 10 15 10 5 0 5 10
Original Original Original O r i g i n a l 1.4 Original Original
etamitsE ytisneD ataD 1.0 Kronossmall etamitsE ytisneD ataD 1.0 Kronosbase etamitsE ytisneD ataD 1.0 Kronoslarge etamitsE ytisneD ataD 1.0 Di f f u s i o nTS etamitsE ytisneD ataD TimeVAE etamitsE ytisneD ataD 1.0 TimeGAN
1.2
| 0.8 | 0.8 | 0.8 | 0.8 | 1.0 | 0.8 |
| --- | --- | --- | --- | --- | --- |
| 0.6 | 0.6 | 0.6 | 0.6 | 0.8 | 0.6 |
0.6
| 0.4 | 0.4 | 0.4 | 0.4 |     | 0.4 |
| --- | --- | --- | --- | --- | --- |
0.4
| 0.2 | 0.2 | 0.2 | 0.2 |     | 0.2 |
| --- | --- | --- | --- | --- | --- |
0.2
| 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| --- | --- | --- | --- | --- | --- |
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0
Data Value Data Value Data Value Data Value Data Value Data Value
(c)ForeignExchange(Forex),Dailyfrequency
Figure 14: Visual comparison of generative models on different datasets. Top row in each subfigure: t-SNE embeddings of
original(red)versussynthetic(blue)data.Bottomrowineachsubfigure:KernelDensityEstimates(KDE)oforiginalversus
syntheticdata.

Models Kronos(Ours) Full-shotTimeSeriesModels
Metrics KronosS KronosB KronosL TimeXer TimeMixer iTransformer PatchTST TimesNet DLinear FEDformer NSTransformer
IC 0.0549 0.0564 0.0546 0.0280 0.0291 0.0350 0.0450 0.0424 0.0405 0.0233 0.0433
XSHG
RankIC 0.0375 0.0390 0.0381 0.0053 0.0079 0.0128 0.0088 0.0175 0.0181 0.0107 0.0155
IC 0.0343 0.0322 0.0361 0.0132 0.0097 0.0204 0.0116 0.0174 0.0197 0.0165 0.0253
XNAS
RankIC 0.0155 0.0190 0.0191 0.0106 0.0048 0.0111 0.0083 0.0084 0.0084 −0.0014 0.0016
IC 0.0314 0.0332 0.0360 0.0094 0.0017 0.0137 0.0053 0.0099 0.0118 0.0046 0.0281
XJPX
RankIC 0.0199 0.0209 0.0277 0.0159 0.0036 0.0271 0.0056 0.0127 0.0149 0.0024 0.0212
IC 0.0634 0.0648 0.0634 −0.0055 0.0094 −0.0252 0.0082 0.0566 0.0024 0.0063 0.0514
XNSE
RankIC 0.0434 0.0464 0.0486 −0.0371 0.0024 −0.0248 0.0084 0.0379 −0.0024 0.0003 0.0225
IC 0.0550 0.0575 0.0567 −0.0328 0.0036 −0.0442 0.0248 0.0416 0.0001 −0.0070 0.0416
XKRX
RankIC 0.0362 0.0393 0.0373 −0.0160 0.0033 −0.0284 0.0214 0.0285 0.0006 −0.0049 0.0058
IC 0.0435 0.0439 0.0428 0.0318 0.0322 0.0336 0.0401 0.0333 0.0392 0.0296 0.0366
XHKG
RankIC 0.0226 0.0236 0.0228 −0.0051 −0.0009 −0.0021 −0.0068 −0.0040 −0.0009 −0.0078 −0.0017
IC 0.0551 0.0551 0.0573 −0.0139 0.0116 −0.0233 0.0194 0.0468 0.0158 0.0169 0.0381
XIDX
RankIC 0.0214 0.0216 0.0223 0.0025 0.0046 0.0011 0.0149 0.0171 0.0037 0.0084 0.0051
IC 0.0411 0.0408 0.0466 −0.0283 0.0079 −0.0281 −0.0037 0.0341 0.0306 −0.0102 0.0101
XKLS
RankIC 0.0215 0.0149 0.0167 0.0051 0.0171 0.0024 −0.0078 −0.0025 0.0208 −0.0169 −0.0103
IC 0.0424 0.0443 0.0448 0.0282 0.0197 0.0275 0.0328 0.0312 0.0394 0.0249 0.0334
XTAI
RankIC 0.0301 0.0320 0.0342 −0.0042 0.0015 0.0111 0.0147 0.0095 0.0192 0.0059 0.0129
IC 0.0247 0.0209 0.0211 0.0105 0.0128 0.0155 0.0149 0.0192 0.0137 0.0081 0.0164
Crypto
RankIC 0.0138 0.0135 0.0129 0.0022 0.0038 0.0134 0.0192 0.0146 0.0040 0.0000 0.0096
IC 0.0279 0.0292 0.0244 0.0124 0.0102 0.0142 0.0158 0.0167 0.0227 0.0153 0.0228
Forex
RankIC 0.0177 0.0141 0.0137 0.0134 0.0128 0.0090 0.0085 0.0175 0.0168 0.0120 0.0079
IC 0.0431 0.0435 0.0440 0.0048 0.0134 0.0036 0.0195 0.0317 0.0214 0.0117 0.0316
Average
RankIC 0.0254 0.0258 0.0267 −0.0007 0.0055 0.0030 0.0087 0.0143 0.0094 0.0008 0.0082
1stCount 4 7 10 0 0 0 1 0 0 0 0
Table14:Fullresultsofpriceseriesforecastingexperiments(Part1):Ourmodel(Kronos)andfull-shottimeseriesmodels.A
higherICorRankICindicatesabetterprediction.Bestandsecondbestresultsaremarkedwithredunderlineandblueunderline,
respectively.
Models Zero-shotTimeSeriesModels
Metrics Time-MOES Time-MOEB MoiraiS MoiraiB MoiraiL TimesFM MomentS MomentB MomentL ChronosS ChronosB ChronosL
IC 0.0463 0.0493 −0.0007 −0.0005 −0.0002 0.0174 0.0028 −0.0032 −0.0009 0.0147 0.0069 0.0195
XSHG
RankIC 0.0304 0.0317 0.0000 −0.0012 0.0003 0.0020 0.0003 −0.0037 −0.0017 −0.0026 −0.0108 0.0025
IC −0.0032 −0.0045 −0.0008 −0.0005 0.0000 0.0076 0.0010 −0.0023 −0.0003 −0.0025 −0.0005 0.0020
XNAS
RankIC −0.0033 −0.0042 −0.0008 0.0013 0.0007 0.0112 −0.0015 −0.0027 −0.0007 −0.0001 0.0008 0.0030
IC 0.0268 0.0280 0.0012 0.0004 0.0000 0.0076 −0.0010 −0.0003 −0.0027 0.0117 0.0113 0.0067
XJPX
RankIC 0.0228 0.0230 0.0025 0.0019 0.0016 0.0073 −0.0031 0.0010 −0.0006 0.0110 0.0123 0.0070
IC 0.0173 0.0190 −0.0005 −0.0008 −0.0006 0.0025 0.0063 −0.0129 −0.0039 −0.0012 −0.0049 0.0014
XNSE
RankIC 0.0155 0.0169 −0.0021 −0.0021 −0.0029 0.0009 0.0060 −0.0104 −0.0055 −0.0041 −0.0066 −0.0005
IC 0.0113 0.0141 −0.0014 0.0006 −0.0011 −0.0105 0.0056 −0.0083 −0.0114 −0.0009 −0.0018 0.0061
XKRX
RankIC 0.0088 0.0118 −0.0020 0.0006 −0.0002 −0.0097 0.0041 −0.0082 −0.0069 −0.0006 −0.0009 0.0072
IC 0.0174 0.0189 0.0000 −0.0001 −0.0013 0.0117 0.0013 −0.0050 −0.0003 0.0159 0.0140 0.0166
XHKG
RankIC 0.0186 0.0201 0.0003 0.0031 0.0011 0.0058 −0.0034 −0.0013 0.0009 0.0190 0.0179 0.0192
IC −0.0053 −0.0052 −0.0009 −0.0009 −0.0003 0.0026 0.0052 −0.0094 −0.0007 0.0021 0.0042 0.0080
XIDX
RankIC 0.0002 0.0000 0.0008 0.0012 0.0007 0.0042 −0.0015 −0.0029 0.0014 0.0087 0.0122 0.0153
IC 0.0123 0.0125 −0.0003 −0.0028 0.0005 0.0106 0.0045 −0.0093 −0.0065 −0.0080 −0.0076 −0.0077
XKLS
RankIC 0.0112 0.0135 0.0010 0.0027 0.0047 −0.0052 0.0000 0.0017 −0.0031 0.0113 0.0118 0.0114
IC 0.0296 0.0292 0.0005 0.0001 −0.0004 −0.0002 0.0025 −0.0047 −0.0046 0.0028 −0.0002 0.0080
XTAI
RankIC 0.0234 0.0224 0.0011 0.0013 0.0003 −0.0028 0.0001 −0.0023 −0.0009 0.0088 0.0060 0.0125
IC 0.0054 0.0037 −0.0008 −0.0006 −0.0004 −0.0009 −0.0002 −0.0004 −0.0030 −0.0114 −0.0129 −0.0096
Crypto
RankIC 0.0069 0.0050 0.0004 0.0011 0.0000 0.0014 −0.0011 −0.0061 −0.0007 −0.0051 −0.0061 −0.0045
IC 0.0265 0.0267 −0.0011 −0.0011 0.0000 0.0092 −0.0007 0.0008 0.0024 0.0176 0.0143 0.0155
Forex
RankIC 0.0115 0.0114 −0.0010 0.0005 −0.0003 0.0076 −0.0014 −0.0010 0.0022 0.0168 0.0147 0.0127
IC 0.0168 0.0174 −0.0004 −0.0006 −0.0003 0.0052 0.0025 −0.0050 −0.0029 0.0037 0.0021 0.0060
Average
RankIC 0.0133 0.0138 0.0000 0.0009 0.0005 0.0021 −0.0001 −0.0033 −0.0014 0.0057 0.0047 0.0078
1stCount 0 0 0 0 0 0 0 0 0 0 0 0
Table 15: Full results of price series forecasting experiments (Part 2): Zero-shot time series models. A higher IC or RankIC
indicatesabetterprediction.Bestandsecondbestresultsaremarkedwithredunderlineandblueunderline,respectively.

Models Kronos(Ours) Full-shotTimeSeriesModels
Metrics KronosS KronosB KronosL TimeXer TimeMixer iTransformer PatchTST TimesNet DLinear FEDformer NSTransformer
IC 0.0677 0.0652 0.0662 0.0456 0.0114 0.0371 0.0467 0.0563 0.0626 0.0589 0.0777
XSHG
RankIC 0.0617 0.0653 0.0642 0.0306 −0.0072 0.0266 0.0437 0.0421 0.0461 0.0568 0.0595
IC 0.0563 0.0626 0.0639 0.0051 0.0270 0.0340 0.0569 −0.0193 0.0144 0.0219 0.0377
XNAS
RankIC 0.0513 0.0544 0.0601 0.0061 0.0204 0.0251 0.0446 0.0352 0.0518 0.0254 0.0335
IC 0.0618 0.0667 0.0668 0.0309 0.0211 0.0439 0.0655 0.0656 0.0621 0.0409 0.0436
XJPX
RankIC 0.0583 0.0623 0.0687 0.0474 0.0145 0.0399 0.0446 0.0556 0.0253 0.0373 0.0428
IC 0.0501 0.0523 0.0585 −0.0021 −0.0126 0.0117 0.0216 0.0238 0.0144 0.0238 0.0314
XNSE
RankIC 0.0541 0.0550 0.0639 0.0031 0.0044 0.0146 0.0238 0.0277 0.0442 0.0130 0.0312
IC 0.0749 0.0778 0.0792 0.0389 0.0253 0.0309 0.0589 0.0844 0.0704 0.0726 0.0754
XKRX
RankIC 0.0707 0.0763 0.0790 −0.0024 −0.0071 0.0282 0.0422 0.0801 0.0439 0.0354 0.0792
IC 0.0678 0.0661 0.0654 0.0666 −0.0276 0.0106 0.0470 0.0276 0.0404 0.0496 0.0210
XHKG
RankIC 0.0671 0.0646 0.0703 0.0707 −0.0063 0.0091 0.0631 0.0288 0.0558 0.0605 0.0264
IC 0.0998 0.0990 0.1046 0.0039 −0.0095 0.0393 0.0003 0.0301 0.0195 −0.0007 0.0244
XIDX
RankIC 0.0943 0.0924 0.1007 −0.0111 −0.0018 0.0341 0.0280 0.0304 0.0184 0.0358 0.0610
IC 0.1213 0.1153 0.1359 0.0144 0.0074 0.0252 0.0605 0.0941 0.0781 −0.0016 0.1046
XKLS
RankIC 0.1047 0.1009 0.1145 −0.0261 0.0097 0.0237 0.0685 0.0712 0.0800 −0.0050 0.0851
IC 0.0549 0.0524 0.0511 0.0382 −0.0038 0.0313 0.0421 0.0216 0.0514 0.0489 0.0143
XTAI
RankIC 0.0597 0.0584 0.0609 0.0404 −0.0027 0.0163 0.0363 0.0261 0.0431 0.0444 0.0159
IC 0.0373 0.0376 0.0368 0.0286 0.0250 0.0372 0.0163 0.0348 0.0446 0.0065 0.0274
Crypto
RankIC 0.0332 0.0336 0.0333 0.0154 0.0135 0.0151 0.0213 0.0272 0.0283 0.0027 0.0111
IC 0.0398 0.0555 0.0441 0.0079 0.0203 0.0266 0.0124 0.0054 0.0254 0.0146 0.0122
Forex
RankIC 0.0289 0.0343 0.0274 0.0275 0.0322 0.0152 0.0148 0.0037 0.0279 0.0148 0.0169
IC 0.0665 0.0682 0.0702 0.0253 0.0076 0.0298 0.0389 0.0386 0.0439 0.0305 0.0427
Average
RankIC 0.0622 0.0634 0.0675 0.0183 0.0063 0.0225 0.0392 0.0389 0.0423 0.0292 0.0421
1stCount 2 3 10 1 0 0 0 2 1 0 1
Table16:Fullresultsofreturnforecastingexperiments(Part1):Ourmodel(Kronos)andfull-shottimeseriesmodels.Ahigher
IC or RankIC indicates a better prediction. Best and second best results are marked with redunderline and blueunderline,
respectively.
Models Zero-shotTimeSeriesModels
Metrics Time-MOES Time-MOEB MoiraiS MoiraiB MoiraiL TimesFM MomentS MomentB MomentL ChronosS ChronosB ChronosL
IC 0.0507 0.0501 0.0507 0.0579 0.0534 0.0322 0.0575 0.0579 0.0575 −0.0152 −0.0055 −0.0019
XSHG
RankIC 0.0612 0.0621 0.0657 0.0647 0.0661 0.0445 0.0527 0.0530 0.0525 −0.0277 −0.0116 −0.0048
IC 0.0416 0.0399 0.0275 0.0281 0.0271 0.0226 0.0290 0.0288 0.0287 0.0545 0.0504 0.0572
XNAS
RankIC 0.0480 0.0457 0.0280 0.0290 0.0304 0.0271 0.0300 0.0297 0.0296 0.0448 0.0405 0.0461
IC 0.0639 0.0642 0.0441 0.0417 0.0446 0.0498 0.0509 0.0508 0.0512 0.0326 0.0323 0.0276
XJPX
RankIC 0.0473 0.0487 0.0790 0.0790 0.0793 0.0579 0.0490 0.0491 0.0493 0.0175 0.0174 0.0126
IC 0.0348 0.0343 0.0356 0.0357 0.0354 0.0068 0.0356 0.0357 0.0354 0.0190 0.0179 0.0168
XNSE
RankIC 0.0476 0.0483 0.0518 0.0518 0.0514 0.0180 0.0518 0.0518 0.0514 0.0116 0.0175 0.0161
IC 0.0573 0.0566 0.0545 0.0546 0.0512 0.0392 0.0545 0.0546 0.0544 0.0523 0.0508 0.0532
XKRX
RankIC 0.0599 0.0592 0.0617 0.0619 0.0545 0.0465 0.0617 0.0619 0.0618 0.0348 0.0347 0.0394
IC 0.0373 0.0385 0.0324 0.0314 0.0304 0.0281 0.0358 0.0357 0.0357 0.0271 0.0286 0.0297
XHKG
RankIC 0.0439 0.0431 0.0485 0.0487 0.0486 0.0369 0.0485 0.0487 0.0486 0.0315 0.0331 0.0328
IC 0.0611 0.0565 0.0487 0.0475 0.0474 0.0555 0.0487 0.0488 0.0489 0.0514 0.0560 0.0615
XIDX
RankIC 0.0638 0.0597 0.0586 0.0586 0.0587 0.0582 0.0586 0.0586 0.0587 0.0404 0.0486 0.0522
IC 0.0971 0.0963 0.0815 0.0782 0.0852 0.0585 0.0856 0.0854 0.0854 0.0804 0.0788 0.0772
XKLS
RankIC 0.0954 0.0952 0.1004 0.1001 0.0999 0.0710 0.0803 0.0800 0.0799 0.0723 0.0698 0.0697
IC 0.0386 0.0369 0.0418 0.0414 0.0412 0.0332 0.0418 0.0414 0.0412 0.0361 0.0359 0.0338
XTAI
RankIC 0.0238 0.0202 0.0494 0.0488 0.0487 0.0505 0.0394 0.0388 0.0387 0.0264 0.0326 0.0312
IC 0.0291 0.0293 −0.0051 −0.0081 −0.0046 −0.0042 −0.0042 −0.0039 −0.0043 0.0041 0.0067 0.0107
Crypto
RankIC 0.0122 0.0112 0.0157 0.0172 0.0159 0.0105 0.0058 0.0071 0.0059 −0.0069 −0.0064 0.0009
IC 0.0334 0.0336 0.0355 0.0357 0.0347 0.0353 0.0155 0.0157 0.0157 0.0289 0.0255 0.0274
Forex
RankIC 0.0217 0.0215 0.0262 0.0264 0.0264 0.0276 0.0162 0.0164 0.0164 0.0194 0.0218 0.0184
IC 0.0495 0.0487 0.0407 0.0404 0.0405 0.0325 0.0410 0.0410 0.0409 0.0337 0.0343 0.0357
Average
RankIC 0.0477 0.0468 0.0532 0.0533 0.0527 0.0408 0.0449 0.0450 0.0448 0.0240 0.0271 0.0286
1stCount 0 0 0 0 2 0 0 0 0 0 0 0
Table17:Fullresultsofreturnforecastingexperiments(Part2):Zero-shottimeseriesmodels.AhigherICorRankICindicates
abetterprediction.Bestandsecondbestresultsaremarkedwithredunderlineandblueunderline,respectively.

Models Kronos(Ours) Full-shotTimeSeriesModels Eco.VolatilityModels
Metrics KronosS KronosB KronosL TimeXer TimeMixer iTransformer PatchTST TimesNet DLinear FEDformer NSTransformer ARCH GARCH
MAE 0.0199 0.0205 0.0203 0.0510 0.0349 0.0593 0.0356 0.0348 0.0398 0.0231 0.0348 0.0247 0.0219
XSHG R2 0.2597 0.2630 0.2809 0.1500 0.1585 0.2191 0.2401 0.1429 0.2400 0.2301 0.1232 0.1969 0.1986
MAE 0.1540 0.1407 0.1503 0.3323 0.3473 0.3223 0.2926 0.2492 0.2416 0.2223 0.2168 0.1472 0.1259
XNAS R2 0.1169 0.0961 0.0978 0.0819 0.0071 0.0876 0.1036 0.0452 0.1192 0.0512 0.0963 0.2174 0.2271
MAE 0.0198 0.0198 0.0196 0.1309 0.1324 0.0425 0.0842 0.0365 0.1527 0.0316 0.0353 0.0320 0.0271
XJPX R2 0.1626 0.1912 0.1996 0.1818 0.0229 0.1245 0.0383 0.1277 0.0133 0.0467 0.1531 0.2421 0.2434
MAE 0.0264 0.0269 0.0267 0.0667 0.0347 0.0502 0.0784 0.0555 0.1272 0.0614 0.0497 0.0269 0.0271
XNSE R2 0.1803 0.1445 0.1815 0.1184 0.0708 0.1140 0.0153 0.0486 0.0152 0.0286 0.0365 0.1424 0.1548
MAE 0.0271 0.0255 0.0246 0.0332 0.0424 0.0408 0.0449 0.0537 0.0608 0.0715 0.0552 0.0347 0.0316
XKRX R2 0.5936 0.6190 0.6156 0.1966 0.0175 0.1967 0.1792 0.2695 0.0795 0.0842 0.2223 0.4617 0.4641
MAE 0.0352 0.0402 0.0349 0.0435 0.0746 0.0679 0.0547 0.0608 0.0529 0.0702 0.0499 0.0464 0.0402
XHKG R2 0.1935 0.1875 0.1824 0.1423 0.0515 0.0394 0.0408 0.0396 0.0482 0.0176 0.0051 0.3294 0.3295
MAE 0.0566 0.0544 0.0501 0.1412 0.2504 0.0925 0.0728 0.0827 0.1263 0.0987 0.0836 0.0647 0.0592
XIDX R2 0.1275 0.1884 0.1467 0.1443 0.0163 0.1730 0.0433 0.1053 0.0322 0.0391 0.1065 0.2209 0.2092
MAE 0.0370 0.0367 0.0376 0.1570 0.0823 0.0456 0.1355 0.0759 0.0533 0.0787 0.0827 0.0397 0.0406
XKLS R2 0.5369 0.4781 0.4967 0.1867 0.1378 0.2245 0.1201 0.1409 0.0529 0.0540 0.1172 0.2148 0.2247
MAE 0.0217 0.0220 0.0213 0.0230 0.0254 0.0267 0.0229 0.0318 0.0262 0.0223 0.0271 0.0263 0.0240
XTAI R2 0.2607 0.2074 0.2915 0.1755 0.1797 0.1740 0.2171 0.1591 0.2592 0.1853 0.1783 0.2021 0.2320
MAE 0.0147 0.0148 0.0145 0.1438 0.0705 0.0346 0.0926 0.0289 0.0446 0.0642 0.0375 0.0286 0.0292
Crypto R2 0.1772 0.2179 0.2658 0.0468 0.0711 0.1212 0.1475 0.2372 0.0547 0.0286 0.1095 0.1642 0.1575
MAE 0.0097 0.0074 0.0069 0.0277 0.0277 0.0205 0.0300 0.0187 0.0212 0.0171 0.0176 0.0219 0.0185
Forex R2 0.1301 0.1235 0.1277 0.0002 0.0302 0.0290 0.0270 0.0029 0.0901 0.0382 0.0034 0.1169 0.1141
MAE 0.0384 0.0372 0.0370 0.1046 0.1021 0.0730 0.0858 0.0662 0.0861 0.0692 0.0627 0.0448 0.0405
Average R2 0.2490 0.2470 0.2624 0.1295 0.0694 0.1366 0.1066 0.1199 0.0913 0.0731 0.1047 0.2281 0.2323
1stCount 4 2 11 0 0 0 0 0 0 0 0 1 3
Table 18: Full results of realized volatility forecasting experiments (Part 1): Our model (Kronos) and full-shot time series
models.AlowerMAEorhigherR2 indicatesabetterprediction.Bestandsecondbestresultsaremarkedwithredunderline
andblueunderline,respectively.
Models Zero-shotTimeSeriesModels
Metrics Time-MOES Time-MOEB MoiraiS MoiraiB MoiraiL TimesFM MomentS MomentB MomentL ChronosS ChronosB ChronosL
MAE 0.0462 0.0471 0.1158 0.0994 0.1048 0.0408 0.0357 0.0343 0.0366 0.0386 0.0384 0.0382
XSHG
R2 0.2423 0.2417 0.2118 0.2233 0.2191 0.0995 0.2479 0.2461 0.2336 0.1946 0.1922 0.1663
MAE 0.2713 0.2498 0.3537 0.1927 0.2502 0.1902 0.1034 0.1020 0.1168 0.1896 0.1863 0.1881
XNAS
R2 0.1255 0.0901 0.1782 0.1228 0.1306 0.0740 0.0872 0.0882 0.0804 0.0811 0.0340 0.0982
MAE 0.0372 0.0367 0.1065 0.0829 0.0878 0.0345 0.0291 0.0278 0.0306 0.0331 0.0331 0.0329
XJPX
R2 0.1392 0.1374 0.1150 0.1541 0.1493 0.1213 0.1489 0.1450 0.01375 0.1812 0.1794 0.1769
MAE 0.0420 0.0415 0.1029 0.0873 0.0924 0.0437 0.0364 0.0358 0.0397 0.0414 0.0413 0.0411
XNSE
R2 0.0411 0.0457 0.0455 0.0588 0.0554 0.0394 0.0483 0.0468 0.0422 0.0454 0.0563 0.0439
MAE 0.0452 0.0447 0.1109 0.0909 0.0982 0.0508 0.0418 0.0413 0.0461 0.0485 0.0484 0.0482
XKRX
R2 0.2248 0.2321 0.2235 0.2576 0.2229 0.1249 0.2914 0.2811 0.2588 0.3357 0.3371 0.3132
MAE 0.0701 0.0671 0.1824 0.1367 0.1499 0.0551 0.0500 0.0475 0.0499 0.0526 0.0523 0.0521
XHKG
R2 0.1757 0.1475 0.0900 0.1838 0.1576 0.1862 0.1537 0.1502 0.1432 0.1064 0.1018 0.1090
MAE 0.0725 0.0718 0.2321 0.1687 0.1876 0.0766 0.0652 0.0695 0.0663 0.0744 0.0735 0.0732
XIDX
R2 0.1558 0.1572 0.1228 0.1118 0.1144 0.0952 0.1607 0.1093 0.1471 0.1445 0.1820 0.1692
MAE 0.0572 0.0553 0.1142 0.0914 0.1037 0.0733 0.0571 0.0597 0.0699 0.0706 0.0705 0.0703
XKLS
R2 0.0828 0.1021 0.1451 0.1559 0.1669 0.0541 0.1714 0.1725 0.1393 0.1673 0.1745 0.1645
MAE 0.0387 0.0384 0.1047 0.0900 0.0954 0.0386 0.0335 0.0319 0.0341 0.0371 0.0369 0.0366
XTAI
R2 0.1901 0.1913 0.1611 0.1704 0.1729 0.0789 0.1885 0.1850 0.1672 0.1868 0.1804 0.1588
MAE 0.0374 0.0373 0.0570 0.0574 0.0572 0.0352 0.0209 0.0236 0.0327 0.0341 0.0340 0.0339
Crypto
R2 0.1416 0.1387 0.1061 0.1004 0.2016 0.0881 0.1685 0.1310 0.1758 0.1566 0.1608 0.1584
MAE 0.0225 0.0110 0.0119 0.0151 0.0120 0.0171 0.0151 0.0155 0.0158 0.0102 0.0124 0.0218
Forex
R2 0.1173 0.0286 0.0145 0.0306 0.0504 0.0141 0.0744 0.0592 0.0717 0.0391 0.0245 0.0453
MAE 0.0673 0.0637 0.1356 0.1011 0.1127 0.0596 0.0444 0.0444 0.0490 0.0573 0.0570 0.0579
Average R2 0.1487 0.1375 0.1285 0.1427 0.1492 0.0887 0.1380 0.1468 0.1339 0.1490 0.1475 0.1458
1stCount 0 0 0 0 0 0 0 1 0 0 0 0
Table 19: Full results of realized volatility forecasting experiments (Part 2): Zero-shot time series models. A lower MAE
or higher R2 indicates a better prediction. Best and second best results are marked with redunderline and blueunderline,
respectively.

Models Kronos(Ours) Time-seriesGenerativeModels
Metrics Kronos Kronos Kronos DiffusionTS TimeVAE TimeGAN
small base large
15min 0.2313 0.2317 0.2393 0.0885 0.0015 0.2241
XSHG
daily 0.1865 0.2227 0.2105 0.2532 0.0142 0.1193
15min 0.1733 0.1478 0.1788 0.1420 0.0387 0.2689
XTAI
daily 0.2088 0.2023 0.2235 0.1712 0.0097 0.0622
15min 0.4100 0.4185 0.4187 0.3005 0.0637 0.0680
Crypto
daily 0.2792 0.2575 0.2835 0.3188 0.0402 0.2114
15min 0.4783 0.4903 0.4688 0.4112 0.0492 0.4015
Forex
daily 0.3337 0.4363 0.4152 0.3177 0.0295 0.2387
Average 0.2876 0.3009 0.3048 0.2504 0.0308 0.1993
1stCount 0 2 4 2 0 1
Table20:FulldiscriminativescoreresultsforsyntheticK-linegenerationexperiments.Ahigherscoreindicatesabettergener-
ationquality.Bestandsecondbestresultsaremarkedwithredunderlineandblueunderline,respectively.
Models Kronos(Ours) Time-seriesGenerativeModels
Metrics Kronos Kronos Kronos DiffusionTS TimeVAE TimeGAN
small base large
IC 0.0223 0.0231 0.0236 0.0103 0.0098 0.0102
15min
RankIC 0.0144 0.0147 0.0151 0.0087 0.0134 0.0081
XSHG
IC 0.0918 0.0902 0.0845 0.0760 −0.0789 0.0108
daily
RankIC 0.0854 0.0839 0.0796 0.0684 −0.0720 0.0150
IC 0.0230 0.0274 0.0281 0.0074 −0.0118 0.0045
15min
RankIC 0.0226 0.0276 0.0299 0.0037 −0.0092 −0.0003
XTAI
IC 0.0460 0.0437 0.0560 0.0013 −0.0213 0.0118
daily
RankIC 0.0445 0.0431 0.0551 −0.0001 −0.0193 0.0118
IC 0.0237 0.0243 0.0237 −0.0016 −0.0012 0.0096
15min
RankIC 0.0222 0.0231 0.0231 −0.0026 −0.0016 0.0079
Crypto
IC 0.0027 0.0051 0.0037 −0.0085 −0.0130 −0.0330
daily
RankIC 0.0028 0.0049 0.0031 −0.0111 −0.0100 −0.0301
IC 0.0202 0.0172 0.0171 0.0156 −0.0150 0.0095
15min
RankIC 0.0183 0.0158 0.0150 0.0142 −0.0140 0.0094
Forex
IC 0.0044 0.0069 0.0042 0.0016 0.0140 −0.0044
daily
RankIC 0.0042 0.0066 0.0045 0.0007 0.0160 −0.0058
IC 0.0293 0.0297 0.0301 0.0128 −0.0147 0.0024
Average
RankIC 0.0268 0.0275 0.0282 0.0102 −0.0121 0.0020
1stCount 4 4 9 0 2 0
Table 21: Full results of predictive usefulness (IC and RankIC) for synthetic K-line generation experiments. Higher IC and
RankICscoressuggestthegenerateddataismoreusefulforbuildingpredictivefinancialmodels.Bestandsecondbestresults
aremarkedwithredunderlineandblueunderline,respectively.

| 11.3        |     |     | 11.3             |     |     | 11.3        |     |     |
| ----------- | --- | --- | ---------------- | --- | --- | ----------- | --- | --- |
| 11.2        |     |     | 11.2             |     |     | 11.2        |     |     |
| ecirP esolC |     |     | ecirP esolC 11.1 |     |     | ecirP esolC |     |     |
| 11.1        |     |     |                  |     |     | 11.1        |     |     |
| 11.0        |     |     | 11.0             |     |     | 11.0        |     |     |
10.9
| 10.9 |              |     |      |              |     | 10.9              |     |     |
| ---- | ------------ | --- | ---- | ------------ | --- | ----------------- | --- | --- |
| 10.8 | Ground Truth |     | 10.8 | Ground Truth |     | 10.8 Ground Truth |     |     |
10.7 Prediction
| 10.7   | Prediction   |     | 10.6   |              |     | 10.7 Prediction |     |     |
| ------ | ------------ | --- | ------ | ------------ | --- | --------------- | --- | --- |
|        | Ground Truth |     |        | Ground Truth |     | Ground Truth    |     |     |
| 5000   | Prediction   |     | 5000   | Prediction   |     | 5000 Prediction |     |     |
| 4000   |              |     | 4000   |              |     | 4000            |     |     |
| emuloV |              |     | emuloV |              |     | emuloV          |     |     |
| 3000   |              |     | 3000   |              |     | 3000            |     |     |
| 2000   |              |     | 2000   |              |     | 2000            |     |     |
| 1000   |              |     | 1000   |              |     | 1000            |     |     |
| 0      |              |     | 0      |              |     | 0               |     |     |
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400 500
|                  | (a)Kronos    |       |                  | (b)Kronos    |      |                   | (c)Kronos |       |
| ---------------- | ------------ | ----- | ---------------- | ------------ | ---- | ----------------- | --------- | ----- |
|                  |              | small |                  |              | base |                   |           | large |
| 11.3             |              |       | 11.3             |              |      | 11.3              |           |       |
| 11.2             |              |       | 11.2             |              |      | 11.2              |           |       |
| ecirP esolC 11.1 |              |       | ecirP esolC 11.1 |              |      | ecirP esolC 11.1  |           |       |
| 11.0             |              |       | 11.0             |              |      | 11.0              |           |       |
| 10.9             |              |       | 10.9             |              |      | 10.9              |           |       |
| 10.8             | Ground Truth |       | 10.8             | Ground Truth |      | 10.8 Ground Truth |           |       |
| 10.7             | Prediction   |       | 10.7             | Prediction   |      | 10.7 Prediction   |           |       |
| 7000             |              |       | 7000             |              |      | 7000              |           |       |
|                  | Ground Truth |       |                  | Ground Truth |      | Ground Truth      |           |       |
| 6000             | Prediction   |       | 6000             | Prediction   |      | 6000 Prediction   |           |       |
| 5000             |              |       | 5000             |              |      | 5000              |           |       |
| emuloV           |              |       | emuloV           |              |      | emuloV            |           |       |
| 4000             |              |       | 4000             |              |      | 4000              |           |       |
| 3000             |              |       | 3000             |              |      | 3000              |           |       |
| 2000             |              |       | 2000             |              |      | 2000              |           |       |
| 1000             |              |       | 1000             |              |      | 1000              |           |       |
| 0                |              |       | 0                |              |      | 0                 |           |       |
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400 500
|                  | (d)TimeMOE   |       |                  | (e)TimeMOE   |       |                   | (f)TimesFM |     |
| ---------------- | ------------ | ----- | ---------------- | ------------ | ----- | ----------------- | ---------- | --- |
|                  |              | small |                  |              | large |                   |            |     |
| 11.3             |              |       | 11.3             |              |       | 11.3              |            |     |
| ecirP esolC 11.2 |              |       | ecirP esolC 11.2 |              |       | ecirP esolC 11.2  |            |     |
| 11.1             |              |       | 11.1             |              |       | 11.1              |            |     |
| 11.0             |              |       | 11.0             |              |       | 11.0              |            |     |
| 10.9             |              |       | 10.9             |              |       | 10.9              |            |     |
| 10.8             | Ground Truth |       | 10.8             | Ground Truth |       | 10.8 Ground Truth |            |     |
| 10.7             | Prediction   |       | 10.7             | Prediction   |       | 10.7 Prediction   |            |     |
| 7000             |              |       | 7000             |              |       | 7000              |            |     |
|                  | Ground Truth |       |                  | Ground Truth |       | Ground Truth      |            |     |
| 6000             | Prediction   |       | 6000             | Prediction   |       | 6000 Prediction   |            |     |
| 5000             |              |       | 5000             |              |       | 5000              |            |     |
| emuloV           |              |       | emuloV           |              |       | emuloV            |            |     |
| 4000             |              |       | 4000             |              |       | 4000              |            |     |
| 3000             |              |       | 3000             |              |       | 3000              |            |     |
| 2000             |              |       | 2000             |              |       | 2000              |            |     |
| 1000             |              |       | 1000             |              |       | 1000              |            |     |
| 0                |              |       | 0                |              |       | 0                 |            |     |
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400 500
|                  | (g)Chronos   | small |                  | (h)Chronos   | base |                   | (i)Chronos | large |
| ---------------- | ------------ | ----- | ---------------- | ------------ | ---- | ----------------- | ---------- | ----- |
| 11.3             |              |       | 11.3             |              |      | 11.3              |            |       |
| ecirP esolC 11.2 |              |       | ecirP esolC 11.2 |              |      | ecirP esolC 11.2  |            |       |
| 11.1             |              |       | 11.1             |              |      | 11.1              |            |       |
| 11.0             |              |       | 11.0             |              |      | 11.0              |            |       |
| 10.9             |              |       | 10.9             |              |      | 10.9              |            |       |
| 10.8             |              |       | 10.8             |              |      | 10.8              |            |       |
|                  | Ground Truth |       |                  | Ground Truth |      | Ground Truth      |            |       |
| 10.7             | Prediction   |       | 10.7             | Prediction   |      | 10.7 Prediction   |            |       |
| 7000             |              |       | 7000             |              |      | 7000              |            |       |
| 6000             | Ground Truth |       | 6000             | Ground Truth |      | 6000 Ground Truth |            |       |
|                  | Prediction   |       |                  | Prediction   |      | Prediction        |            |       |
| 5000             |              |       | 5000             |              |      | 5000              |            |       |
| emuloV 4000      |              |       | emuloV 4000      |              |      | emuloV 4000       |            |       |
| 3000             |              |       | 3000             |              |      | 3000              |            |       |
| 2000             |              |       | 2000             |              |      | 2000              |            |       |
| 1000             |              |       | 1000             |              |      | 1000              |            |       |
| 0                |              |       | 0                |              |      | 0                 |            |       |
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400 500
|     | (j)iTransformer |     |     | (k)DLinear |     |     | (l)TimesNet |     |
| --- | --------------- | --- | --- | ---------- | --- | --- | ----------- | --- |
Figure 15: Forecasting results for the ‘Close Price’ and ‘Volume’ of China Film Co.,Ltd. (SSE: 600977), based on 5-minute
K-linedata.Themodelusesa400-steplook-backwindowtopredicta120-stephorizon.Bluelinesrepresentthegroundtruths
andredlinesarethemodel’spredictions.

| 90          |              |     | 90          |              |     | 90                |     |     |
| ----------- | ------------ | --- | ----------- | ------------ | --- | ----------------- | --- | --- |
| 88          |              |     | 88          |              |     | 88                |     |     |
| ecirP esolC |              |     | ecirP esolC |              |     | ecirP esolC       |     |     |
| 86          |              |     | 86          |              |     | 86                |     |     |
| 84          |              |     | 84          |              |     | 84                |     |     |
| 82          | Ground Truth |     | 82          | Ground Truth |     | 82 Ground Truth   |     |     |
| 80          | Prediction   |     | 80          | Prediction   |     | 80 Prediction     |     |     |
|             | Ground Truth |     |             | Ground Truth |     | Ground Truth      |     |     |
| 800000      | Prediction   |     | 800000      | Prediction   |     | 800000 Prediction |     |     |
| 600000      |              |     | 600000      |              |     | 600000            |     |     |
| emuloV      |              |     | emuloV      |              |     | emuloV            |     |     |
| 400000      |              |     | 400000      |              |     | 400000            |     |     |
| 200000      |              |     | 200000      |              |     | 200000            |     |     |
| 0           |              |     | 0           |              |     | 0                 |     |     |
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400 500
|               | (a)Kronos    |       |               | (b)Kronos    |      |                   | (c)Kronos |       |
| ------------- | ------------ | ----- | ------------- | ------------ | ---- | ----------------- | --------- | ----- |
|               |              | small |               |              | base |                   |           | large |
| 90            |              |       | 90            |              |      | 90                |           |       |
| 88            |              |       | 88            |              |      | 88                |           |       |
| ecirP esolC   |              |       | ecirP esolC   |              |      | ecirP esolC       |           |       |
| 86            |              |       | 86            |              |      | 86                |           |       |
| 84            |              |       | 84            |              |      | 84                |           |       |
| 82            | Ground Truth |       | 82            | Ground Truth |      | 82 Ground Truth   |           |       |
|               | Prediction   |       |               | Prediction   |      | Prediction        |           |       |
| 80            |              |       | 80            |              |      | 80                |           |       |
|               | Ground Truth |       |               | Ground Truth |      | Ground Truth      |           |       |
| 800000        | Prediction   |       | 800000        | Prediction   |      | 800000 Prediction |           |       |
| emuloV 600000 |              |       | emuloV 600000 |              |      | emuloV 600000     |           |       |
| 400000        |              |       | 400000        |              |      | 400000            |           |       |
| 200000        |              |       | 200000        |              |      | 200000            |           |       |
| 0             |              |       | 0             |              |      | 0                 |           |       |
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400 500
|                | (d)TimeMOE   |       |                | (e)TimeMOE   |       |                   | (f)TimesFM |     |
| -------------- | ------------ | ----- | -------------- | ------------ | ----- | ----------------- | ---------- | --- |
|                |              | small |                |              | large |                   |            |     |
| 90             |              |       | 90             |              |       | 90                |            |     |
| ecirP esolC 88 |              |       | ecirP esolC 88 |              |       | ecirP esolC 88    |            |     |
| 86             |              |       | 86             |              |       | 86                |            |     |
| 84             |              |       | 84             |              |       | 84                |            |     |
| 82             | Ground Truth |       | 82             | Ground Truth |       | 82 Ground Truth   |            |     |
| 80             | Prediction   |       | 80             | Prediction   |       | 80 Prediction     |            |     |
|                | Ground Truth |       |                | Ground Truth |       | Ground Truth      |            |     |
| 800000         | Prediction   |       | 800000         | Prediction   |       | 800000 Prediction |            |     |
| emuloV 600000  |              |       | emuloV 600000  |              |       | emuloV 600000     |            |     |
| 400000         |              |       | 400000         |              |       | 400000            |            |     |
| 200000         |              |       | 200000         |              |       | 200000            |            |     |
| 0              |              |       | 0              |              |       | 0                 |            |     |
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400 500
|                | (g)Chronos   | small |                | (h)Chronos   | base |                     | (i)Chronos | large |
| -------------- | ------------ | ----- | -------------- | ------------ | ---- | ------------------- | ---------- | ----- |
| 90             |              |       | 90             |              |      | 90                  |            |       |
| ecirP esolC 88 |              |       | ecirP esolC 88 |              |      | ecirP esolC 88      |            |       |
| 86             |              |       | 86             |              |      | 86                  |            |       |
| 84             |              |       | 84             |              |      | 84                  |            |       |
| 82             |              |       | 82             |              |      | 82                  |            |       |
|                | Ground Truth |       |                | Ground Truth |      | Ground Truth        |            |       |
| 80             | Prediction   |       | 80             | Prediction   |      | 80 Prediction       |            |       |
| 800000         | Ground Truth |       | 800000         | Ground Truth |      | 800000 Ground Truth |            |       |
|                | Prediction   |       |                | Prediction   |      | Prediction          |            |       |
| emuloV 600000  |              |       | emuloV 600000  |              |      | emuloV 600000       |            |       |
| 400000         |              |       | 400000         |              |      | 400000              |            |       |
| 200000         |              |       | 200000         |              |      | 200000              |            |       |
| 0              |              |       | 0              |              |      | 0                   |            |       |
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400 500
|     | (j)iTransformer |     |     | (k)DLinear |     |     | (l)TimesNet |     |
| --- | --------------- | --- | --- | ---------- | --- | --- | ----------- | --- |
Figure16:Forecastingresultsforthe‘ClosePrice’and‘Volume’ofPopMart(HKEX:09992),basedon5-minuteK-linedata.
Themodelusesa400-steplook-backwindowtopredicta120-stephorizon.Bluelinesrepresentthegroundtruthsandredlines
arethemodel’spredictions.

| 140             |              |     | 140              |     |     | 140              |     |     |
| --------------- | ------------ | --- | ---------------- | --- | --- | ---------------- | --- | --- |
| ecirP esolC 130 |              |     | ecirP esolC 130  |     |     | ecirP esolC 130  |     |     |
| 120             |              |     | 120              |     |     | 120              |     |     |
| 110             |              |     | 110              |     |     | 110              |     |     |
|                 | Ground Truth |     | Ground Truth     |     |     | Ground Truth     |     |     |
| 100             | Prediction   |     | 100 Prediction   |     |     | 100 Prediction   |     |     |
| 1e8             |              |     | 1e8              |     |     | 1e8              |     |     |
| 1.6             | Ground Truth |     | 1.6 Ground Truth |     |     | 1.6 Ground Truth |     |     |
| 1.4             | Prediction   |     | 1.4 Prediction   |     |     | 1.4 Prediction   |     |     |
| emuloV 1.2      |              |     | emuloV 1.2       |     |     | emuloV 1.2       |     |     |
| 1.0             |              |     | 1.0              |     |     | 1.0              |     |     |
| 0.8             |              |     | 0.8              |     |     | 0.8              |     |     |
| 0.6             |              |     | 0.6              |     |     | 0.6              |     |     |
| 0.4             |              |     | 0.4              |     |     | 0.4              |     |     |
| 0.2             |              |     | 0.2              |     |     | 0.2              |     |     |
0 50 100 150 200 250 300 0 50 100 150 200 250 300 0 50 100 150 200 250 300
|                 | (a)Kronos |       |                 | (b)Kronos |      |                 | (c)Kronos |       |
| --------------- | --------- | ----- | --------------- | --------- | ---- | --------------- | --------- | ----- |
|                 |           | small |                 |           | base |                 |           | large |
| 140             |           |       | 140             |           |      | 140             |           |       |
| ecirP esolC 130 |           |       | ecirP esolC 130 |           |      | ecirP esolC 130 |           |       |
| 120             |           |       | 120             |           |      | 120             |           |       |
110
| 110        |              |     | 110              |     |     |                  |     |     |
| ---------- | ------------ | --- | ---------------- | --- | --- | ---------------- | --- | --- |
|            | Ground Truth |     | Ground Truth     |     |     | 100 Ground Truth |     |     |
| 100        | Prediction   |     | 100 Prediction   |     |     | Prediction       |     |     |
| 1e8        |              |     | 1e8              |     |     | 1e8              |     |     |
| 1.6        | Ground Truth |     | 1.6 Ground Truth |     |     | 1.6 Ground Truth |     |     |
| 1.4        | Prediction   |     | 1.4 Prediction   |     |     | 1.4 Prediction   |     |     |
| emuloV 1.2 |              |     | emuloV 1.2       |     |     | emuloV 1.2       |     |     |
| 1.0        |              |     | 1.0              |     |     | 1.0              |     |     |
| 0.8        |              |     | 0.8              |     |     | 0.8              |     |     |
| 0.6        |              |     | 0.6              |     |     | 0.6              |     |     |
| 0.4        |              |     | 0.4              |     |     | 0.4              |     |     |
| 0.2        |              |     | 0.2              |     |     | 0.2              |     |     |
0 50 100 150 200 250 300 0 50 100 150 200 250 300 0 50 100 150 200 250 300
|                 | (d)TimeMOE   |       |                  | (e)TimeMOE |       |                  | (f)TimesFM |     |
| --------------- | ------------ | ----- | ---------------- | ---------- | ----- | ---------------- | ---------- | --- |
|                 |              | small |                  |            | large |                  |            |     |
| 140             |              |       | 140              |            |       | 140              |            |     |
| ecirP esolC 130 |              |       | ecirP esolC 130  |            |       | ecirP esolC 130  |            |     |
| 120             |              |       | 120              |            |       | 120              |            |     |
| 110             |              |       | 110              |            |       | 110              |            |     |
|                 | Ground Truth |       | Ground Truth     |            |       | Ground Truth     |            |     |
| 100             | Prediction   |       | 100 Prediction   |            |       | 100 Prediction   |            |     |
| 1e8             |              |       | 1e8              |            |       | 1e8              |            |     |
| 1.6             | Ground Truth |       | 1.6 Ground Truth |            |       | 1.6 Ground Truth |            |     |
| 1.4             | Prediction   |       | 1.4 Prediction   |            |       | 1.4 Prediction   |            |     |
| emuloV 1.2      |              |       | emuloV 1.2       |            |       | emuloV 1.2       |            |     |
| 1.0             |              |       | 1.0              |            |       | 1.0              |            |     |
| 0.8             |              |       | 0.8              |            |       | 0.8              |            |     |
| 0.6             |              |       | 0.6              |            |       | 0.6              |            |     |
| 0.4             |              |       | 0.4              |            |       | 0.4              |            |     |
| 0.2             |              |       | 0.2              |            |       | 0.2              |            |     |
0 50 100 150 200 250 300 0 50 100 150 200 250 300 0 50 100 150 200 250 300
|                 | (g)Chronos   | small |                  | (h)Chronos | base |                  | (i)Chronos | large |
| --------------- | ------------ | ----- | ---------------- | ---------- | ---- | ---------------- | ---------- | ----- |
| 140             |              |       | 140              |            |      | 140              |            |       |
| ecirP esolC 130 |              |       | ecirP esolC 130  |            |      | ecirP esolC 130  |            |       |
| 120             |              |       | 120              |            |      | 120              |            |       |
| 110             |              |       | 110              |            |      | 110              |            |       |
|                 | Ground Truth |       | Ground Truth     |            |      | Ground Truth     |            |       |
| 100             | Prediction   |       | 100 Prediction   |            |      | 100 Prediction   |            |       |
| 1e8             |              |       | 1e8              |            |      | 1e8              |            |       |
| 1.6             | Ground Truth |       | 1.6 Ground Truth |            |      | 1.6 Ground Truth |            |       |
| 1.4             | Prediction   |       | 1.4 Prediction   |            |      | 1.4 Prediction   |            |       |
| 1.2             |              |       | 1.2              |            |      | 1.2              |            |       |
| emuloV          |              |       | emuloV           |            |      | emuloV           |            |       |
| 1.0             |              |       | 1.0              |            |      | 1.0              |            |       |
| 0.8             |              |       | 0.8              |            |      | 0.8              |            |       |
| 0.6             |              |       | 0.6              |            |      | 0.6              |            |       |
| 0.4             |              |       | 0.4              |            |      | 0.4              |            |       |
| 0.2             |              |       | 0.2              |            |      | 0.2              |            |       |
0 50 100 150 200 250 300 0 50 100 150 200 250 300 0 50 100 150 200 250 300
|     | (j)iTransformer |     |     | (k)DLinear |     |     | (l)TimesNet |     |
| --- | --------------- | --- | --- | ---------- | --- | --- | ----------- | --- |
Figure17:Forecastingresultsforthe‘ClosePrice’and‘Volume’ofNVIDIA(NASDAQ:NVDA),basedon1-hourK-linedata.
Themodelusesa240-steplook-backwindowtopredicta60-stephorizon.Bluelinesrepresentthegroundtruthsandredlines
arethemodel’spredictions.

| 45000             |              |     | 45000             |              |     |     | 45000             |              |     |     |
| ----------------- | ------------ | --- | ----------------- | ------------ | --- | --- | ----------------- | ------------ | --- | --- |
| ecirP esolC 44000 |              |     | ecirP esolC 44000 |              |     |     | ecirP esolC 44000 |              |     |     |
| 43000             |              |     | 43000             |              |     |     | 43000             |              |     |     |
| 42000             |              |     | 42000             |              |     |     | 42000             |              |     |     |
|                   | Ground Truth |     |                   | Ground Truth |     |     |                   | Ground Truth |     |     |
| 41000             |              |     | 41000             |              |     |     | 41000             |              |     |     |
|                   | Prediction   |     |                   | Prediction   |     |     |                   | Prediction   |     |     |
| 100000            | Ground Truth |     | 100000            | Ground Truth |     |     | 100000            | Ground Truth |     |     |
|                   | Prediction   |     |                   | Prediction   |     |     |                   | Prediction   |     |     |
| 80000             |              |     | 80000             |              |     |     | 80000             |              |     |     |
| emuloV 60000      |              |     | emuloV 60000      |              |     |     | emuloV 60000      |              |     |     |
| 40000             |              |     | 40000             |              |     |     | 40000             |              |     |     |
| 20000             |              |     | 20000             |              |     |     | 20000             |              |     |     |
|                   | 0            |     |                   | 0            |     |     |                   | 0            |     |     |
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400 500
|       | (a)Kronos |       |       |     | (b)Kronos |      |       |     | (c)Kronos |       |
| ----- | --------- | ----- | ----- | --- | --------- | ---- | ----- | --- | --------- | ----- |
|       |           | small |       |     |           | base |       |     |           | large |
| 45000 |           |       | 45000 |     |           |      | 46000 |     |           |       |
45000
| ecirP esolC 44000 |     |     | ecirP esolC 44000 |     |     |     | ecirP esolC |     |     |     |
| ----------------- | --- | --- | ----------------- | --- | --- | --- | ----------- | --- | --- | --- |
44000
| 43000 |     |     | 43000 |     |     |     |     |     |     |     |
| ----- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
43000
| 42000  |              |     | 42000  |              |     |     | 42000  |              |     |     |
| ------ | ------------ | --- | ------ | ------------ | --- | --- | ------ | ------------ | --- | --- |
|        | Ground Truth |     |        | Ground Truth |     |     |        | Ground Truth |     |     |
| 41000  | Prediction   |     | 41000  | Prediction   |     |     | 41000  | Prediction   |     |     |
| 100000 | Ground Truth |     | 100000 | Ground Truth |     |     | 100000 | Ground Truth |     |     |
|        | Prediction   |     |        | Prediction   |     |     |        | Prediction   |     |     |
| 80000  |              |     | 80000  |              |     |     | 80000  |              |     |     |
| emuloV |              |     | emuloV |              |     |     | emuloV |              |     |     |
| 60000  |              |     | 60000  |              |     |     | 60000  |              |     |     |
| 40000  |              |     | 40000  |              |     |     | 40000  |              |     |     |
| 20000  |              |     | 20000  |              |     |     | 20000  |              |     |     |
|        | 0            |     |        | 0            |     |     |        | 0            |     |     |
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400 500
|             | (d)TimeMOE |       |                   |     | (e)TimeMOE |       |             |     | (f)TimesFM |     |
| ----------- | ---------- | ----- | ----------------- | --- | ---------- | ----- | ----------- | --- | ---------- | --- |
|             |            | small |                   |     |            | large |             |     |            |     |
| 46000       |            |       | 46000             |     |            |       |             |     |            |     |
| 45000       |            |       | 45000             |     |            |       | 45000       |     |            |     |
| ecirP esolC |            |       |                   |     |            |       | ecirP esolC |     |            |     |
| 44000       |            |       | ecirP esolC 44000 |     |            |       | 44000       |     |            |     |
| 43000       |            |       | 43000             |     |            |       | 43000       |     |            |     |
42000
| 42000  |              |     | 42000  |              |     |     |        |              |     |     |
| ------ | ------------ | --- | ------ | ------------ | --- | --- | ------ | ------------ | --- | --- |
| 41000  | Ground Truth |     | 41000  | Ground Truth |     |     | 41000  | Ground Truth |     |     |
|        | Prediction   |     |        | Prediction   |     |     |        | Prediction   |     |     |
| 100000 | Ground Truth |     | 100000 | Ground Truth |     |     | 100000 | Ground Truth |     |     |
|        | Prediction   |     |        | Prediction   |     |     |        | Prediction   |     |     |
| 80000  |              |     | 80000  |              |     |     | 80000  |              |     |     |
| emuloV |              |     | emuloV |              |     |     | emuloV |              |     |     |
| 60000  |              |     | 60000  |              |     |     | 60000  |              |     |     |
| 40000  |              |     | 40000  |              |     |     | 40000  |              |     |     |
| 20000  |              |     | 20000  |              |     |     | 20000  |              |     |     |
|        | 0            |     |        | 0            |     |     |        | 0            |     |     |
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400 500
|             | (g)Chronos | small |             |     | (h)Chronos | base |             |     | (i)Chronos | large |
| ----------- | ---------- | ----- | ----------- | --- | ---------- | ---- | ----------- | --- | ---------- | ----- |
| 46000       |            |       | 46000       |     |            |      |             |     |            |       |
| 45000       |            |       | 45000       |     |            |      | 45000       |     |            |       |
| ecirP esolC |            |       | ecirP esolC |     |            |      | ecirP esolC |     |            |       |
| 44000       |            |       | 44000       |     |            |      | 44000       |     |            |       |
43000
| 43000        |              |     | 43000        |              |     |     |              |              |     |     |
| ------------ | ------------ | --- | ------------ | ------------ | --- | --- | ------------ | ------------ | --- | --- |
| 42000        |              |     | 42000        |              |     |     | 42000        |              |     |     |
| 41000        | Ground Truth |     | 41000        | Ground Truth |     |     | 41000        | Ground Truth |     |     |
|              | Prediction   |     |              | Prediction   |     |     |              | Prediction   |     |     |
| 100000       |              |     | 100000       |              |     |     | 100000       |              |     |     |
|              | Ground Truth |     |              | Ground Truth |     |     |              | Ground Truth |     |     |
| 80000        | Prediction   |     | 80000        | Prediction   |     |     | 80000        | Prediction   |     |     |
| emuloV 60000 |              |     | emuloV 60000 |              |     |     | emuloV 60000 |              |     |     |
| 40000        |              |     | 40000        |              |     |     | 40000        |              |     |     |
| 20000        |              |     | 20000        |              |     |     | 20000        |              |     |     |
|              | 0            |     |              | 0            |     |     |              | 0            |     |     |
0 100 200 300 400 500 0 100 200 300 400 500 0 100 200 300 400 500
|     | (j)iTransformer |     |     |     | (k)DLinear |     |     |     | (l)TimesNet |     |
| --- | --------------- | --- | --- | --- | ---------- | --- | --- | --- | ----------- | --- |
Figure18:Forecastingresultsforthe‘ClosePrice’and‘Volume’oftheBTC/USDTperpetualcontractonBinance,basedon
15-minute K-line data. The model uses a 360-step look-back window to predict a 120-step horizon. Blue lines represent the
groundtruthsandredlinesarethemodel’spredictions.

| 90             |     |     | 90             |     |     | 90             |     |     |
| -------------- | --- | --- | -------------- | --- | --- | -------------- | --- | --- |
| ecirP esolC 85 |     |     | ecirP esolC 85 |     |     | ecirP esolC 85 |     |     |
| 80             |     |     | 80             |     |     | 80             |     |     |
75
| 75     |              |     | 75     |              |     |                    |     |     |
| ------ | ------------ | --- | ------ | ------------ | --- | ------------------ | --- | --- |
| 70     | Ground Truth |     | 70     | Ground Truth |     | 70 Ground Truth    |     |     |
|        | Prediction   |     |        | Prediction   |     | Prediction         |     |     |
| 65     |              |     | 65     |              |     | 65                 |     |     |
| 80000  | Ground Truth |     | 80000  | Ground Truth |     | 80000 Ground Truth |     |     |
| 70000  | Prediction   |     | 70000  | Prediction   |     | 70000 Prediction   |     |     |
| 60000  |              |     | 60000  |              |     | 60000              |     |     |
| 50000  |              |     | 50000  |              |     | 50000              |     |     |
| emuloV |              |     | emuloV |              |     | emuloV             |     |     |
| 40000  |              |     | 40000  |              |     | 40000              |     |     |
| 30000  |              |     | 30000  |              |     | 30000              |     |     |
| 20000  |              |     | 20000  |              |     | 20000              |     |     |
| 10000  |              |     | 10000  |              |     | 10000              |     |     |
| 0      |              |     | 0      |              |     | 0                  |     |     |
0 20 40 60 80 100 120 140 0 20 40 60 80 100 120 140 0 20 40 60 80 100 120 140
|     | (a)Kronos |       |     | (b)Kronos |      |     | (c)Kronos |       |
| --- | --------- | ----- | --- | --------- | ---- | --- | --------- | ----- |
|     |           | small |     |           | base |     |           | large |
90
| 90  |     |     | 90  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
85
| ecirP esolC 85 |     |     | ecirP esolC 85 |     |     | ecirP esolC 80 |     |     |
| -------------- | --- | --- | -------------- | --- | --- | -------------- | --- | --- |
| 80             |     |     | 80             |     |     |                |     |     |
75
| 75     |              |     | 75     |              |     | 70                |     |     |
| ------ | ------------ | --- | ------ | ------------ | --- | ----------------- | --- | --- |
| 70     | Ground Truth |     | 70     | Ground Truth |     | 65 Ground Truth   |     |     |
|        | Prediction   |     |        | Prediction   |     | 60 Prediction     |     |     |
| 65     |              |     | 65     |              |     |                   |     |     |
| 140000 |              |     | 140000 |              |     | 140000            |     |     |
|        | Ground Truth |     |        | Ground Truth |     | Ground Truth      |     |     |
| 120000 | Prediction   |     | 120000 | Prediction   |     | 120000 Prediction |     |     |
| 100000 |              |     | 100000 |              |     | 100000            |     |     |
| emuloV |              |     | emuloV |              |     | emuloV            |     |     |
| 80000  |              |     | 80000  |              |     | 80000             |     |     |
| 60000  |              |     | 60000  |              |     | 60000             |     |     |
| 40000  |              |     | 40000  |              |     | 40000             |     |     |
| 20000  |              |     | 20000  |              |     | 20000             |     |     |
| 0      |              |     | 0      |              |     | 0                 |     |     |
0 20 40 60 80 100 120 140 0 20 40 60 80 100 120 140 0 20 40 60 80 100 120 140
|                | (d)TimeMOE   |       |                | (e)TimeMOE   |       |                   | (f)TimesFM |     |
| -------------- | ------------ | ----- | -------------- | ------------ | ----- | ----------------- | ---------- | --- |
|                |              | small |                |              | large |                   |            |     |
| 90             |              |       | 90             |              |       | 90                |            |     |
| ecirP esolC 85 |              |       | ecirP esolC 85 |              |       | ecirP esolC 85    |            |     |
| 80             |              |       | 80             |              |       | 80                |            |     |
| 75             |              |       | 75             |              |       | 75                |            |     |
| 70             | Ground Truth |       | 70             | Ground Truth |       | 70 Ground Truth   |            |     |
|                | Prediction   |       |                | Prediction   |       | Prediction        |            |     |
| 65             |              |       | 65             |              |       | 65                |            |     |
| 140000         |              |       | 140000         |              |       | 140000            |            |     |
|                | Ground Truth |       |                | Ground Truth |       | Ground Truth      |            |     |
| 120000         | Prediction   |       | 120000         | Prediction   |       | 120000 Prediction |            |     |
| 100000         |              |       | 100000         |              |       | 100000            |            |     |
| emuloV         |              |       | emuloV         |              |       | emuloV            |            |     |
| 80000          |              |       | 80000          |              |       | 80000             |            |     |
| 60000          |              |       | 60000          |              |       | 60000             |            |     |
| 40000          |              |       | 40000          |              |       | 40000             |            |     |
| 20000          |              |       | 20000          |              |       | 20000             |            |     |
| 0              |              |       | 0              |              |       | 0                 |            |     |
0 20 40 60 80 100 120 140 0 20 40 60 80 100 120 140 0 20 40 60 80 100 120 140
|                | (g)Chronos | small |                | (h)Chronos | base |                | (i)Chronos | large |
| -------------- | ---------- | ----- | -------------- | ---------- | ---- | -------------- | ---------- | ----- |
| 90             |            |       | 90             |            |      | 90             |            |       |
| ecirP esolC 85 |            |       | ecirP esolC 85 |            |      | ecirP esolC 85 |            |       |
| 80             |            |       | 80             |            |      | 80             |            |       |
| 75             |            |       |                |            |      | 75             |            |       |
75
| 70  |              |     |     |              |     | 70            |     |     |
| --- | ------------ | --- | --- | ------------ | --- | ------------- | --- | --- |
|     | Ground Truth |     | 70  | Ground Truth |     | Ground Truth  |     |     |
| 65  | Prediction   |     |     | Prediction   |     | 65 Prediction |     |     |
65
| 140000       |              |     | 140000       |              |     | 140000              |     |     |
| ------------ | ------------ | --- | ------------ | ------------ | --- | ------------------- | --- | --- |
| 120000       | Ground Truth |     | 120000       | Ground Truth |     | 120000 Ground Truth |     |     |
|              | Prediction   |     |              | Prediction   |     | Prediction          |     |     |
| 100000       |              |     | 100000       |              |     | 100000              |     |     |
| emuloV 80000 |              |     | emuloV 80000 |              |     | emuloV 80000        |     |     |
| 60000        |              |     | 60000        |              |     | 60000               |     |     |
| 40000        |              |     | 40000        |              |     | 40000               |     |     |
| 20000        |              |     | 20000        |              |     | 20000               |     |     |
| 0            |              |     | 0            |              |     | 0                   |     |     |
0 20 40 60 80 100 120 140 0 20 40 60 80 100 120 140 0 20 40 60 80 100 120 140
|     | (j)iTransformer |     |     | (k)DLinear |     |     | (l)TimesNet |     |
| --- | --------------- | --- | --- | ---------- | --- | --- | ----------- | --- |
Figure 19: Forecasting results for the ‘Close Price’ and ‘Volume’ of BMW (FWB: BMW), based on daily K-line data. The
modelusesa120-steplook-backwindowtopredicta30-stephorizon.Bluelinesrepresentthegroundtruthsandredlinesare
themodel’spredictions.