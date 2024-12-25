# EpiLynx: Automated Epitope-Linker Construction Software

## Introduction
In traditional vaccine development workflows, researchers manually link epitopes using a trial-and-error approach and rely on external software to fetch the instability index of the constructed sequences. This process is not only time-consuming but also prone to inefficiencies, especially when dealing with multiple epitopes.

**EpiLynx** is the first software to fully automate the epitope-linker construction process, providing researchers with a streamlined, efficient, and accurate tool for vaccine design.
![Screenshot (142)](https://github.com/user-attachments/assets/44ec2a51-7574-4600-b940-ab28a21a5ad3)
---


## Features
- **Automated Linking:** Eliminates the need for manual trial-and-error linking of epitopes.
- **Two Innovative Approaches for Construction:**
  1. **GRP-Based Real-Time Linking:** Uses real-time instability index calculations for sequential linking of epitopes and linkers.
  2. **AI-Based Combination with Pruning Techniques:** Efficiently evaluates and prunes potential combinations to construct the optimal sequence.
- **Integrated Instability Index Calculation:** Instability indices are computed in real-time directly within the software, saving researchers from switching between tools.
- **Web-Based Deployment:** Accessible from any device with an internet connection at [EpiLynx](https://epilynx.sbhmprksh.in).
  ![Screenshot (140)](https://github.com/user-attachments/assets/741f88d7-cc36-4bf7-9dee-a79de8d67050)

---

### Problem Statement
Before EpiLynx, researchers had to:
1. Manually link epitopes and add linkers based on intuition or trial and error.
2. Fetch the instability index of sequences from various external tools.
3. Repeat this process iteratively to identify an optimal sequence.

This process could take days to weeks, especially when analyzing multiple potential combinations.

## How It Works
1. Upload an initial CSV file (`default_file.csv`) containing epitope sequences and linker options.
2. The software processes the input to:
   - Link epitopes automatically.
   - Calculate instability indices in real-time.
   - Provide optimal results using AI-enhanced algorithms.
3. Download the final results for further analysis.



### EpiLynx Solution
EpiLynx introduces a fully automated solution:
1. **GRP-Based Real-Time Linking:**
   ![Screenshot (141)](https://github.com/user-attachments/assets/6bccd83f-c15c-42d6-9a04-4c7c842dea57)
   - Implements a novel algorithm inspired by the GRP matrix to calculate the real-time instability index of each sequence as it is constructed.
   - Allows users to generate stable and optimal sequences in a step-by-step manner.
3. **AI-Based Combination with Pruning Techniques:**
   ![Screenshot (143)](https://github.com/user-attachments/assets/edbc13e5-432f-472f-b255-ebfc55fe5412)
   - Recursively evaluates all possible epitope-linker combinations.
   - Prunes non-optimal branches early, ensuring efficiency and scalability for larger datasets.

### Key Component: `logic.py`
The core functionality of EpiLynx resides in the `logic.py` module. This file contains the complete implementation of:
- Real-time instability index calculations.
- GRP-based algorithms.
- AI-based pruning and sequence construction techniques.

---


## Deployment
EpiLynx is deployed and accessible via the following link:
[https://epilynx.sbhmprksh.in](https://epilynx.sbhmprksh.in)

### Installation (For Local Use)
To run EpiLynx locally:
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd EpiLynx
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python manage.py runserver
   ```
4. Access the application in your browser at `http://127.0.0.1:8000/`.

---

## Future Work
- Expanding support for additional linker databases.
- Integrating predictive models for toxicity and immunogenicity.
- Adding a feature for population coverage analysis.

---

## Contributing
Contributions to improve EpiLynx are welcome! Please submit pull requests or open issues for bug reports and feature suggestions.

---

## Acknowledgments
Special thanks to the researchers and collaborators who provided valuable feedback during development.

---

EpiLynx simplifies vaccine design by automating the once-manual epitope-linker process, saving researchers valuable time and resources. Start your efficient vaccine development journey today!
