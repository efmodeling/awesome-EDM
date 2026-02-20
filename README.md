# awesome-EDM [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of **Empirical Dynamical Modeling (EDM)** papers, software, and resources.

EDM is a nonparametric framework for analyzing and forecasting nonlinear dynamical systems
directly from time series data, using state-space reconstruction (Takens' theorem) to
recover attractor geometry without requiring an explicit equation-based model.

> Under active development — contributions welcome!

---

## Contents

- [Foundational Theory](#foundational-theory)
  - [Embedding Theorems](#embedding-theorems)
  - [Chaos and Nonlinear Dynamics](#chaos-and-nonlinear-dynamics)
- [Core Methods](#core-methods)
  - [Simplex Projection](#simplex-projection)
  - [S-map](#s-map)
  - [Convergent Cross Mapping (CCM)](#convergent-cross-mapping-ccm)
  - [Multiview Embedding (MVE)](#multiview-embedding-mve)
  - [Extensions and Variants](#extensions-and-variants)
- [Causality and Inference](#causality-and-inference)
- [Applications](#applications)
  - [Ecology and Fisheries](#ecology-and-fisheries)
  - [Climate Science](#climate-science)
  - [Neuroscience](#neuroscience)
  - [Epidemiology](#epidemiology)
- [Software and Tools](#software-and-tools)
  - [R](#r)
  - [Python](#python)
  - [Julia](#julia)
  - [C++](#c)
- [Reviews and Tutorials](#reviews-and-tutorials)
- [Datasets](#datasets)
- [Events and Communities](#events-and-communities)
- [Mind Map](#mind-map)

---

## Foundational Theory

### Embedding Theorems

- Takens, F. (1981). Detecting strange attractors in turbulence. *Lecture Notes in Mathematics*, 898, 366–381. [DOI](https://doi.org/10.1007/BFb0091924) — **The foundational theorem underpinning all of EDM.**
- Mañé, R. (1981). On the dimension of the compact invariant sets of certain non-linear maps. *Lecture Notes in Mathematics*, 898, 230–242.
- Sauer, T., Yorke, J. A., & Casdagli, M. (1991). Embedology. *Journal of Statistical Physics*, 65, 579–616. [DOI](https://doi.org/10.1007/BF01053745) — *Generalization of Takens' theorem to generic, non-smooth embeddings.*
- Deyle, E. R., & Sugihara, G. (2011). Generalized theorems for nonlinear state space reconstruction. *PLoS ONE*, 6(3), e18295. [DOI](https://doi.org/10.1371/journal.pone.0018295) — *Extends embedding theory to multivariate and partially observed systems.*

### Chaos and Nonlinear Dynamics

- Lorenz, E. N. (1963). Deterministic nonperiodic flow. *Journal of Atmospheric Sciences*, 20(2), 130–141. [DOI](https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2)
- May, R. M. (1976). Simple mathematical models with very complicated dynamics. *Nature*, 261, 459–467. [DOI](https://doi.org/10.1038/261459a0)

---

## Core Methods

### Simplex Projection

- **Sugihara, G., & May, R. M. (1990).** Nonlinear forecasting as a way of distinguishing chaos from measurement error in time series. *Nature*, 344, 734–741. [DOI](https://doi.org/10.1038/344734a0) — **Seminal paper introducing simplex projection.**
- Sugihara, G. (1994). Nonlinear forecasting for the classification of natural time series. *Philosophical Transactions of the Royal Society A*, 348, 477–495. [DOI](https://doi.org/10.1098/rsta.1994.0106)

### S-map

- Sugihara, G. (1994). Nonlinear forecasting for the classification of natural time series. *Philosophical Transactions of the Royal Society A*, 348, 477–495. [DOI](https://doi.org/10.1098/rsta.1994.0106) — *Introduces the S-map (Sequential locally weighted global linear maps).*
- Deyle, E. R., et al. (2016). Tracking and forecasting ecosystem interactions in real time. *Proceedings of the Royal Society B*, 283, 20152258. [DOI](https://doi.org/10.1098/rspb.2015.2258)

### Convergent Cross Mapping (CCM)

- **Sugihara, G., May, R., Ye, H., Hsieh, C. H., Deyle, E., Fogarty, M., & Munch, S. (2012).** Detecting causality in complex ecosystems. *Science*, 338(6106), 496–500. [DOI](https://doi.org/10.1126/science.1227079) — **Landmark paper introducing CCM.**
- Clark, A. T., Ye, H., Isbell, F., Deyle, E. R., Cowles, J., Tilman, G. D., & Sugihara, G. (2015). Spatial convergent cross mapping to detect causal relationships from short time series. *Ecology*, 96(5), 1174–1181. [DOI](https://doi.org/10.1890/14-1479.1)
- Ye, H., Deyle, E. R., Gilarranz, L. J., & Sugihara, G. (2015). Distinguishing time-delayed causal interactions using convergent cross mapping. *Scientific Reports*, 5, 14750. [DOI](https://doi.org/10.1038/srep14750)

### Multiview Embedding (MVE)

- **Ye, H., & Sugihara, G. (2016).** Information leverage in interconnected ecosystems: Overcoming the curse of dimensionality. *Science*, 353(6302), 922–925. [DOI](https://doi.org/10.1126/science.aag0863) — **Introduces MVE; leverages ensemble of library views for improved forecasting.**

### Extensions and Variants

- Cenci, S., Sugihara, G., & Saavedra, S. (2019). Regularized S-maps for inference of population dynamics. *Methods in Ecology and Evolution*, 10(4), 650–660. [DOI](https://doi.org/10.1111/2041-210X.13150)
- Ushio, M., et al. (2018). Fluctuating interaction network and time-varying stability of a natural fish community. *Nature*, 554, 360–363. [DOI](https://doi.org/10.1038/nature25504) — *Extended S-map for interaction network inference.*
- Chang, C.-W., et al. (2021). Varying-coefficient stochastic differential equations with applications in ecology. *Journal of Agricultural, Biological and Environmental Statistics*, 26, 446–463. [DOI](https://doi.org/10.1007/s13253-021-00450-6)

---

## Causality and Inference

- van Nes, E. H., Scheffer, M., Brovkin, V., Lenton, T. M., Ye, H., Deyle, E., & Sugihara, G. (2015). Causal feedbacks in climate change. *Nature Climate Change*, 5, 445–448. [DOI](https://doi.org/10.1038/nclimate2568)
- Cobey, S., & Baskerville, E. B. (2016). Limits to causal inference with state-space reconstruction for infectious disease. *PLoS ONE*, 11(6), e0169050. [DOI](https://doi.org/10.1371/journal.pone.0169050) — *Critical perspective on CCM limitations.*
- Harnack, D., Laminski, E., Schünemann, M., & Pawelzik, K. R. (2017). Topological causality in dynamical systems. *Physical Review Letters*, 119(9), 098301. [DOI](https://doi.org/10.1103/PhysRevLett.119.098301)
- Runge, J., et al. (2019). Inferring causation from time series in Earth system sciences. *Nature Communications*, 10, 2553. [DOI](https://doi.org/10.1038/s41467-019-10105-3) — *Broader survey of causal inference methods; situates CCM.*

---

## Applications

### Ecology and Fisheries

- Hsieh, C. H., Glaser, S. M., Lucas, A. J., & Sugihara, G. (2005). Distinguishing random environmental fluctuations from ecological catastrophes for the North Pacific ecosystem. *Nature*, 435, 336–340. [DOI](https://doi.org/10.1038/nature03553)
- Deyle, E. R., Fogarty, M., Hsieh, C. H., Kaufman, L., MacCall, A. D., Munch, S. B., & Sugihara, G. (2013). Predicting climate effects on Pacific sardine. *PNAS*, 110(16), 6430–6435. [DOI](https://doi.org/10.1073/pnas.1215506110)
- Ye, H., et al. (2015). Equation-free mechanistic ecosystem forecasting using empirical dynamic modeling. *PNAS*, 112(13), E1569–E1576. [DOI](https://doi.org/10.1073/pnas.1417063112)
- Munch, S. B., Rogers, T. L., & Sugihara, G. (2017). Nonlinear dynamics and noise in fisheries recruitment: A global meta-analysis. *Fish and Fisheries*, 18(6), 996–1007. [DOI](https://doi.org/10.1111/faf.12220)
- Ushio, M., Hsieh, C. H., Masuda, R., Deyle, E. R., Ye, H., Chang, C.-W., & Sugihara, G. (2018). Fluctuating interaction network and time-varying stability of a natural fish community. *Nature*, 554, 360–363. [DOI](https://doi.org/10.1038/nature25504)

### Climate Science

- Tsonis, A. A., Deyle, E. R., May, R. M., Sugihara, G., Swanson, K., Verbeten, J. D., & Wang, G. (2015). Dynamical evidence for causality between galactic cosmic rays and interannual variation in global temperature. *PNAS*, 112(11), 3253–3256. [DOI](https://doi.org/10.1073/pnas.1420291112)
- van Nes, E. H., et al. (2015). Causal feedbacks in climate change. *Nature Climate Change*, 5, 445–448. [DOI](https://doi.org/10.1038/nclimate2568)

### Neuroscience

- Tajima, S., Yanagawa, T., Fujii, N., & Toyoizumi, T. (2015). Locally embedded presages of global network bursts. *PNAS*, 112(31), 9723–9728. [DOI](https://doi.org/10.1073/pnas.1418908112)

### Epidemiology

- Cobey, S., & Baskerville, E. B. (2016). Limits to causal inference with state-space reconstruction for infectious disease. *PLoS ONE*, 11, e0169050. [DOI](https://doi.org/10.1371/journal.pone.0169050)

---

## Software and Tools

### R

- **[rEDM](https://github.com/SugiharaLab/rEDM)** — The primary R package for EDM, developed by the Sugihara Lab. [`CRAN`](https://cran.r-project.org/package=rEDM) | [`Docs`](https://ha0ye.github.io/rEDM/)
- **[multispatialCCM](https://cran.r-project.org/package=multispatialCCM)** — CCM for spatially replicated time series (Clark et al., 2015).

### Python

- **[pyEDM](https://github.com/SugiharaLab/pyEDM)** — Official Python/C++ EDM implementation by the Sugihara Lab. [`PyPI`](https://pypi.org/project/pyEDM/)
- **[skccm](https://github.com/nickc1/skccm)** — Scikit-style CCM implementation.
- **[causal-ccm](https://github.com/PrinceJavier/causal_ccm)** — Lightweight CCM for Python users.

### Julia

- **[EDM.jl](https://github.com/JuliaEDM/EDM.jl)** — Julia implementation of EDM methods.

### C++

- **[cppEDM](https://github.com/SugiharaLab/cppEDM)** — Core C++ library underlying pyEDM; high-performance EDM computation.

---

## Reviews and Tutorials

- **Chang, C.-W., Ushio, M., & Hsieh, C.-H. (2017).** Empirical dynamic modeling for beginners. *Ecological Research*, 32(6), 785–796. [DOI](https://doi.org/10.1007/s11284-017-1469-9) — **Recommended starting point.**
- Munch, S. B., Brias, A., Sugihara, G., & Rogers, T. L. (2020). Frequently asked questions about nonlinear dynamics and empirical dynamic modelling. *ICES Journal of Marine Science*, 77(4), 1463–1479. [DOI](https://doi.org/10.1093/icesjms/fsz209)
- Sugihara Lab rEDM vignettes — [Online tutorial](https://ha0ye.github.io/rEDM/)
- EDM Workshop materials — [GitHub](https://github.com/ha0ye/EDM_workshops)

---

## Datasets

- **Maizuru fish community** — Used in Ushio et al. (2018). Time series of 15 fish species from a coastal ecosystem. Available via the `rEDM` package.
- **Pacific sardine/anchovy** — Used in Deyle et al. (2013) and Hsieh et al. (2005). Bundled in `rEDM`.
- **Three-species Lotka–Volterra simulations** — Synthetic benchmark data, reproducible from Chang et al. (2017).
- **rEDM bundled datasets** — Sea surface temperature, anchovy, sardine time series included in the R package.

---

## Events and Communities

- [Sugihara Lab — Scripps Institution of Oceanography, UCSD](https://deepeco.ucsd.edu/)
- [ICES Working Groups on stock assessment and ecosystem modeling](https://www.ices.dk/)
- [Complex Systems Society](https://cssociety.org/)

---

## Mind Map

Generate a visual mind map of the EDM paper landscape:

```bash
pip install matplotlib networkx pyyaml
python generate_mindmap.py
```

See [`generate_mindmap.py`](generate_mindmap.py) and [`papers.yaml`](papers.yaml) for details.

---

## Contributing

Pull requests are welcome! Please:
1. Add entries in the correct section
2. Follow the existing citation format (Author(s), Year, Title, *Venue*, DOI)
3. Annotate landmark papers with a bold introductory note

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

`awesome-EDM` is dedicated to the public domain under [CC0 1.0](LICENSE).
