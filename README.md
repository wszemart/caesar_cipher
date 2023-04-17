## Caesar_cipher
#### Simple app to encode and decode text by using Ceasar cipher. Created with Python.
### Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More detail about functionality](#more-detail-about-functionality)

### [General info](#general-info)
<details>
<summary>Click here to see general information about <b>Project</b>!</summary>

The application was created for a practice purposes. In the project was used the project patterns: Facade, FactoryMethod and AbstractFactory. The app functionality was tested by the pytest library. Style and compatibility with PEP8 rules was checked and corrected by the PEP8 Black library. The usage of the application was designed from the Menu level. The console-menu package was used to create the Menu.
</details>

### [Technologies](#technologies)
<details>
<summary>Click here to see general information about <b>Technologies</b>!</summary>

Project is created with:
<ul>
<li>Python</li>
<li>pytest</li>
<li>unitest</li>
</ul>
</details>

### [Setup](#setup)
<details>
<summary>Click here to see general information about <b>Setup</b>!</summary>
<ul>

To run this app:
<li>Clone the repository</li>

```git clone https://github.com/wszemart/caesar_cipher```
<li>Install <i>console-menu</i> and <i>pytest</i> packages</li> 
<li>In the terminal go to directory with repository and run this command 

``` python main.py ```</li>
</ul>
</details>

### [More detail about functionality](#more-detail-about-functionality)
<details>
<summary>Click here to see general information about <b>Functionality</b>!</summary>

The application has the Menu and the Submenu. From the Menu level are supported such functionalities as:
<ul>
<li>choosing type of the action to execute (encrypt/decrypt)</li>
<li>loading data from a file</li>
<li>going to the Submenu (Memory Buffer Menu)</li>
<li>exiting the application</li>
</ul>
While the program is running, the inserted and loaded data are stored in the list (Memory Buffer functionality). What allows after going to the Submenu to:
<ul>
<li>displaying the stored data (Show Buffer)</li>
<li>memory cleaning (CLear Buffer)</li>
<li>removing singular items from the memory (Delete position from Memory Buffer)</li>
<li>saving data as a file in json form (Save Buffer to file)</li>
<li>going back to the main Menu</li>
</ul>
</details>
