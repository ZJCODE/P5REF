import streamlit as st
import streamlit.components.v1 as components

# https://cdnjs.com/libraries/p5.js

def get_html_content(script, width_ratio=1):
    # 将宽度比例转换为缩放比例
    scale_ratio = width_ratio  # 假设width_ratio即为我们想要的缩放比例
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.4/p5.min.js"></script>
        <meta charset="utf-8" />
        <style>
        body {{
            transform: scale({scale_ratio});  /* 应用缩放 */
            transform-origin: top left;  /* 保证缩放时内容仍然居中 */
        }}
        </style>
    </head>
    <body>
        <script>
        {script}
        </script>
    </body>
    </html>
    """

def draw_script(script,width=None):
    if 'createCanvas' not in script or 'function setup()' not in script:
        return components.html("请检查代码是否为P5.js代码")
    try:
        width_in_code = int(script.replace(" ","").split("createCanvas(")[1].split(",")[0])
        height_in_code = int(script.replace(" ","").split("createCanvas(")[1].split(",")[1].split(");")[0])
    except Exception as e:
        width_in_code = 400
        height_in_code = 400
        print(e)
    
    if width is None:
        width = width_in_code
        height = height_in_code
        html = get_html_content(script=script)
    else:
        width_ratio = width/width_in_code
        height = int(height_in_code * width_ratio)
        html = get_html_content(script=script, width_ratio=width_ratio)

    return components.html(html, width=width, height=height)
        
def build_script(basic,setup,draw):
    return basic + "\nfunction setup() {" + setup +"} \nfunction draw() {" + draw +"}"
