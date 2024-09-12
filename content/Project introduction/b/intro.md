# Example document without heading comments

The work is shipped by Chuncheng Zhang.

---

[toc]

## FastAPI

The web service is maintained by the FastAPI Package.

### JinJa2 templates

It inline links the html template with each others.

### Tailwindcss

The web style is controlled by the tailwindcss, see the documents for details.

- <https://tailwindcss.com/docs/installation>
- <https://tailwindui.com/documentation>

## MNE package

The backend computing is operated by MNE package.

### Data formats

The data formats are supported:
  
- The .bdf files

  It supposes the .bdf file are in pair.

  - data.bdf, is the data file.
  - evt.bdf, in the same folder, is the event file.

  ```python
  # Read and link them in mne package
  raw = mne.io.read_raw('data.bdf')
  annotations = mne.read_annotations('evt.bdf')
  raw.set_annotations(annotations)
  ```

  The .bdf format document:

  - <https://mne.tools/stable/auto_tutorials/io/20_reading_eeg_data.html>
  - <https://www.biosemi.com/faq/file_format.htm>

  BioSemi data format (.bdf)

  The BDF format is a 24-bit variant of the EDF format used by EEG systems manufactured by BioSemi. It can be imported with mne.io.read_raw_bdf().
  BioSemi amplifiers do not perform “common mode noise rejection” automatically. The signals in the EEG file are the voltages between each electrode and the CMS active electrode, which still contain some CM noise (50 Hz, ADC reference noise, etc.). The BioSemi FAQ provides more details on this topic. Therefore, it is advisable to choose a reference (e.g., a single channel like Cz, average of linked mastoids, average of all electrodes, etc.) after importing BioSemi data to avoid losing signal information. The data can be re-referenced later after cleaning if desired.

### Operations

The operations are implemented:

1. Visualization of Data and Device layout
2. Preprocessing
3. Pattern analysis

### Classic BCI protocol

- Motion Imaginary (MI)
- Steady-State Visual Evoked Potential (SSVEP)
- Rapid Serial Visual Presentation (RSVP)
