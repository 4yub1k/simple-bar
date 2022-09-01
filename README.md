# Simple-Bar
Loading bar, Progress bar, all in one highly customizable per your need.<pip install simple-bar>

![image](https://user-images.githubusercontent.com/45902447/187984455-28f1ffe6-9036-4bc6-b638-6ccf9e585b4e.png)
  

It is super easy to implement in your code, just call it with you loop and the rest will be taken care, you can change the color, symbols, loading time, size, 
and more.

![](https://img.shields.io/badge/Python-3.10-green)

### Installation:
```
pip install simple-bar
```
You are ready to go .
```python
  from simplebar.bar import loading
```
### Help: 
 > Note: Set LOADING_TIME = 0, in order to load according to the tasks.
```python
  loading(LOADING_BAR_RANGE=50, LOADING_MAX_VAL=100, LOADING_TIME=0.1, LOOP_RANGE=10, 
          fg_text_color="green", bg_text_color="black", text_style="bold",
          fg_value_color="white", bg_value_color="black", value_style="normal",
          symbol_load='#', symbol_bg='.')
```
```
  LOADING_BAR_RANGE                   # Change length of Loading bar.
  LOADING_MAX_VAL                     # Values upto which you want loading bar.
  LOADING_TIME                        # Stepwise wait time for loading bar (seconds).
  LOOP_RANGE                          # Loop size where you want to use loading e-g for i in range(20), LOOP_RANGE=20.
  loop_value                          # iteration value e-g i, for i in range(20).

  fg_text_color                       # Symbols text color in the bar.
  bg_text_color                       # Symbols background color in the bar.
  text_style                          # Style of symbol BOLD,NORMAL.

  fg_value_color                      # Value text color at end of bar.
  bg_value_color                      # Value background color at end of bar.
  value_style                         # Style of value at end of bar BOLD,NORMAL.

  symbol_load                         # Symbol to use in loading bar.
  symbol_bg                           # Background symbol to use in loading bar.
```

### Examples:
 ```python
  LOOP_SIZE = 20
  print("Task 1:")
  for i in range(LOOP_SIZE):
      # some task
      loading(50, 50, 0.1, LOOP_SIZE, i+1,
              fg_text_color="green", bg_text_color="black", text_style="bold",
              fg_value_color="white", bg_value_color="black", value_style="bold",
              symbol_load='#', symbol_bg='.')
 ```
 ![image](https://user-images.githubusercontent.com/45902447/187982840-35b19982-9083-4af0-8145-59c52de9b449.png)

  ```python
  LOOP_SIZE = 20
  print("\nTask 2:")
  for i in range(LOOP_SIZE):
      # some task
      loading(50, 100, 0.1, LOOP_SIZE, i+1,
              fg_text_color="red", bg_text_color="black", text_style="bold",
              fg_value_color="yellow", bg_value_color="black", value_style="bold",
              symbol_load='*', symbol_bg='-')
  ```
  ![image](https://user-images.githubusercontent.com/45902447/187983080-b45faf05-ed4f-4b1e-882e-aece6f7d9911.png)

  ```python
  LOOP_SIZE = 20
  print("\nTask 3:")
  for i in range(LOOP_SIZE):
      # some task
      loading(50, 10, 0.1, LOOP_SIZE, i+1,
              fg_text_color="cyan", bg_text_color="black", text_style="bold",
              fg_value_color="magenta", bg_value_color="black", value_style="bold",
              symbol_load='>', symbol_bg='-')
  ```
  ![image](https://user-images.githubusercontent.com/45902447/187983191-3eaa6031-677a-4775-acc5-fe0332556d6a.png)

  ```python
  
  LOOP_SIZE = 20
  print("\nTask 4:")
  for i in range(LOOP_SIZE):
      # some task
      loading(100, 200, 0.1, LOOP_SIZE, i+1,
              fg_text_color="red", bg_text_color="green", text_style="bold",
              fg_value_color="red", bg_value_color="black", value_style="bold",
              symbol_load='x', symbol_bg='=')
```
  ![image](https://user-images.githubusercontent.com/45902447/187983278-625bf206-ae2a-4781-ab99-efda816ecf54.png)

  ```python
  LOOP_SIZE = 20
  print("\nTask 5:")
  for i in range(LOOP_SIZE):
      # some task
      loading(100, 100, 0.1, LOOP_SIZE, i+1,
              fg_text_color="red", bg_text_color="black", text_style="bold",
              fg_value_color="red", bg_value_color="black", value_style="bold",
              symbol_load=':', symbol_bg='-')
  ```
  ![image](https://user-images.githubusercontent.com/45902447/187983535-f59a50c6-32c2-4d3d-967e-8e8ebf83aefe.png)

 ```python
  LOOP_SIZE = 20
  print("\nTask 6:")
  for i in range(LOOP_SIZE):
      # some task
      loading(50, 200, 0.1, LOOP_SIZE, i+1,
              fg_text_color="blue", bg_text_color="black", text_style="bold",
              fg_value_color="green", bg_value_color="black", value_style="bold",
              symbol_load='@', symbol_bg='_')
  ```
 ![image](https://user-images.githubusercontent.com/45902447/187983639-80f7bdfc-7511-4438-8f72-fa0e93ebf0e7.png)

 ```python
  LOOP_SIZE = 40
  print("\nTask 7:")
  for i in range(LOOP_SIZE):
      # some task
      loading(40, 500, 0.1, LOOP_SIZE, i+1,
              fg_text_color="white", bg_text_color="black", text_style="bold",
              fg_value_color="blue", bg_value_color="black", value_style="bold",
              symbol_load='%', symbol_bg='-')
  ```
  ![image](https://user-images.githubusercontent.com/45902447/187983745-d042d65c-4942-4ebb-90a7-4d312d93e7f4.png)

 ```python 
  LOOP_SIZE = 40
print("\nTask 8:")
for i in range(LOOP_SIZE):
    # some task
    loading(40, 1000, 0.1, LOOP_SIZE, i+1,
            fg_text_color="yellow", bg_text_color="black", text_style="bold",
            fg_value_color="red", bg_value_color="yellow", value_style="bold",
            symbol_load='+', symbol_bg='.')
  ```
![image](https://user-images.githubusercontent.com/45902447/187982526-b82b52fd-9f9a-4577-8b7f-72c90404a1f6.png)

**I'll keep it updating, time to time**, *Thank you !* 😉
