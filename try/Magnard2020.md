PHYSICAL REVIEW LETTERS 125, 260502 (2020)

Editors’ Suggestion Featured in Physics![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.001.png)

Microwave Quantum Link between Superconducting Circuits Housed

in Spatially Separated Cryogenic Systems

<a name="_page0_x53.00_y105.00"></a><a name="_page0_x53.00_y118.00"></a>P. Magnard[ ,](https://orcid.org/0000-0001-9151-6499)1[,*](#_page4_x71.00_y302.00) S. Storz,1 P. Kurpiers[ ,](https://orcid.org/0000-0002-8958-4473)1 J. Sch r, 1 F. Marxer,1 J. L tolf, 1 T. Walter,1 J.-C. Besse[ ,](https://orcid.org/0000-0002-1490-0072)1 M. Gabureac,1![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.002.png)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.003.png)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.004.png)

K. Reuer[ ,](https://orcid.org/0000-0001-6125-9938)1 A. Akin[ ,](https://orcid.org/0000-0003-1242-6466)1 B. Royer[ ,](https://orcid.org/0000-0001-9695-8552)2[,  ](#_page4_x71.00_y346.00)A. Blais,2,3 and A. Wallraff1,4[, ](#_page4_x71.00_y324.00)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.005.png)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.006.png)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.007.png)

1Department of Physics, ETH Z rich, CH-8093 Z rich, Switzerland

2Institut Quantique and Depa· rtement de Physique, Universite· de Sherbrooke, Sherbrooke, Quebec· J1K 2R1, Canada 3Canadian Institute for Advanced Research, Toronto, Ontario M5G 1Z8, Canada

4Quantum Center, ETH Z rich, 8093 Z rich, Switzerland

![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.008.png) (Received 7 August 2020; accepted 16 November 2020; published 21 December 2020)

Superconducting circuits are a strong contender for realizing quantum computing systems and are also successfully used to study quantum optics and hybrid quantum systems. However, their cryogenic operation temperatures and the current lack of coherence-preserving microwave-to-optical conversion solutions have hindered the realization of superconducting quantum networks spanning different cryogenic systems or larger distances. Here, we report the successful operation of a cryogenic waveguide coherently linking transmon qubits located in two dilution refrigerators separated by a physical distance offivemeters. We transfer qubit states and generate entanglement on demand with average transfer and target state fidelities of 85.8% and 79.5%, respectively, between the two nodes of this elementary network. Cryogenic microwave links provide an opportunity to scale up systems for quantum computing and create local area superconducting quantum communication networks over length scales of at least tens of meters.

DOI: [10.1103/PhysRevLett.125.260502](https://doi.org/10.1103/PhysRevLett.125.260502)

Superconducting circuits are an appealing platform to execute quantum information processing algorithms on noisy-intermediate-scale or error-correctable quantum hard- ware [\[1  5\]](#_page4_x53.00_y368.00) and to study fundamental quantum phenomena [\[6  9\]](#_page4_x53.00_y566.00). Today s state-of-the-art superconducting quantum processors contain a few dozen qubits on a single chip, held at cryogenic temperatures in individual dilution refrig- erators. Efforts in qubit integration and packaging[\[10  13\] ](#_page4_x315.00_y80.00)will likely extend the scale of these processors to thousands of qubitsinthe foreseeablefuture.However,limitationssuch asavailablewafersize,refrigeratedspace,andcoolingpower may arise beyond that scale[\[14\]](#_page4_x315.00_y278.00). Therefore, major innova- tions in both device integration and cryogenics are required to realize error-corrected quantum computers able to tackle interesting problems intractable on high-performance com- puting systems, likely requiring millions of qubits[\[15,16\]](#_page4_x315.00_y322.00). Networking quantum processors housed in different cryo- genic nodes may provide a modular solution to scale up quantum computers beyond these limitations [\[17,18\]](#_page4_x315.00_y399.00). The capabilities of quantum computers may be extended by forming clusters of networked processors housed in indi- vidual cryogenic modules similar to the clusters of process- ing units used in the high-performance systems.

One approach to realize such networks is to use micro- wave-to-optical quantum transducers[\[19  22\]](#_page4_x315.00_y487.00) with which superconducting circuits may be entangled with optical photons to communicate over long distances in a fashion similar to single atoms[\[23\]](#_page4_x315.00_y685.00), trapped ions[\[24\]](#_page5_x53.00_y69.00), or defects in diamond [\[25\]](#_page5_x53.00_y113.00). However, despite the constant improvement

of microwave-to-optical transducers, bringing their con- version efficiency, bandwidth, added noise, laser-induced quasiparticle poisoning, and heat loads to practical levels on a single device remains a challenge.

A complementary approach is to connect dilution-refrig- erator-based cryogenic systems with cold, superconducting waveguides [\[26\]](#_page5_x53.00_y168.00). This approach could prove advantageous for distributing quantum computing tasks in local cryo- genic quantum networks, as it would benefit from readily available, fast, deterministic, error-correctable, and high- fidelity chip-to-chip quantum communication schemes with microwave photons [\[26  34\]](#_page5_x53.00_y168.00). In this Letter, we report the realization of such a cryogenic quantum microwave channel between superconducting qubits located in two distinct dilution refrigerator units. Using a photon shaping technique to transfer excitations deterministically[\[28,35\]](#_page5_x53.00_y234.00), we transfer qubit states and generate entanglement on demand between the distant qubits.

Our experimental setup consists of two cryogen-free dilution refrigerators, each of which houses a supercon- ducting circuit with a single qubit cooled to below 20 mK and separated by 5 m (Fig.[1](#_page1_x52.00_y47.00)). The two identically designed circuits have a frequency-tunable transmon qubit, each with relaxation and coherence times T  12  s and

Te  6  s, coupled dispersively to two Purcell1 filtered

2

resonators: one for readout and one for excitation transfer, as shown in green and yellow, respectively, in Fig. [1(b)](#_page1_x52.00_y47.00). The jgi to jei transition frequencies of transmon qubits labeled A and B are tuned to ωq;A=2π ¼ 6.457 GHz and

0031-9007=20=125(26)=260502(7) 260502-1 ' 2020 American Physical Society

PHYSICAL REVIEW LETTERS 125, 260502 (2020)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.009.png)

<a name="_page1_x52.00_y47.00"></a><a name="_page1_x315.00_y47.00"></a>Vacuum Can![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.010.png)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.011.png)

1) (a) 50K

A B 4K ![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.012.png)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.013.png)Still 

5 m BT 

Al WR90 (b) 

ADC & FPGA 

2) N.A AM LM AM N.B 60

< 20 mK

(K) 50

50K

T 40

3\.75

(K) 3.5

coax.-WR90 WR90 4K

T 3.25

signal generator arbitrary pulse synthesizer

900

circulator detection chain with(-out) JPA 850

(mK)

Still 800

FIG. 1. (a) Schematic representation and (b) simplified circuit T) 20

diagram of the experimental setup. Each transmon qubit at nodes

A (red) and B (blue) is connected to two Purcell filteredλ=4 (mK 10

resonators: one for readout (green) and one for excitation transfer BT 0 , , , : temperature sensors (50K, 4K, still, BT) by emission of a shaped photon (yellow). The light blue back- T 0. 1.25 2.5 3.75 5.

ground illustrates the refrigerated space. position, x (m)

260502-2
PHYSICAL REVIEW LETTERS 125, 260502 (2020)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.009.png)

ωq;B=2π ¼ 6.074 GHz, respectively, by applying a mag- netic field to their superconducting quantum interference device loops. This adjusts the dispersive shift on each transfer resonator such that their frequencies ωt=2π ¼

8\.406 GHz are matched[\[28\]](#_page5_x53.00_y234.00). Here, jgi, jei, and jf i denote the three lowest energy levels of the transmon qubit.

We connect the transfer resonators to each other through a 4.9 m long, superconducting, rectangular aluminum WR90 waveguide in series with two flexible, coaxial copper cables of 0.4 m length each and a circulator. At mK temperatures, the waveguide exhibits attenuation below 1 dB=km over the X band (8  12 GHz), which

amounts to a total loss below 10−3 over 4.9 m of the waveguide [\[36\]](#_page5_x53.00_y674.00). With attenuation levels comparable to that of optical photons in telecom fibers[\[44\]](#_page5_x315.00_y432.00), the waveguide is in principle suited for high-fidelity transmission of micro- wave photons over intracity scale distances[\[26\]](#_page5_x53.00_y168.00).

To perform single-qubit gates, we apply microwave pulses created by arbitrary waveform generators to each qubit through dedicated drive lines. To perform readout, we apply a gated microwave tone to the readout resonator. The transmitted signal is then amplified, down-converted, digitized, and processed by a field-programmable gate array (FPGA). Using quantum-limited Josephson para- metric amplifiers (JPA) in the detection chain, we achieve single-shotthree-leveldiscriminationofthetransmonstates with ∼5% average error (10% for joint two-qubit readout). Devices, microwave setup, pulse calibration, and qubit readout are discussed in more detail in the Supplemental Material [\[36\]](#_page5_x53.00_y674.00).

FIG. 2. (a) Longitudinal cross section of a schematic repre- sentation (left half) and a 3D model (right half) of the cryogenic system. Theinset onthe toprightshowsatransverse crosssection of the link. (b) Measured temperature in steady-state vs sensor position x on the axis along the link for all four temperature stages. Nodes A and B: NA and NB; adapter module: AM; link module: LM.

We cool the waveguide to temperatures below 20 mK by mounting it in a custom-made cryogenic system consisting of concentric, octagonal radiation shields held at temper- atures of approximately 50 K, 4 K, 850 mK (still), and 15 mK (base temperature) and installed in an o-ring sealed vacuumcan[Fig.[2(a)](#_page1_x315.00_y47.00)].SeetheSupplementalMaterialfora photograph of the full system [\[36\]](#_page5_x53.00_y674.00). The waveguide is thermalized to the base temperature shield every 0.25 m using flexible copper braids, and the radiation shields are cooled to their equilibrium temperatures using the dilution refrigerators at each end of the system.

The largest heat load on the system is due to room temperature black body radiation, which we mitigate by a set of low-emissivity radiation shields manufactured from high thermal conductivity copper and mechanically sup- ported by thin-walled low thermal conductivity posts. In addition,theheatloadonthe50Kstageisreducedbyusing multilayer insulation [\[45\]](#_page5_x315.00_y476.00). Generally, minimizing the heat flow between shields at different temperature stages and maximizing the thermal conductivity along each stage reduces thermal gradients and thus allows for lower final temperatures. By making the arrangement of shields light- proof, the base temperature shields cool to below 20 mK.

260502-2
PHYSICAL REVIEW LETTERS 125, 260502 (2020)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.009.png)

We designed the link to be modular, with 1.25 m long<a name="_page2_x315.00_y47.00"></a> (a) excitation transfer : 311 ns![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.014.png)

adapter modules to connect the link to each dilution

refrigerator and 2.5 m long link modules, which also allow

for an extension of the link [Fig.[2(a)](#_page1_x315.00_y47.00)]. To compensate for A z

thermal contraction during cooldown, we use flexible

copper braids for thermal anchoring between modules.

For the same reason, flexible coaxial cables are used to

connect the samples to the waveguide.

To monitor the temperature profile of the link, we

installed temperature sensors at the positions indicated in B z

Fig. [2(a)](#_page1_x315.00_y47.00). Three days after commencing cooldown, the

system reaches the steady-state temperature distribution 0 100 200 300 400

shown in Fig. [2(b)](#_page1_x315.00_y47.00), demonstrating the excellent perfor- time, t (ns)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.015.png)

mance of the system. As expected, on each stage, the (b) 1![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.016.png)

temperature is lowest at the nodes and the highest in the

middle of the link, with an exception for the still stage ,P

where we heated node B to 900 mK to optimize cooling .5

power by increasing the flow of 3He.

To characterize the excitation transfer through the link,

Populations

we first reset the transmon qubits with microwave drives 0

[\[46\]](#_page5_x315.00_y509.00) and apply two consecutive Gaussian π pulses to 0 60 120 180 240 prepare the qubit and resonator system at node A in the ![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.017.png)state jf 0i [Fig. [3(a)](#_page2_x315.00_y47.00)], where jqi and jni in jqni denote the truncation time, (ns)

transmon state and the transfer resonator Fock state, respec- FIG. 3. (a) Pulse scheme used to characterize the excitation tively. We then drive transmon A on the jf 0i ↔jg1i transfer dynamics. Thejf 0i →jg1i drives and the g-e and e-f π sideband transition[\[47,48\]](#_page5_x315.00_y564.00) to populate the transfer resonator pulses are represented in blue, gray, and purple, respectively. We with one photon. This photon couples into the waveguide at usesolidanddashedlinesforthetime-truncated(τ ¼ 140 ns)and rate κA=2π ¼ 8.9 MHz and propagates to node B in 28 ns, full excitation transfer sequences, respectively. The straight as estimated from the waveguide length and the relevant yellow lines illustrate the propagation path of the rising and group velocities [\[36\]](#_page5_x53.00_y674.00). We shape the jf 0i ↔ jg1i pulse falling edges of the photon in space-time. The subsequence appropriately to emit the photon with a time-symmetric defining the excitation transfer is enclosed in a gray box. envelope ϕðtÞ∝sechðΓt=2Þ [\[28,48,49\]](#_page5_x53.00_y234.00), where the photon (b) PopulationP in selected two-transmon statesjABi vs jf 0i ↔

jg1i pulse truncation timeτ. Solid lines show the results of master bandwidth Γ can be adjusted up to a maximum value of equation simulations.

min½κA;κB . Here we choose Γ=2π ¼ κB=2π  6.2 MHz to

minimize the duration of the protocol. To absorb the photon

at node B, we then drive transmon B with anjf 0i ↔ jg1i population measured in bothjgfi and jegi (not shown) is pulsewhose timereversewould emit a photonindistinguish- due to e-f decay. In case of photon loss or failed able from the incoming one[\[35\]](#_page5_x53.00_y630.00). Finally, we apply ane-f π absorption during the transfer process, the system ends pulse on transmon B to map the excitation back to theg-e up in the state jggi. Comparing the measured amplitudes manifold and then perform a single-shot readout on both of the fields emitted by A or B using the measurement qutrits. Here and in following experiments, we present data chain behind the circulator [Fig. [1(b)](#_page1_x52.00_y47.00)], we determine a that is corrected for readout errors using reference measure- 22.3% photon loss, dominated by the insertion loss of ments [\[36\]](#_page5_x53.00_y674.00). For these parameters, the excitation transfer the circulator, and a 4.2% absorption inefficiency [\[36\]](#_page5_x53.00_y674.00), sequence, consisting of thejf 0i ↔ jg1i pulses and the final which is in reasonable agreement with the 25.3% residual e-f π pulse, completes in 311 ns. population measured in the statejggi. Finally, the transfer

Truncating the jf 0i ↔ jg1i pulses prematurely at time efficiency is characterized by the 67.5% final population τ, we characterize the time dependence of the state in jgei. The time between the applications of the emission population of the two transmon qubits throughout the and absorption pulses is set to experimentally maximize transfer pulse (Fig. [3](#_page2_x315.00_y47.00)). As the excitation transfers from the transfer efficiency. By comparing the time of arrival of node A to node B via the photonic modes (the waveguide photons emitted from A or B in the photon measurement and both transfer resonators), the population swaps from chain, we determine this optimal time difference to be the state jfgi of the two spatially separated qubits jABi 38 ns, which decomposes into the photon propagation to jgei via the intermediate state jggi. The final two- time and an extra 10 ns lag [\[36\]](#_page5_x53.00_y674.00). Simulations of the transmon state populations highlight the different sources transfer dynamics, using the master equation model from of errors in the excitation transfer. The ∼3% residual Ref. [\[28\]](#_page5_x53.00_y234.00) and independently measured parameters, are in

260502-3
PHYSICAL REVIEW LETTERS 125, 260502 (2020)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.009.png)

good agreement with the data [solid lines in Fig.[3(b)](#_page2_x315.00_y47.00)] and the measured pulse timing [\[36\]](#_page5_x53.00_y674.00).

To probe the quantum nature of the excitation transfer, we characterize the qubit state transfer protocol with quantum process tomography. To do so, we reset the qubits to their ground states, prepare A in one of the six mutually unbiased qubit states[\[50\]](#_page6_x53.00_y47.00), apply an e-f π pulse on A, and then apply an excitation transfer sequence [Fig.[4(a)](#_page3_x52.00_y371.00)]. For transmonfromeach whichinputBstatewewithinferρi;sthree-lethewe transferreconstructvel quantumprocessthe¼ 1statePmatrixfinal tomographystateχ [\[36\]](#_page5_x53.00_y674.00)ρ[ ](#_page5_x53.00_y674.00). Wofe,

f;s determinean average state fidelityF s 6 sF ðρi;s;ρf;sÞ¼

82\.4  0.06% and a process fidelity ofF p ¼ TrðχidealχÞ ¼

75\.3  0.1% relative to the ideal qubit state transfer process. When correcting for readout errors, these fidelities reach 85.8  0.06% and 79.5  0.1%, respec- tively [Fig. [4(b)](#_page3_x52.00_y371.00)]. On average, the input states have equal populations injgi and jei, which are transferred in vacuum states, insensitive to loss, with close-to-unit fidelity, and single-photon Fock states, suffering from loss, with a fidelity of 67.5% corresponding to the transfer efficiency. Therefore, the state transfer fidelitiesF s and F p can be larger than the photon transfer efficiency if the phase coherence of the process is sufficiently large.

![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.018.jpeg)

FIG. 4. (a) Quantum circuit used to perform and characterize the qubit state transfer. (b) Absolute value of the qubit state

transfer matrix jχj in the Pauli basis f1;X¼σ  x;Y  ¼iσ  y;Z¼σ  zg.

3) Quantum circuit used to deterministically generate and characterize the Bell state jψþ i. (d) Expectation value hσiσ i

j of the two-qubit Pauli operators, and (e) real part of the density

matrixρ of reconstructed Bell state. In (b),(d),(e), solid blue bars, redwireframes,and gray wireframes arethemeasured,simulated, and target quantities, respectively.

To generate entanglemep ffiffintffiacross the link, we prepare

qubit A in ðjei þ j f iÞ= 2, qubit B in jgi, and apply the

excitation transfer pulses [Fig.[4(c)](#_page3_x52.00_y371.00)]. Using quantum state tomography, we reconstruct the two-qutrit density matrix

ρ3⊗3 of qubits A and B [\[36\]](#_page5_x53.00_y674.00). To quantify the entanglement

with standard metrics, we consider the density matrixρ,

consisting of the two-qubit elements ofρ3⊗3 [Fig. [4(d)](#_page3_x52.00_y371.00),[(e)](#_page3_x52.00_y371.00)].

We determine the fidelity hψþ jρjψþ i ¼ 79.5  0.1%

(71.9  0.1%) with prespectffiffiffi to the ideal Bell state

jψþ i ¼ ðjgei þ j egiÞ= 2, and evaluate a concurrence of

CðρÞ ¼0.746  0.003 (0.588  0.002), with (without) cor-

rection for readout errors.

Simulations of the qubit state transfer and entanglement

generation sequences are in good agreement with the measuremepnffit ffiresults,ffiffiffiffiasffiquantifffiffiffiffiiedffiffibypffiffiffitheffiffiffiffismallffiffiffiffiffiffitraceffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi distances Trðjχ− χsimj2Þ¼0.09 and Trðjρ − ρsimj2Þ¼

0\.023 between the reconstructed and simulated quantities. These simulations suggest that photon loss and transmon

decay are the dominant sources of errors in these protocols, contributing to 11.8% and ∼6% infidelity, respectively. In

future experiments, the photon loss may be reduced to 5%

by removing the circulator [\[31  34\]](#_page5_x53.00_y410.00), by using a printed

circuit board metalized with a superconductor, and by

using low-loss coaxial cables between the device and

the waveguide. Simulations of the protocols with 5%

photon loss and reasonably improved coherence times

<a name="_page3_x52.00_y371.00"></a>(T  Te  30  s) and transfer resonator bandwidth

1 2

(κ=2π ¼ 12 MHz) indicate that Bell state fidelities and

state transfer process fidelities as high as 96% may be

achievable, which may enable distributed surface-code computation [\[17\]](#_page4_x315.00_y399.00) and communication [\[51\]](#_page6_x53.00_y80.00) between distant

cryogenic nodes. Further improvement may be obtainable

using protocols requiring less time compared to the coher-

ence of the circuit elements[\[31\]](#_page5_x53.00_y410.00) or ones that are resilient to

photon loss [\[33,34,52,53\]](#_page5_x53.00_y520.00) and thermal excitation [\[26,27\]](#_page5_x53.00_y168.00).

This realization of a meter-scale, mK temperature, microwave-frequency coherent quantum link and its use

for quantum state transfer and entanglement generation

suggests a number of directions for future research. For

example, we plan to experimentally investigate the distri-

bution of quantum information processing tasks between

quantum nodes hosting multiple qubits using a coherent

cryogenic network, an essential part of a modular quantum

computer architecture [\[54\]](#_page6_x53.00_y190.00). In addition, the modularity of

the cryogenic link demonstrated here offers a straightfor-

ward path toward extending the physical distance between

nodes by adding modules to the link. Due to the small

photon loss in the superconducting rectangular waveguide,

cryogenic links covering distances of tens or evenhundreds

of meters could be realized, primarily limited by financial

constraints imposed by the thermal requirements. On such

length scales, one may investigate nonlocal physics[\[55,56\]](#_page6_x53.00_y223.00)

or non-Markovian waveguide QED [\[57,58\]](#_page6_x315.00_y168.00) with super-

conducting quantum devices and set the grounds for

microwave quantum local area networks[\[26\]](#_page5_x53.00_y168.00).

260502-4
PHYSICAL REVIEW LETTERS 125, 260502 (2020)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.009.png)

This work is supported by the European Research Council (ERC) through the Superconducting Quantum Networks  (SuperQuNet) project, by the National Centre<a name="_page4_x315.00_y80.00"></a>of Competence in Research Quantum Science and Technology  (NCCR QSIT), a research instrument of the Swiss National Science Foundation (SNSF), by ETH Zurich, by NSERC, the Canada First Research Excellence Fund, and by the Vanier Canada Graduate Scholarships. P.M., S.S., P.K. and T.W. designed and developed the experiment. J.-C.B., T.W. and M.G. fab- ricated the samples. J.L., P.K., P.M., S.S., F.M., and J.S. designed, characterized, and assembled the cryogenic system. P.M., P.K., and S.S. performed the experiments. P.M., P.K., and A.W. analyzed and interpreted the data. P.M., K.R, A.A., J.S., and F.M. implemented the FPGA firmware and experiment automation. B.R., P.M., and P.K. performed the master equation simulations. P.M. and A.W. wrote the manuscript. All authors commented on the manuscript. The project was led by A.W.![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.019.png)

[*](#_page0_x53.00_y105.00)Corresponding author.

<a name="_page4_x71.00_y324.00"></a>paul.magnard@phys.ethz.ch

Corresponding author.

<a name="_page4_x71.00_y346.00"></a>andreas.wallraff@phys.ethz.ch

Present Address: Department of Physics, Yale University, New Haven, Connecticut 06520, USA.

1. J. Preskill, Quantum computing in the NISQ era and beyond, [Quantum 2, 79 (2018)](https://doi.org/10.22331/q-2018-08-06-79).
1. F. Arute et al., Quantum supremacy using a programmable superconducting processor, [Nature (London) 574, 505 (2019)](https://doi.org/10.1038/s41586-019-1666-5).
1. A. Kandala, K. Temme, A.D. C rcoles, A. Mezzacapo, J.M. Chow, and J.M. Gambetta, Error mitigation extends the computational reach of a noisy quantum processor, [Nature (London) 567, 491 (2019)](https://doi.org/10.1038/s41586-019-1040-7).
1. N. Ofek, A. Petrenko, R. Heeres, P. Reinhold, Z. Leghtas,

   2. Vlastakis, Y. Liu, L. Frunzio, S.M. Girvin, L. Jiang, M. Mirrahimi, M.H. Devoret, and R.J. Schoelkopf, Extending the lifetime of a quantum bit with error correction in superconducting circuits,[Nature (London)536, 441 (2016)](https://doi.org/10.1038/nature18949).
1. C.K. Andersen, A. Remm, S. Lazar, S. Krinner, N. Lacroix, G.J. Norris, M. Gabureac, C. Eichler, and A. Wallraff, Repeated quantum error detection in a surface code,[Nat. Phys. 16, 875 (2020)](https://doi.org/10.1038/s41567-020-0920-y).
1. A. van Loo, A. Fedorov, K. Lalumiere,‘ B. Sanders, A. Blais, and A. Wallraff, Photon-mediated interactions between distant articial atoms, [Science 342, 1494 (2013)](https://doi.org/10.1126/science.1244324).
1. S. Hacohen-Gourgy, L.S. Martin, E. Flurin, V.V. Ramasesh, K.B.Whaley,and I.Siddiqi, Quantum dynamics of simultaneously measured non-commuting observables, [Nature (London) 538, 491 (2016)](https://doi.org/10.1038/nature19762).
1. N. Cottet, S. Jezouin, L. Bretheau, P. Campagne-Ibarcq, Q. Ficheux,J.Anders,A.Auffeves,‘ R.Azouit,P.Rouchon,and

   2. Huard, Observing a quantum maxwell demon at work, [Proc. Natl. Acad. Sci. U.S.A. 114, 7561 (2017)](https://doi.org/10.1073/pnas.1704827114).
1. Z.K. Minev, S.O. Mundhada, S. Shankar, P. Reinhold, R. Gutierrez-J· Æuregui, R.J. Schoelkopf, M. Mirrahimi, H.J.

Carmichael, and M.H. Devoret, To catch and reverse a quantum jump mid-flight, [Nature (London) 570, 200 (2019)](https://doi.org/10.1038/s41586-019-1287-z).

10. J.H. Bejan· in, T.G. McConkey,J.R. Rinehart, C.T. Earnest, C.R.H.McRae, D.Shiri, J.D. Bateman,Y.Rohanizadegan,

    2. Penava, P. Breul, S. Royak, M. Zapatka, A.G. Fowler, and M. Mariantoni, Three-Dimensional Wiring for Exten- sible Quantum Computing: The Quantum Socket, [Phys. Rev. Applied 6, 044010 (2016)](https://doi.org/10.1103/PhysRevApplied.6.044010).
10. R.N. Das, J.L. Yoder, D. Rosenberg, D.K. Kim, D. Yost, J. Mallek, D. Hover, V. Bolkhovsky, A.J. Kerman, and W.D. Oliver, Cryogenic qubit integration for quantum computing, in IEEE 68th Electronic Components and Technology Conference (ECTC) (IEEE, San Diego, CA, 2018), <https://dx.doi.org./10.1109/ECTC.2018.00080>.
10. B. Foxen et al., Qubit compatible superconducting inter- connects, [Quantum Sci. Technol. 3, 014005 (2018)](https://doi.org/10.1088/2058-9565/aa94fc).
10. C.U. Lei, L. Krayzman, S. Ganjam, L. Frunzio, and R.J. Schoelkopf, High coherence superconducting microwave cavities with indium bump bonding,[Appl. Phys. Lett. 116, 154002 (2020)](https://doi.org/10.1063/5.0003907)<a name="_page4_x315.00_y278.00"></a>.
10. S. Krinner, S. Storz, P. Kurpiers, P. Magnard, J. Heinsoo, R. <a name="_page4_x71.00_y302.00"></a>Keller, J. L tolf, C. Eichler, and A. Wallraff, Engineering cryogenic setups for 100-qubitscale superconductingcircuit <a name="_page4_x315.00_y322.00"></a>systems, [Eur. Phys. J. Quantum Technol. 6, 2 (2019)](https://doi.org/10.1140/epjqt/s40507-019-0072-0).
10. M. Reiher, N. Wiebe, K.M. Svore, D. Wecker, and M. Troyer, Elucidating reaction mechanisms on quantum com- puters, [Proc. Natl. Acad. Sci. U.S.A. 114, 7555 (2017)](https://doi.org/10.1073/pnas.1619152114).
10. R.<a name="_page4_x53.00_y368.00"></a> Babbush, C. Gidney, D.W. Berry, N. Wiebe, J. McClean,

    2. Paler, A. Fowler, and H. Neven, Encoding Electronic Spectra in Quantum Circuits with Linear T Complexity, <a name="_page4_x315.00_y399.00"></a>[Phys. Rev. X 8, 041015 (2018)](https://doi.org/10.1103/PhysRevX.8.041015).
10. N.H. Nickerson, J.F. Fitzsimons, and S.C. Benjamin, Freely Scalable Quantum Technologies Using Cells of 5- to-50 Qubits with Very Lossy and Noisy Photonic Links, [Phys. Rev. X 4, 041041 (2014)](https://doi.org/10.1103/PhysRevX.4.041041).
10. T. Brecht, W. Pfaff, C. Wang, Y. Chu, L. Frunzio, M.H. Devoret, and R.J. Schoelkopf, Multilayer microwave in- tegrated quantum circuits for scalable quantum computing, <a name="_page4_x315.00_y487.00"></a>[npj Quantum Inf. 2, 16002 (2016)](https://doi.org/10.1038/npjqi.2016.2).
10. L. Fan, C.-L. Zou, R. Cheng, X. Guo, X. Han, Z. Gong, S. Wang, and H.X. Tang, Superconducting cavity electro- optics: A platform for coherent photon conversion between superconducting and photonic circuits, [Sci. Adv. 4, eaar4994 (2018)](https://doi.org/10.1126/sciadv.aar4994).
10. A.P. Higginbotham, P.S. Burns, M.D. Urmey, R.W. <a name="_page4_x53.00_y566.00"></a>Peterson, N.S. Kampel, B.M. Brubaker, G. Smith, K.W. Lehnert, and C.A. Regal, Harnessing electro-optic corre- lations in an efficient mechanical converter,[Nat. Phys. 14, 1038 (2018)](https://doi.org/10.1038/s41567-018-0210-0).
10. M. Forsch, R. Stockill, A. Wallucks, I. Marinković, C. G rtner, R.A. Norte, F. van Otten, A. Fiore, K. Srinivasan, and S. Gr blacher, Microwave-to-optics conversion using a mechanicaloscillatorinitsquantumgroundstate,[Nat.Phys. 16, 69 (2020)](https://doi.org/10.1038/s41567-019-0673-7).
10. M. Mirhosseini, A. Sipahigil, M. Kalaee, and O. Painter, Quantum transduction of optical photons from a super- <a name="_page4_x315.00_y685.00"></a>conducting qubit, [arXiv:2004.04838](https://arXiv.org/abs/2004.04838).
10. J. Hofmann, M. Krug, N. Ortegel, L. Gerard,· M. Weber,

W. Rosenfeld, and H. Weinfurter, Heralded entanglement

260502-5
PHYSICAL REVIEW LETTERS 125, 260502 (2020)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.009.png)

between widely separated atoms, [Science 337, 72 (2012)](https://doi.org/10.1126/science.1221856)<a name="_page5_x53.00_y69.00"></a>.

24. D.L. Moehring, P. Maunz, S. Olmschenk, K.C. Younge, D.N. Matsukevich, L.M. Duan, and C. Monroe, Entangle- ment of single-atom quantum bits at a distance, [Nature (London) 449, 68 (2007)](https://doi.org/10.1038/nature06118)<a name="_page5_x53.00_y113.00"></a>.
24. H. Bernien, B. Hensen, W. Pfaff, G. Koolstra, M. S. Blok,

L. Robledo, T. H. Taminiau, M. Markham, D. J. Twitchen,

L. Childress, and R. Hanson, Heralded entanglement between solid-state qubits separated by three metres, <a name="_page5_x53.00_y168.00"></a>[Nature (London) 497, 86 (2013)](https://doi.org/10.1038/nature12016).

26. Z.-L. Xiang, M. Zhang, L. Jiang, and P. Rabl, Intracity Quantum Communication via Thermal Microwave Net- works, [Phys. Rev. X 7, 011035 (2017)](https://doi.org/10.1103/PhysRevX.7.011035).
26. B. Vermersch, P.-O. Guimond, H. Pichler, and P. Zoller, Quantum State Transfer via Noisy Photonic and Phononic <a name="_page5_x53.00_y234.00"></a>Waveguides, [Phys. Rev. Lett. 118, 133601 (2017)](https://doi.org/10.1103/PhysRevLett.118.133601).
26. P. Kurpiers, P. Magnard, T. Walter, B. Royer, M. Pechal,

    10. Heinsoo, Y. Salathe,· A. Akin, S. Storz, J.-C. Besse, S. Gasparinetti, A. Blais, and A. Wallraff, Deterministic quantum state transfer and remote entanglement using microwave photons, [Nature (London) 558, 264 (2018)](https://doi.org/10.1038/s41586-018-0195-y).
26. P. Campagne-Ibarcq, E. Zalys-Geller, A. Narla, S. Shankar,

    10. Reinhold, L. Burkhart, C. Axline, W. Pfaff, L. Frunzio, R.J. Schoelkopf, and M.H. Devoret, Deterministic Remote Entanglement of Superconducting Circuits Through Micro- wave Two-Photon Transitions,[Phys. Rev. Lett.120, 200501 (2018)](https://doi.org/10.1103/PhysRevLett.120.200501).
26. C. Axline, L. Burkhart, W. Pfaff, M. Zhang, K. Chou, P. Campagne-Ibarcq, P. Reinhold, L. Frunzio, S.M. Girvin, L. Jiang, M.H. Devoret, and R.J. Schoelkopf, On-demand quantum state transfer and entanglement between remote <a name="_page5_x53.00_y410.00"></a>microwave cavity memories, [Nat. Phys. 14, 705 (2018)](https://doi.org/10.1038/s41567-018-0115-y).
26. Y.P. Zhong, H.-S. Chang, K.J. Satzinger, M.-H. Chou, A. Bienfait, C.R. Conner, . Dumur, J. Grebel, G.A. Peairs,<a name="_page5_x315.00_y432.00"></a>R.G. Povey, D.I. Schuster, and A.N. Cleland, Violating Bell s inequality with remotely connected superconducting qubits, [Nat. Phys. 15, 741 (2019)](https://doi.org/10.1038/s41567-019-0507-7).
26. N. Leung, Y. Lu, S. Chakram, R.K. Naik, N. Earnest, R.<a name="_page5_x315.00_y476.00"></a>Ma, K. Jacobs, A.N. Cleland, and D.I. Schuster, Deter- ministic bidirectional communication and remote entangle- ment generation between superconducting qubits, [npjQuantum Inf. 5, 18 (2019)](https://doi.org/10.1038/s41534-019-0128-0)<a name="_page5_x315.00_y509.00"></a><a name="_page5_x53.00_y520.00"></a>.
26. H.-S. Chang, Y.P. Zhong, A. Bienfait, M.-H. Chou, C.R. Conner, E. Dumur, J. Grebel, G.A. Peairs, R.G. Povey, K.J. Satzinger, and A.N. Cleland, Remote Entanglement via Adiabatic Passage Using a Tunably Dissipative Quan-<a name="_page5_x315.00_y564.00"></a>tum Communication System,[Phys. Rev. Lett. 124, 240502 (2020)](https://doi.org/10.1103/PhysRevLett.124.240502).
26. L.D. Burkhart, J. Teoh, Y. Zhang, C.J. Axline, L. Frunzio, M.H. Devoret, L. Jiang, S.M. Girvin, and R.J. Schoelkopf, Error-detected state transfer and entanglement in a super- <a name="_page5_x53.00_y630.00"></a>conducting quantum network, [arXiv:2004.06168](https://arXiv.org/abs/2004.06168).
26. J.I. Cirac, P. Zoller, H.J. Kimble, and H. Mabuchi, Quantum State Transfer and Entanglement Distribution Among Distant Nodes in a Quantum Network, [Phys. Rev. Lett. 78, 3221 (1997)](https://doi.org/10.1103/PhysRevLett.78.3221)<a name="_page5_x53.00_y674.00"></a>.
26. See Supplemental Material, which includes Refs. [37  43], at [http://link.aps.org/supplemental/10.1103/PhysRevLett .125.260502](http://link.aps.org/supplemental/10.1103/PhysRevLett.125.260502) for details about the characterization of

waveguide loss, for details about the sample fabrication and parameters, for a complete wiring diagram of the setup, for details about the calibration of pulses and their relative timings, for details about qutrit single-shot readout, for a photograph of the full cryogenic system, for details about the characterization of some properties of the transfer via measurement of photon envelopes, and for details about the tomographic reconstruction methods.

37. P. Kurpiers, T. Walter, P. Magnard, Y. Salathe, and A. Wallraff, Characterizing the attenuation of coaxial and rectangular microwave-frequency waveguides at cryo- genic temperatures, [Eur. Phys. J. Quantum Technol. 4, 8 (2017)](https://doi.org/10.1140/epjqt/s40507-017-0059-7).
37. D.M. Pozar, Microwave Engineering, 4th ed. (Wiley & Sons, Inc., New Jersey, USA, 2012).
37. T. Walter, P. Kurpiers, S. Gasparinetti, P. Magnard, A. Potočnik, Y. Salathe,· M. Pechal, M. Mondal, M. Oppliger,

    100. Eichler, and A. Wallraff, Rapid, High-Delity, Single-Shot Dispersive Readout of Superconducting Qubits,[Phys. Rev. Applied 7, 054020 (2017)](https://doi.org/10.1103/PhysRevApplied.7.054020).
37. K. Geerlings, Z. Leghtas, I.M. Pop, S. Shankar, L. Frunzio, R.J. Schoelkopf, M. Mirrahimi, and M.H. Devoret, Dem- onstrating a Driven Reset Protocol for a Superconducting Qubit, [Phys. Rev. Lett. 110, 120501 (2013)](https://doi.org/10.1103/PhysRevLett.110.120501).
37. K. Serniak, M. Hays, G. de Lange, S. Diamond, S. Shankar, L.D. Burkhart, L. Frunzio, M. Houzet, and M.H. Devoret, Hot Nonequilibrium Quasiparticles in Transmon Qubits, [Phys. Rev. Lett. 121, 157701 (2018)](https://doi.org/10.1103/PhysRevLett.121.157701).
37. F. Motzoi, J.M. Gambetta, P. Rebentrost, and F.K. Wilhelm, Simple Pulses for Elimination of Leakage in Weakly Nonlinear Qubits, [Phys. Rev. Lett. 103, 110501 (2009)](https://doi.org/10.1103/PhysRevLett.103.110501).
37. I.L. Chuang and M.A. Nielsen, Prescription for experi- mental determination of the dynamics of a quantum black box, [J. Mod. Opt. 44, 2455 (1997)](https://doi.org/10.1080/09500349708231894).
37. Y. Tamura, H. Sakuma, K. Morita, M. Suzuki, Y. Yamamoto, K.Shimada,Y.Honma,K.Sohma,T.Fujii,andT.Hasegawa, The first 0.14-db/km loss optical fiber and its impact on submarine transmission, [J. Light. Technol. 36, 44 (2018)](https://doi.org/10.1109/JLT.2018.2796647).
37. V. Parma, Cryostat Design, CAS  CERN Accelerator School: Course on Superconductivity for Accelerators, [https://doi.org/10.5170/CERN-2014-005.353 (2014).](https://doi.org/10.5170/CERN-2014-005.353)
37. P. Magnard, P. Kurpiers, B. Royer, T. Walter, J.-C. Besse, S. Gasparinetti, M. Pechal, J. Heinsoo, S. Storz, A. Blais, and A.Wallraff,FastandUnconditional All-MicrowaveResetof a Superconducting Qubit, [Phys. Rev. Lett. 121, 060502 (2018)](https://doi.org/10.1103/PhysRevLett.121.060502).
37. S. Zeytinoğlu, M. Pechal, S. Berger, A.A. Abdumalikov Jr.,
    1. Wallraff, and S. Filipp, Microwave-induced amplitude- and phase-tunable qubit-resonator coupling in circuit quan- tum electrodynamics, [Phys. Rev. A 91, 043846 (2015)](https://doi.org/10.1103/PhysRevA.91.043846).
37. M. Pechal, L. Huthmacher, C. Eichler, S. Zeytinoğlu, A.A. Abdumalikov Jr., S. Berger, A. Wallraff, and S. Filipp, Microwave-Controlled Generation of Shaped Single Pho- tons in Circuit Quantum Electrodynamics,[Phys. Rev. X 4, 041010 (2014)](https://doi.org/10.1103/PhysRevX.4.041010).
37. O. Morin, M. K rber, S. Langenfeld, and G. Rempe, Deterministic Shaping and Reshaping of Single-Photon Temporal Wave Functions, [Phys. Rev. Lett. 123, 133602 (2019)](https://doi.org/10.1103/PhysRevLett.123.133602).

260502-6
PHYSICAL REVIEW LETTERS 125, 260502 (2020)![](Aspose.Words.65b636c8-456e-42e2-a2e7-32b9905b209a.009.png)

50. S.J.<a name="_page6_x53.00_y47.00"></a> van Enk, N. L tkenhaus, and H.J. Kimble, Exper- imental procedures for entanglement verication,[Phys. Rev. A 75, 052318 (2007)](https://doi.org/10.1103/PhysRevA.75.052318)<a name="_page6_x53.00_y80.00"></a>.
50. A.G. Fowler, D.S. Wang, C.D. Hill, T.D. Ladd, R. Van Meter, and L.C.L. Hollenberg, Surface Code Quantum Communication, [Phys. Rev. Lett. 104, 180503 (2010)](https://doi.org/10.1103/PhysRevLett.104.180503).
50. P. Kurpiers, M. Pechal, B. Royer, P. Magnard, T. Walter, J. Heinsoo, Y. Salathe,· A. Akin, S. Storz, J.-C. Besse, S. Gasparinetti, A. Blais, and A. Wallraff, Quantum Commu- nication with Time-Bin Encoded Microwave Photons,[Phys. Rev. Applied 12, 044067 (2019)](https://doi.org/10.1103/PhysRevApplied.12.044067).
50. <a name="_page6_x315.00_y168.00"></a>K. Bergmann et al., Roadmap on STIRAP applications, [J. Phys. B 52, 202001 (2019)](https://doi.org/10.1088/1361-6455/ab3995)<a name="_page6_x53.00_y190.00"></a>.
50. J.I. Cirac, A.K. Ekert, S.F. Huelga, and C. Macchiavello, Distributed quantum computation over noisy channels, <a name="_page6_x53.00_y223.00"></a>[Phys. Rev. A 59, 4249 (1999)](https://doi.org/10.1103/PhysRevA.59.4249).
50. B. Hensen, H. Bernien, A.E. Dreau, A. Reiserer, N. Kalb, M.S. Blok, J. Ruitenberg, R.F.L. Vermeulen, R.N.

Schouten, C. Abellan, W. Amaya, V. Pruneri, M.W. Mitchell, M. Markham, D.J. Twitchen, D. Elkouss, S. Wehner, T.H. Taminiau, and R. Hanson, Loophole- free Bell inequality violation using electron spins separated by 1.3 kilometres, [Nature (London) 526, 682 (2015)](https://doi.org/10.1038/nature15759).

56. P. Bierhorst, E. Knill, S. Glancy, Y. Zhang, A. Mink, S. Jordan, A. Rommal, Y.-K. Liu, B. Christensen, S.W. Nam, M.J. Stevens, and L.K. Shalm, Experimentally generated randomness certified by the impossibility of superluminal signals, [Nature (London) 556, 223 (2018)](https://doi.org/10.1038/s41586-018-0019-0).
56. F. Dinc and A.M. Branczyk, Non-markovian super-super- radiance in a linear chain of up to 100 qubits, [Phys. Rev. Research 1, 032042 (2019)](https://doi.org/10.1103/PhysRevResearch.1.032042).
56. G. Calaj , Y.-L.L. Fang, H.U. Baranger, and F. Ciccarello, Exciting a bound state in the continuum through multi- photon scattering plus delayed quantum feedback, [Phys. Rev. Lett. 122, 073601 (2019)](https://doi.org/10.1103/PhysRevLett.122.073601).
260502-7
