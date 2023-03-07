# python GUI for Analog clock

<h1 align="center">

<img  src="https://user-images.githubusercontent.com/99537126/223482084-013fab11-d1e4-4e77-9cd7-e8c46952c3b3.png" alt="coding display" style="width:650px; height:500px"/>

<img  src="https://user-images.githubusercontent.com/99537126/223483977-71253239-e987-4840-9038-678adcaa371e.png" alt="coding display" style="width:650px; height:500px"/>
</h1>

This is a Python script that creates a simple desktop application using `PyQt5` library to display an analog clock that runs on a local webpage.

The script creates a main window, sets its size and title, and adds a QWebEngineView widget to display the webpage. The webpage is loaded from a local HTML file that contains the clock design and JavaScript code to update the clock hands' positions. The webpage's CSS style is also defined in the HTML file.

The clock hands' position is updated using the `setInterval()` method in JavaScript. The function gets the current time, calculates the rotation angle for each hand, and sets the transform CSS property for each hand element.

The CSS style for the clock and its hands is defined in a separate file called style.css, which is linked to the HTML file using the `<link>` tag.

Finally, the script sets the application icon using the `setWindowIcon()` method.

To run this script, you need to have `PyQt5` and `PyQt5.QtWebEngineWidgets` libraries installed on your system.

