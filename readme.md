# Muse data acquisition tool
A simple program that uses the developer api of MUSE headband to connect and to save the EEG data in `.mat` format. This was built to conduct studies on classifying different tasks based on EEG data.

### Getting Started
```shell
$ git clone https://github.com/paul-shuvo/muse-data-acquisition-tool.git
$ cd muse-data-acquisition-tool
$ pip install
$ python src/muse_data_acquisition_tool.py
```

This will launch the following GUI interface:
 <br /><img src="https://i.imgur.com/6E804eo.jpg" width="300">

The form elements can be changed in the `setupUi`
method.

Experiments can be added either by changing the `experiment_args` variable or using the `add_experiment` method in the `experiments.py` file.

Once started, the programm will go through the experiments and save EEG data as `.mat` files.
<br /><img src="http://i.imgur.com/iz1x6dm.jpg" width="600">   

__The information of each subject is saved in an xml file in the following format.__

```xml
<?xml version="1.0"?>
<cvcr>
    <subject ID="04">
        <date>12052015</date>
        <serial>04</serial>
        <name>Person A</name>
        <age>23</age>
        <gender>Female</gender>
    </subject>
    <subject ID="05">
        <date>12052015</date>
        <serial>05</serial>
        <name>Person B</name>
        <age>19</age>
        <gender>Male</gender>
    </subject>
</cvcr>
```
