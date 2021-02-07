# widgets
>Custom Qt widgets and scripts for my desktop

If it turns out good, I'll add setup tools and make
it an installable package.

Without a custom layout to fix the spacing in clockwidget.

![Widget example](/images/run_widgets.png)

With spacing hack
```
t = "<span style=\"color:#93ebd5;\">{0}</span><span style=\"color:#00afd7;\">:</span><span style=\"color:#d5f6ff;\">{1}</span>".format(hourDisplay, minuteDisplay)
```
This solution is ugly but effective...
I wanted to color each digit of the clock + separator ":".
This is the only way I've found so far to achieve normal spacing at font size 70
without reimplementing sizeHint() and things like that.

![Widget hack example](/images/run_widgets_spacing_hack.png)
