{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Plagiarism Text Data\n",
    "\n",
    "In this project, you will be tasked with building a plagiarism detector that examines a text file and performs binary classification; labeling that file as either plagiarized or not, depending on how similar the text file is when compared to a provided source text. \n",
    "\n",
    "The first step in working with any dataset is loading the data in and noting what information is included in the dataset. This is an important step in eventually working with this data, and knowing what kinds of features you have to work with as you transform and group the data!\n",
    "\n",
    "So, this notebook is all about exploring the data and noting patterns about the features you are given and the distribution of data. \n",
    "\n",
    "> There are not any exercises or questions in this notebook, it is only meant for exploration. This notebook will note be required in your final project submission.\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Read in the Data\n",
    "\n",
    "The cell below will download the necessary data and extract the files into the folder `data/`.\n",
    "\n",
    "This data is a slightly modified version of a dataset created by Paul Clough (Information Studies) and Mark Stevenson (Computer Science), at the University of Sheffield. You can read all about the data collection and corpus, at [their university webpage](https://ir.shef.ac.uk/cloughie/resources/plagiarism_corpus.html). \n",
    "\n",
    "> **Citation for data**: Clough, P. and Stevenson, M. Developing A Corpus of Plagiarised Short Answers, Language Resources and Evaluation: Special Issue on Plagiarism and Authorship Analysis, In Press. [Download]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--2019-07-08 23:48:31--  https://s3.amazonaws.com/video.udacity-data.com/topher/2019/January/5c4147f9_data/data.zip\n",
      "Resolving s3.amazonaws.com (s3.amazonaws.com)... 52.216.176.85\n",
      "Connecting to s3.amazonaws.com (s3.amazonaws.com)|52.216.176.85|:443... connected.\n",
      "HTTP request sent, awaiting response... 200 OK\n",
      "Length: 113826 (111K) [application/zip]\n",
      "Saving to: ‘data.zip’\n",
      "\n",
      "data.zip            100%[===================>] 111.16K  --.-KB/s    in 0.02s   \n",
      "\n",
      "2019-07-08 23:48:31 (4.83 MB/s) - ‘data.zip’ saved [113826/113826]\n",
      "\n",
      "Archive:  data.zip\n",
      "   creating: data/\n",
      "  inflating: data/.DS_Store          \n",
      "   creating: __MACOSX/\n",
      "   creating: __MACOSX/data/\n",
      "  inflating: __MACOSX/data/._.DS_Store  \n",
      "  inflating: data/file_information.csv  \n",
      "  inflating: __MACOSX/data/._file_information.csv  \n",
      "  inflating: data/g0pA_taska.txt     \n",
      "  inflating: __MACOSX/data/._g0pA_taska.txt  \n",
      "  inflating: data/g0pA_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g0pA_taskb.txt  \n",
      "  inflating: data/g0pA_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g0pA_taskc.txt  \n",
      "  inflating: data/g0pA_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g0pA_taskd.txt  \n",
      "  inflating: data/g0pA_taske.txt     \n",
      "  inflating: __MACOSX/data/._g0pA_taske.txt  \n",
      "  inflating: data/g0pB_taska.txt     \n",
      "  inflating: __MACOSX/data/._g0pB_taska.txt  \n",
      "  inflating: data/g0pB_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g0pB_taskb.txt  \n",
      "  inflating: data/g0pB_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g0pB_taskc.txt  \n",
      "  inflating: data/g0pB_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g0pB_taskd.txt  \n",
      "  inflating: data/g0pB_taske.txt     \n",
      "  inflating: __MACOSX/data/._g0pB_taske.txt  \n",
      "  inflating: data/g0pC_taska.txt     \n",
      "  inflating: __MACOSX/data/._g0pC_taska.txt  \n",
      "  inflating: data/g0pC_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g0pC_taskb.txt  \n",
      "  inflating: data/g0pC_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g0pC_taskc.txt  \n",
      "  inflating: data/g0pC_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g0pC_taskd.txt  \n",
      "  inflating: data/g0pC_taske.txt     \n",
      "  inflating: __MACOSX/data/._g0pC_taske.txt  \n",
      "  inflating: data/g0pD_taska.txt     \n",
      "  inflating: __MACOSX/data/._g0pD_taska.txt  \n",
      "  inflating: data/g0pD_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g0pD_taskb.txt  \n",
      "  inflating: data/g0pD_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g0pD_taskc.txt  \n",
      "  inflating: data/g0pD_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g0pD_taskd.txt  \n",
      "  inflating: data/g0pD_taske.txt     \n",
      "  inflating: __MACOSX/data/._g0pD_taske.txt  \n",
      "  inflating: data/g0pE_taska.txt     \n",
      "  inflating: __MACOSX/data/._g0pE_taska.txt  \n",
      "  inflating: data/g0pE_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g0pE_taskb.txt  \n",
      "  inflating: data/g0pE_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g0pE_taskc.txt  \n",
      "  inflating: data/g0pE_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g0pE_taskd.txt  \n",
      "  inflating: data/g0pE_taske.txt     \n",
      "  inflating: __MACOSX/data/._g0pE_taske.txt  \n",
      "  inflating: data/g1pA_taska.txt     \n",
      "  inflating: __MACOSX/data/._g1pA_taska.txt  \n",
      "  inflating: data/g1pA_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g1pA_taskb.txt  \n",
      "  inflating: data/g1pA_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g1pA_taskc.txt  \n",
      "  inflating: data/g1pA_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g1pA_taskd.txt  \n",
      "  inflating: data/g1pA_taske.txt     \n",
      "  inflating: __MACOSX/data/._g1pA_taske.txt  \n",
      "  inflating: data/g1pB_taska.txt     \n",
      "  inflating: __MACOSX/data/._g1pB_taska.txt  \n",
      "  inflating: data/g1pB_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g1pB_taskb.txt  \n",
      "  inflating: data/g1pB_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g1pB_taskc.txt  \n",
      "  inflating: data/g1pB_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g1pB_taskd.txt  \n",
      "  inflating: data/g1pB_taske.txt     \n",
      "  inflating: __MACOSX/data/._g1pB_taske.txt  \n",
      "  inflating: data/g1pD_taska.txt     \n",
      "  inflating: __MACOSX/data/._g1pD_taska.txt  \n",
      "  inflating: data/g1pD_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g1pD_taskb.txt  \n",
      "  inflating: data/g1pD_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g1pD_taskc.txt  \n",
      "  inflating: data/g1pD_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g1pD_taskd.txt  \n",
      "  inflating: data/g1pD_taske.txt     \n",
      "  inflating: __MACOSX/data/._g1pD_taske.txt  \n",
      "  inflating: data/g2pA_taska.txt     \n",
      "  inflating: __MACOSX/data/._g2pA_taska.txt  \n",
      "  inflating: data/g2pA_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g2pA_taskb.txt  \n",
      "  inflating: data/g2pA_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g2pA_taskc.txt  \n",
      "  inflating: data/g2pA_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g2pA_taskd.txt  \n",
      "  inflating: data/g2pA_taske.txt     \n",
      "  inflating: __MACOSX/data/._g2pA_taske.txt  \n",
      "  inflating: data/g2pB_taska.txt     \n",
      "  inflating: __MACOSX/data/._g2pB_taska.txt  \n",
      "  inflating: data/g2pB_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g2pB_taskb.txt  \n",
      "  inflating: data/g2pB_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g2pB_taskc.txt  \n",
      "  inflating: data/g2pB_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g2pB_taskd.txt  \n",
      "  inflating: data/g2pB_taske.txt     \n",
      "  inflating: __MACOSX/data/._g2pB_taske.txt  \n",
      "  inflating: data/g2pC_taska.txt     \n",
      "  inflating: __MACOSX/data/._g2pC_taska.txt  \n",
      "  inflating: data/g2pC_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g2pC_taskb.txt  \n",
      "  inflating: data/g2pC_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g2pC_taskc.txt  \n",
      "  inflating: data/g2pC_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g2pC_taskd.txt  \n",
      "  inflating: data/g2pC_taske.txt     \n",
      "  inflating: __MACOSX/data/._g2pC_taske.txt  \n",
      "  inflating: data/g2pE_taska.txt     \n",
      "  inflating: __MACOSX/data/._g2pE_taska.txt  \n",
      "  inflating: data/g2pE_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g2pE_taskb.txt  \n",
      "  inflating: data/g2pE_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g2pE_taskc.txt  \n",
      "  inflating: data/g2pE_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g2pE_taskd.txt  \n",
      "  inflating: data/g2pE_taske.txt     \n",
      "  inflating: __MACOSX/data/._g2pE_taske.txt  \n",
      "  inflating: data/g3pA_taska.txt     \n",
      "  inflating: __MACOSX/data/._g3pA_taska.txt  \n",
      "  inflating: data/g3pA_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g3pA_taskb.txt  \n",
      "  inflating: data/g3pA_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g3pA_taskc.txt  \n",
      "  inflating: data/g3pA_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g3pA_taskd.txt  \n",
      "  inflating: data/g3pA_taske.txt     \n",
      "  inflating: __MACOSX/data/._g3pA_taske.txt  \n",
      "  inflating: data/g3pB_taska.txt     \n",
      "  inflating: __MACOSX/data/._g3pB_taska.txt  \n",
      "  inflating: data/g3pB_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g3pB_taskb.txt  \n",
      "  inflating: data/g3pB_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g3pB_taskc.txt  \n",
      "  inflating: data/g3pB_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g3pB_taskd.txt  \n",
      "  inflating: data/g3pB_taske.txt     \n",
      "  inflating: __MACOSX/data/._g3pB_taske.txt  \n",
      "  inflating: data/g3pC_taska.txt     \n",
      "  inflating: __MACOSX/data/._g3pC_taska.txt  \n",
      "  inflating: data/g3pC_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g3pC_taskb.txt  \n",
      "  inflating: data/g3pC_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g3pC_taskc.txt  \n",
      "  inflating: data/g3pC_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g3pC_taskd.txt  \n",
      "  inflating: data/g3pC_taske.txt     \n",
      "  inflating: __MACOSX/data/._g3pC_taske.txt  \n",
      "  inflating: data/g4pB_taska.txt     \n",
      "  inflating: __MACOSX/data/._g4pB_taska.txt  \n",
      "  inflating: data/g4pB_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g4pB_taskb.txt  \n",
      "  inflating: data/g4pB_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g4pB_taskc.txt  \n",
      "  inflating: data/g4pB_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g4pB_taskd.txt  \n",
      "  inflating: data/g4pB_taske.txt     \n",
      "  inflating: __MACOSX/data/._g4pB_taske.txt  \n",
      "  inflating: data/g4pC_taska.txt     \n",
      "  inflating: __MACOSX/data/._g4pC_taska.txt  \n",
      "  inflating: data/g4pC_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g4pC_taskb.txt  \n",
      "  inflating: data/g4pC_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g4pC_taskc.txt  \n",
      "  inflating: data/g4pC_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g4pC_taskd.txt  \n",
      "  inflating: data/g4pC_taske.txt     \n",
      "  inflating: __MACOSX/data/._g4pC_taske.txt  \n",
      "  inflating: data/g4pD_taska.txt     \n",
      "  inflating: __MACOSX/data/._g4pD_taska.txt  \n",
      "  inflating: data/g4pD_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g4pD_taskb.txt  \n",
      "  inflating: data/g4pD_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g4pD_taskc.txt  \n",
      "  inflating: data/g4pD_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g4pD_taskd.txt  \n",
      "  inflating: data/g4pD_taske.txt     \n",
      "  inflating: __MACOSX/data/._g4pD_taske.txt  \n",
      "  inflating: data/g4pE_taska.txt     \n",
      "  inflating: __MACOSX/data/._g4pE_taska.txt  \n",
      "  inflating: data/g4pE_taskb.txt     \n",
      "  inflating: __MACOSX/data/._g4pE_taskb.txt  \n",
      "  inflating: data/g4pE_taskc.txt     \n",
      "  inflating: __MACOSX/data/._g4pE_taskc.txt  \n",
      "  inflating: data/g4pE_taskd.txt     \n",
      "  inflating: __MACOSX/data/._g4pE_taskd.txt  \n",
      "  inflating: data/g4pE_taske.txt     \n",
      "  inflating: __MACOSX/data/._g4pE_taske.txt  \n",
      "  inflating: data/orig_taska.txt     \n",
      "  inflating: __MACOSX/data/._orig_taska.txt  \n",
      "  inflating: data/orig_taskb.txt     \n",
      "  inflating: data/orig_taskc.txt     \n",
      "  inflating: __MACOSX/data/._orig_taskc.txt  \n",
      "  inflating: data/orig_taskd.txt     \n",
      "  inflating: __MACOSX/data/._orig_taskd.txt  \n",
      "  inflating: data/orig_taske.txt     \n",
      "  inflating: __MACOSX/data/._orig_taske.txt  \n",
      "  inflating: data/test_info.csv      \n",
      "  inflating: __MACOSX/data/._test_info.csv  \n",
      "  inflating: __MACOSX/._data         \n"
     ]
    }
   ],
   "source": [
    "!wget https://s3.amazonaws.com/video.udacity-data.com/topher/2019/January/5c4147f9_data/data.zip\n",
    "!unzip data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# import libraries\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This plagiarism dataset is made of multiple text files; each of these files has characteristics that are is summarized in a `.csv` file named `file_information.csv`, which we can read in using `pandas`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>File</th>\n",
       "      <th>Task</th>\n",
       "      <th>Category</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>g0pA_taska.txt</td>\n",
       "      <td>a</td>\n",
       "      <td>non</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>g0pA_taskb.txt</td>\n",
       "      <td>b</td>\n",
       "      <td>cut</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>g0pA_taskc.txt</td>\n",
       "      <td>c</td>\n",
       "      <td>light</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>g0pA_taskd.txt</td>\n",
       "      <td>d</td>\n",
       "      <td>heavy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>g0pA_taske.txt</td>\n",
       "      <td>e</td>\n",
       "      <td>non</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>g0pB_taska.txt</td>\n",
       "      <td>a</td>\n",
       "      <td>non</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>g0pB_taskb.txt</td>\n",
       "      <td>b</td>\n",
       "      <td>non</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>g0pB_taskc.txt</td>\n",
       "      <td>c</td>\n",
       "      <td>cut</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>g0pB_taskd.txt</td>\n",
       "      <td>d</td>\n",
       "      <td>light</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>g0pB_taske.txt</td>\n",
       "      <td>e</td>\n",
       "      <td>heavy</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             File Task Category\n",
       "0  g0pA_taska.txt    a      non\n",
       "1  g0pA_taskb.txt    b      cut\n",
       "2  g0pA_taskc.txt    c    light\n",
       "3  g0pA_taskd.txt    d    heavy\n",
       "4  g0pA_taske.txt    e      non\n",
       "5  g0pB_taska.txt    a      non\n",
       "6  g0pB_taskb.txt    b      non\n",
       "7  g0pB_taskc.txt    c      cut\n",
       "8  g0pB_taskd.txt    d    light\n",
       "9  g0pB_taske.txt    e    heavy"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csv_file = 'data/file_information.csv'\n",
    "plagiarism_df = pd.read_csv(csv_file)\n",
    "\n",
    "# print out the first few rows of data info\n",
    "plagiarism_df.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Types of Plagiarism\n",
    "\n",
    "Each text file is associated with one **Task** (task A-E) and one **Category** of plagiarism, which you can see in the above DataFrame.\n",
    "\n",
    "###  Five task types, A-E\n",
    "\n",
    "Each text file contains an answer to one short question; these questions are labeled as tasks A-E.\n",
    "* Each task, A-E, is about a topic that might be included in the Computer Science curriculum that was created by the authors of this dataset. \n",
    "    * For example, Task A asks the question: \"What is inheritance in object oriented programming?\"\n",
    "\n",
    "### Four categories of plagiarism \n",
    "\n",
    "Each text file has an associated plagiarism label/category:\n",
    "\n",
    "1. `cut`: An answer is plagiarized; it is copy-pasted directly from the relevant Wikipedia source text.\n",
    "2. `light`: An answer is plagiarized; it is based on the Wikipedia source text and includes some copying and paraphrasing.\n",
    "3. `heavy`: An answer is plagiarized; it is based on the Wikipedia source text but expressed using different words and structure. Since this doesn't copy directly from a source text, this will likely be the most challenging kind of plagiarism to detect.\n",
    "4. `non`: An answer is not plagiarized; the Wikipedia source text is not used to create this answer.\n",
    "5. `orig`: This is a specific category for the original, Wikipedia source text. We will use these files only for comparison purposes.\n",
    "\n",
    "> So, out of the submitted files, the only category that does not contain any plagiarism is `non`.\n",
    "\n",
    "In the next cell, print out some statistics about the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of files:  100\n",
      "Number of unique tasks/question types (A-E):  5\n",
      "Unique plagiarism categories:  ['non' 'cut' 'light' 'heavy' 'orig']\n"
     ]
    }
   ],
   "source": [
    "# print out some stats about the data\n",
    "print('Number of files: ', plagiarism_df.shape[0])  # .shape[0] gives the rows \n",
    "# .unique() gives unique items in a specified column\n",
    "print('Number of unique tasks/question types (A-E): ', (len(plagiarism_df['Task'].unique())))\n",
    "print('Unique plagiarism categories: ', (plagiarism_df['Category'].unique()))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You should see the number of text files in the dataset as well as some characteristics about the `Task` and `Category` columns. **Note that the file count of 100 *includes* the 5 _original_ wikipedia files for tasks A-E.** If you take a look at the files in the `data` directory, you'll notice that the original, source texts start with the filename `orig_` as opposed to `g` for \"group.\" \n",
    "\n",
    "> So, in total there are 100 files, 95 of which are answers (submitted by people) and 5 of which are the original, Wikipedia source texts.\n",
    "\n",
    "Your end goal will be to use this information to classify any given answer text into one of two categories, plagiarized or not-plagiarized."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Distribution of Data\n",
    "\n",
    "Next, let's look at the distribution of data. In this course, we've talked about traits like class imbalance that can inform how you develop an algorithm. So, here, we'll ask: **How evenly is our data distributed among different tasks and plagiarism levels?**\n",
    "\n",
    "Below, you should notice two things:\n",
    "* Our dataset is quite small, especially with respect to examples of varying plagiarism levels.\n",
    "* The data is distributed fairly evenly across task and plagiarism types."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Task:\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Task</th>\n",
       "      <th>Counts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>b</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>c</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>d</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>e</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Task  Counts\n",
       "0    a      20\n",
       "1    b      20\n",
       "2    c      20\n",
       "3    d      20\n",
       "4    e      20"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Plagiarism Levels:\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Category</th>\n",
       "      <th>Counts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>cut</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>heavy</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>light</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>non</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>orig</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Category  Counts\n",
       "0      cut      19\n",
       "1    heavy      19\n",
       "2    light      19\n",
       "3      non      38\n",
       "4     orig       5"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Task & Plagiarism Level Combos :\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Task</th>\n",
       "      <th>Category</th>\n",
       "      <th>Counts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>cut</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>a</td>\n",
       "      <td>heavy</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>a</td>\n",
       "      <td>light</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>a</td>\n",
       "      <td>non</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>a</td>\n",
       "      <td>orig</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>b</td>\n",
       "      <td>cut</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>b</td>\n",
       "      <td>heavy</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>b</td>\n",
       "      <td>light</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>b</td>\n",
       "      <td>non</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>b</td>\n",
       "      <td>orig</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>c</td>\n",
       "      <td>cut</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>c</td>\n",
       "      <td>heavy</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>c</td>\n",
       "      <td>light</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>c</td>\n",
       "      <td>non</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>c</td>\n",
       "      <td>orig</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>d</td>\n",
       "      <td>cut</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>d</td>\n",
       "      <td>heavy</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>d</td>\n",
       "      <td>light</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>d</td>\n",
       "      <td>non</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>d</td>\n",
       "      <td>orig</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>e</td>\n",
       "      <td>cut</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>e</td>\n",
       "      <td>heavy</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>e</td>\n",
       "      <td>light</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>e</td>\n",
       "      <td>non</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>e</td>\n",
       "      <td>orig</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Task Category  Counts\n",
       "0     a      cut       4\n",
       "1     a    heavy       3\n",
       "2     a    light       3\n",
       "3     a      non       9\n",
       "4     a     orig       1\n",
       "5     b      cut       3\n",
       "6     b    heavy       4\n",
       "7     b    light       3\n",
       "8     b      non       9\n",
       "9     b     orig       1\n",
       "10    c      cut       3\n",
       "11    c    heavy       5\n",
       "12    c    light       4\n",
       "13    c      non       7\n",
       "14    c     orig       1\n",
       "15    d      cut       4\n",
       "16    d    heavy       4\n",
       "17    d    light       5\n",
       "18    d      non       6\n",
       "19    d     orig       1\n",
       "20    e      cut       5\n",
       "21    e    heavy       3\n",
       "22    e    light       4\n",
       "23    e      non       7\n",
       "24    e     orig       1"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Show counts by different tasks and amounts of plagiarism\n",
    "\n",
    "# group and count by task\n",
    "counts_per_task=plagiarism_df.groupby(['Task']).size().reset_index(name=\"Counts\")\n",
    "print(\"\\nTask:\")\n",
    "display(counts_per_task)\n",
    "\n",
    "# group by plagiarism level\n",
    "counts_per_category=plagiarism_df.groupby(['Category']).size().reset_index(name=\"Counts\")\n",
    "print(\"\\nPlagiarism Levels:\")\n",
    "display(counts_per_category)\n",
    "\n",
    "# group by task AND plagiarism level\n",
    "counts_task_and_plagiarism=plagiarism_df.groupby(['Task', 'Category']).size().reset_index(name=\"Counts\")\n",
    "print(\"\\nTask & Plagiarism Level Combos :\")\n",
    "display(counts_task_and_plagiarism)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It may also be helpful to look at this last DataFrame, graphically.\n",
    "\n",
    "Below, you can see that the counts follow a pattern broken down by task. Each task has one source text (original) and the highest number on `non` plagiarized cases."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<BarContainer object of 25 artists>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "% matplotlib inline\n",
    "\n",
    "# counts\n",
    "group = ['Task', 'Category']\n",
    "counts = plagiarism_df.groupby(group).size().reset_index(name=\"Counts\")\n",
    "\n",
    "plt.figure(figsize=(8,5))\n",
    "plt.bar(range(len(counts)), counts['Counts'], color = 'blue')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Up Next\n",
    "\n",
    "This notebook is just about data loading and exploration, and you do not need to include it in your final project submission. \n",
    "\n",
    "In the next few notebooks, you'll use this data to train a complete plagiarism classifier. You'll be tasked with extracting meaningful features from the text data, reading in answers to different tasks and comparing them to the original Wikipedia source text. You'll engineer similarity features that will help identify cases of plagiarism. Then, you'll use these features to train and deploy a classification model in a SageMaker notebook instance. "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "conda_amazonei_mxnet_p36",
   "language": "python",
   "name": "conda_amazonei_mxnet_p36"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
