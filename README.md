# Generating Natural Timings for Violin Sheet Music

## Description

This project utilizes neural networks to predict expressive features in violin performances. These features are then synthesized into audio files. Overall, the goal of this project is to create natural sounding audio, given sheet music.

## Proposal Paper

For a comprehensive understanding of our project, please refer to our proposal paper [here](./documents/McAuley_Dong_ERSP_2023_Proposal.pdf). Additionally, you should refer to this paper to understand the representations of notes used in this project.

## Project Structure
```md
.
├── bach-violin-dataset/
│   └── this is ported from https://github.com/salu133445/bach-violin-dataset
├── documents/
│   └── McAuley_Dong_ERSP_2023_Proposal.pdf
├── src/
│   ├── data/
│   │   ├── parse_data.ipynb
│   │   ├── plot_data.ipynb
│   │   ├── print_data.ipynb
│   │   └── randomizer.ipynb
│   ├── dataset-paths/
│   │   ├── [training/validating/testing]-source-input.txt
│   │   └── [training/validating/testing]-ground-truth.txt
│   ├── models/
│   │   ├── linear-regression/
│   │   │   ├── data_processing.ipynb
│   │   │   ├── linear_regression_model.ipynb
│   │   │   └── synthesize_all_linear_regression_results.ipynb
│   │   ├── mlp/
│   │   │   ├── data_processing.ipynb
│   │   │   ├── mlp_model.ipynb
│   │   │   └── synthesize_all_mlp_results.ipynb
│   │   └── lstm/
│   │       ├── data_processing.ipynb
│   │       ├── lstm_model.ipynb
│   │       └── synthesize_all_lstm_results.ipynb
│   ├── synthesize/
│   │   ├── synthesize_all_ground_truths.ipynb
│   │   ├── synthesize_all_source_inputs.ipynb
│   │   └── synthesize_functions.ipynb
│   ├── global_variables.ipynb
│   └── plot_mse.ipynb
└── environment.yml
```
The most important parts of our project structure are in `src`. Our project mainly involved 5 stages:

1. **Extract the CSV values from `bach-violin-dataset`.** This was done in `parse_data.ipynb`, where it takes in the name of the CSV file containing the note values, then returns a list of tuple values which correspond to each note.
2. **Create the training/validation/testing datasets to train and test the models on.** This was done with `randomizer.ipynb`, which split the dataset into 70% training, 20% validation, and 10% testing. The file paths of these pieces were then recorded into `dataset-paths/`. Additionally, there is a file named `data_processing.ipynb` within each model folder. This is so that we can further manipulate the dataset to be in the “correct” format for training, which is specific to each model. We also used a PyTorch API to create minibatches for our dataset, specifically Dataset and DataLoader from `torch.utils.data`. 
3. **Train the model!** After all of our datasets have been created, our training code is run on all of the respective `[model_name]_model.ipynb` notebooks. For some of the models, like the MLP and LSTM model, there will also be corresponding `[model].pt` files, which store the state of the models after training. For this, we also used PyTorch APIs.
4. **Print the results and error values with the testing dataset.** This is done in `plot_mse.ipynb`, as well as `plot_data.ipynb` in `data`. The reason for this redundancy is because our boxplot was specific to our poster, so we created a new file for it. These plots were created by Matplotlib.
5. **Synthesize the audio from the generated results.** This is done within each `synthesize_all_[model]_results.ipynb`, which use the functions in `synthesize`. The tuples are converted into MIDI through PrettyMIDI, which is then converted into audio through FluidSynth.

Feel free to download our code and run it for yourself! To accomplish this, be sure to activate the environment in `environment.yml` so that you have all of the required packages. Here are some additional resources that may be useful for understanding our code:
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html): Contains lots of tutorials for building your own basic model, as well as documentation on all of the different layers we used, mini-batching APIs, and LSTM specific APIs, such as `PadPackedSequence`.
- [PrettyMIDI Documentation](https://craffel.github.io/pretty-midi/)
- [FluidSynth Documentation](https://www.fluidsynth.org/documentation/)
