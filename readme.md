# Muse data acquisition tool

This tool connects to the muse device and uses the api to dump EEG data of the subjects who go through different experiments.

### Fill the form and hit start.  <br /><img src="https://i.imgur.com/6E804eo.jpg" width="300">

### It'll dump the all the data including EEG values in the desired folder. <br /><img src="http://i.imgur.com/iz1x6dm.jpg" width="600">   

### The information of each subject is saved in an xml file.

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
