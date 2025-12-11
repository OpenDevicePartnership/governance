# Open Device Partnership (ODP)

## Steering Committee Application

<img src="jerry-xie.jpg" alt="Portrait" style="width: 150px; height: 150px; border-radius: 75px; display: block; margin: 0 auto;">

<div style="text-align: center;">

### Jerry Xie • Principal Software Engineer • Microsoft

**`jerryxie@microsoft.com` / [GitHub](https://github.com/jerrysxie) / [LinkedIn](https://www.linkedin.com/in/jerry-sxie/)**

**Proposed Term:** Jan 2026 – Dec 2026

**Primary Focus Area:** Secure EC Firmware  

</div>

---

## Professional Background

Jerry Xie is a Principal Software Engineer based in Austin, TX. He has been working in the embedded space for 20 years. For the first 17 years, he developed embedded firmware and Windows/Linux/RTOS device drivers for industrial controllers and test & measurement systems.

In 2022, he joined the WSSI (Windows System Silicon Integration) organization within Microsoft. For the past 3 years, he has been working with Windows OEMs and silicon partners to enable the Windows experience on new hardware platforms. He has been focusing on ensuring the numerous compute elements on silicon platforms work well for Windows and porting Windows drivers to these new platforms. For the past year, he has been heavily involved in Microsoft's Security First Initiative to pivot platform firmware development toward memory-safe languages like Rust and to secure every compute element on the platform starting with the EC (Embedded Controller).

## Value Added to ODP

Working in WSSI puts Jerry in a unique position to align the ODP vision of security and stability for platform firmware between Windows OS, silicon partners, and OEMs. He has been leading the WSSI EC team to develop Rust HAL support and Rust driver support for EC peripherals for ODP. The ODP EC team has been engaging with MCU vendors and IC vendors to encourage the creation of Rust HAL for their components. In collaboration with OEM partners, the ODP EC team designed the initial EC subsystems model and developed an end-to-end proof of concept for ODP v1.0.

Jerry advocated for EC subsystem team formation to distribute ownership and responsibilities in a scalable way. The ODP EC team under his guidance has also established pipelines to audit the Rust crates used to build the EC firmware. To build engagement, Jerry facilitates weekly ODP EC tech forums and helps to onboard EC contributors. Currently he is contributing to shape ODP v2.0's roadmap for EC.

## Strategic Impact & Vision for ODP

Jerry envisions ODP EC becoming the default Rust-based EC firmware architecture. Key goals include:

* Helping partners accelerate their adoption of memory-safe languages like Rust for platform firmware development
* Driving standardization of EC interfaces across SoC-EC for different platforms
* Enabling DICE boot and SPDM as baseline features for EC

Jerry aims to formalize ODP integration across Microsoft's platform firmware stack with a focus on establishing a secure EC baseline implementation that can serve as the root of trust for a Windows system. He hopes to accelerate partners' adoption of ODP EC services and advocate for inbox support for ODP EC services from the Windows OS team. He actively pushes for adoption of memory-safe language like Rust within Microsoft through tech forums and guides.

## Commitments & Outcomes

* Extend EC MCU HAL support beyond IMXRT and add more EC peripheral driver support with vendor contributions
* Flesh out EC subsystem service functionality in ODP
  * Align on unified EC bus interface + protocol for AP communication
  * Make progress toward off-the-shelf, ready-to-run EC implementation for a chosen platform
* DICE boot support for at least 1 MCU family
* Selection of ODP EC SDK hardware platform and develop a prototype
* Engage more partners to join the ODP EC project

## Year in Review (If Renewing)

N/A
