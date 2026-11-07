# AYS-Y:1 (Model 1.1) — Passively Safe Thorium Micro-Reactor Core
**Open-Source Fluid-Dynamic Verification & Core Architecture (TRL 3)**

[![License: CERN-OHL-S v2](https://img.shields.io/badge/License-CERN--OHL--S%20v2-blue.svg)](https://ohwr.org/cernohl)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22977539.svg)](https://doi.org/10.5281/zenodo.22977539)
[![OpenFOAM](https://img.shields.io/badge/OpenFOAM-v2312-brightgreen.svg)](https://www.openfoam.com)

---

## 📌 Executive Summary
The **AYS-Y:1 (Model 1.1)** is an advanced 20 MWe (46.5 MWth) passively safe micro-reactor architecture designed to eliminate mechanical control rod dependencies and mitigate single-point failure modes. 

It integrates a **two-phase fluidized bed core** suspended in an optimized non-toxic quaternary fluoride salt (**Opt-4: $^{7}\text{LiF-NaF-KF-CaF}_2$**) paired with a continuous **3D Sugihara Helical Baffle ("Impossible Staircase")** geometry. Under Station Blackout (SBO) conditions, the core passively terminates reactivity ($k_{\text{eff}} \le 0.95$) within 5.1 seconds purely via density differential and gravitational settling.

---

## ⚡ Key Engineering Innovations

* **Non-Toxic Molten Salt Backbone (Opt-4):**
  * Elimination of beryllium toxicity ($BeF_2$-free), significantly reducing test facility and deployment overhead.
  * In-situ $CaF_2$ redox-buffering providing superior passivity against SiC/structural fluorination.
  * Fluid density ($\rho_f \approx 2050 \text{ kg/m}^3$) tuned to $2 \text{ mm}$ TRISO micro-compacts ($\rho_p = 2300 \text{ kg/m}^3$).
* **Sugihara Spiral Cascade Hydrodynamics:**
  * Eliminates core channeling and bubbling instabilities (slugging) via azimuthal velocity distribution ($\theta_h = 33.7^\circ$).
  * Liquid-cushioned tangential flow preventing particulate attrition during continuous multi-year campaigns.
* **Deterministic Passive SBO Shutdown:**
  * Free of moving mechanical actuators or high-pressure squib valves.
  * Complete unpowered settling into an axial subcritical dump well ($D = 260 \text{ mm}$) in $\approx 5.1 \text{ s}$.

---

## 📐 System Specifications

| Parameter | Specification | Units |
| :--- | :--- | :--- |
| **Thermal / Net Electric Rating** | 46.5 / 20.0 | $\text{MW}_{\text{th}} \text{ / } \text{MW}_{\text{e}}$ |
| **Active Core Dimensions** | $\varnothing 600 \times 1200$ | $\text{mm}$ |
| **Subcritical Dump Well** | $\varnothing 260 \times 600$ | $\text{mm}$ |
| **Coolant Matrix** | $^{7}\text{LiF-NaF-KF-CaF}_2$ (44-10-41-5 mol%) | — |
| **Fuel Geometry** | $2.0 \text{ mm}$ TRISO spherical micro-compacts | — |
| **Operating Void Fraction ($\epsilon$)**| $0.70$ (Operational, $k_{\text{eff}} \approx 1.00$) | — |
| **Shutdown Void Fraction ($\epsilon$)** | $0.40$ (Compacted, $k_{\text{eff}} \le 0.95$) | — |
| **Core Inlet / Outlet Temperatures**| 560 / 650 | $^\circ\text{C}$ |
| **Emergency Shutdown Mechanism** | 100% Gravity-Driven Passive Settling | — |

---

## 🛠 Repository Structure
