
import streamlit as st
from draw import draw_script

def references():
    tab_basic,tab_draw,tab_axis,\
    tab_color,\
    tab_text,tab_interaction,\
    tab_animation,tab_function,\
    tab_particle,tab_program,\
    tab_3d,tab_other = st.tabs(["基础简介",
                                "形状绘制",
                                "坐标系统",
                                "颜色样式",
                                "文本使用",
                                "交互操作",
                                "动画效果",
                                "变量函数",
                                "编程专项",
                                "粒子系统",
                                "3D绘图",
                                "其他"])

    with tab_basic:
        c1,c2,c3 = st.columns([3,2,2])
        with c1:
            st.markdown("#### 基础简介")
            st.write("""P5.js是一个基于Processing的JavaScript库，用于创建交互式图形和动画。

P5.js的设计目标是让艺术家、设计师、教育工作者和初学者能够轻松地创建图形。
""")
        with c2:
            # template 
            st.markdown("#### 代码模板")
            code = """            
            // 一些基础参数
            let x = 0; // 可以定义一些变量
            
            // 初始化函数
            function setup() {
                // 创建画布
                createCanvas(400, 400);
            }
            
            // 绘制函数
            function draw() {
                // 设置背景色
                background(220);
                // 绘制一个圆位于(200,200)坐标，半径为100
                circle(200,200,100);
            }
            """
            st.code(code,language="javascript")
        with c3:
            st.markdown("#### 画布展示")
            draw_script(code)
            # st.image("assets/Demo.png",use_column_width=True)
    with tab_draw:
        # title, info, code
        tab_draw_codes = [
        ("直线",
         "函数 line(x1, y1, x2, y2) 用于绘制一条直线，x1,y1为起点坐标，x2,y2为终点坐标",
         """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    line(50,50,300,300); 
}"""),
        ("矩形",
         "函数 rect(x, y, w, h) 用于绘制一个矩形，x,y为矩形左上角坐标，w,h为矩形宽高",
         """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    rect(50,50,200,260); 
}"""),
    ("椭圆",
     "函数 ellipse(x, y, w, h) 用于绘制一个椭圆，x,y为椭圆中心坐标，w,h为椭圆宽高",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    ellipse(200,200,200,100);
}"""),   
    ("圆",
     "函数 circle(x, y, d) 用于绘制一个圆，x,y为圆心坐标，d为直径",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    circle(200,200,100);
}"""),
    ("正方形",
     "函数 square(x, y, s) 用于绘制一个正方形，x,y为正方形左上角坐标，s为边长",
     """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    square(50,50,200);
}"""),
    ("三角形",
     "函数 triangle(x1, y1, x2, y2, x3, y3) 用于绘制一个三角形，x1,y1,x2,y2,x3,y3为三角形三个顶点坐标",
     """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    triangle(100,100,100,300,300,300);
}"""), 
    ("弧形",
        "函数 arc(x, y, w, h, start, stop) 用于绘制一个弧形，x,y为圆心坐标，w,h为圆宽高，start,stop为起始角度和结束角度 默认单位为弧度, 方向为顺时针",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    arc(200,200,200,200,0,PI);
}"""),
    ("贝塞尔曲线",
     "函数 bezier(x1, y1, cx1, cy1, cx2, cy2, x2, y2) 用于绘制一个贝塞尔曲线，x1,y1为起点坐标，cx1,cy1为第一个控制点坐标，cx2,cy2为第二个控制点坐标，x2,y2为终点坐标",
     """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    bezier(100,100,100,200,200,100,300,300);
}"""),
    ("点",
     "函数 point(x, y) 用于绘制一个点，x,y为点的坐标",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    strokeWeight(10); // 设置点的大小
    point(200,200);
}"""),
    ("多边形",
        "函数 beginShape() 和 endShape() 用于绘制多边形 通过 vertex() 函数添加顶点",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    beginShape();
    vertex(200, 50);
    vertex(300, 150);
    vertex(275, 275);
    vertex(125, 275);
    vertex(100, 150);
    endShape(CLOSE);
}"""),
        ]
        c1,c2,c3,c4 = st.columns(4)
        with c1:
            for i in range(0, len(tab_draw_codes),4):
                st.write(f"##### 绘制{tab_draw_codes[i][0]}")
                st.info(tab_draw_codes[i][1])
                st.code(tab_draw_codes[i][2],language="javascript")
                draw_script(tab_draw_codes[i][2],120)
        with c2:
            for i in range(1, len(tab_draw_codes),4):
                st.write(f"##### 绘制{tab_draw_codes[i][0]}")
                st.info(tab_draw_codes[i][1])
                st.code(tab_draw_codes[i][2],language="javascript")
                draw_script(tab_draw_codes[i][2],120)
        with c3:
            for i in range(2, len(tab_draw_codes),4):
                st.write(f"##### 绘制{tab_draw_codes[i][0]}")
                st.info(tab_draw_codes[i][1])
                st.code(tab_draw_codes[i][2],language="javascript")
                draw_script(tab_draw_codes[i][2],120)
        with c4:
            for i in range(3, len(tab_draw_codes),4):
                st.write(f"##### 绘制{tab_draw_codes[i][0]}")
                st.info(tab_draw_codes[i][1])
                st.code(tab_draw_codes[i][2],language="javascript")
                draw_script(tab_draw_codes[i][2],120)
    with tab_axis:
        # title, info, code
        tab_axis_codes = [
        ("坐标系",
         "P5.js中的坐标系原点在画布的左上角，x轴向右，y轴向下",
         """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    rect(200,100,100,150);
}"""),
        ("坐标平移",
         "函数 translate(x, y) 用于坐标平移，x,y为平移距离 默认以画布左上角为原点 ,常用于将坐标中心移动到画面中心 translate(width/2,height/2)",
         """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    translate(50,50);
    rect(200,100,100,150);
}"""),
    ("坐标旋转",
     "函数 rotate(angle) 用于坐标旋转,angle为旋转角度 默认绕坐标原点(0,0)即画布左上角旋转",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    rotate(PI/6);
    rect(200,100,100,150);
}"""),
    ("坐标缩放",
     "函数 scale(s) 用于坐标缩放,s为缩放比例 默认以画布左上角为原点",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    scale(0.5);
    rect(200,100,100,150);
}"""),
    ("坐标缩放两个方向",
        "函数 scale(s1,s2) 用于坐标缩放,s1,s2为x,y方向缩放比例 默认以画布左上角为原点",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    scale(1,0.5);
    rect(200,100,100,150);
}"""),
    ("坐标中心模式",
        "函数 rectMode(CENTER) 用于设置矩形绘制模式为中心模式,同理还有ellipseMode(CENTER)",
            """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    rectMode(CENTER);
    rect(200,100,100,150);
}"""),
    ("临时坐标系",
        "函数 push() 和 pop() 用于创建临时坐标系，push()用于创建开始，pop()用于结束",
            """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    push();
    rotate(PI/6);
    rect(200,100,100,150);
    pop();
    rect(200,100,100,150);
}"""),
    ("坐标系复位",
     "函数 resetMatrix() 用于复位坐标系 恢复到初始状态",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    rotate(PI/6);
    rect(200,100,100,150);
    resetMatrix();
    rect(200,100,100,150);
}"""),
     ]
        c1,c2,c3,c4 = st.columns(4)
        with c1:
            for i in range(0, len(tab_axis_codes),4):
                st.write(f"##### {tab_axis_codes[i][0]}")
                st.info(tab_axis_codes[i][1])
                st.code(tab_axis_codes[i][2],language="javascript")
                if i == 0:
                    code = tab_axis_codes[i][2].strip()[:-1] + """// 绘制原点
                                                                strokeWeight(30);
                                                                point(0,0);
                                                                strokeWeight(1);
                                                                textSize(30);
                                                                text("(0,0)",20,50);
                                                                
                                                                // 绘制 (200,100)
                                                                strokeWeight(30);
                                                                point(200,100);
                                                                strokeWeight(1);
                                                                textSize(30);
                                                                text("(200,100)",210,80);
                                                                
                                                                // 绘制横纵坐标网格
                                                                stroke(100);
                                                                strokeWeight(2);
                                                                for (let i = 0; i < width; i += 100) {
                                                                    line(i, 0, i, height);
                                                                }
                                                                for (let i = 0; i < height; i += 100) {
                                                                    line(0, i, width, i);
                                                                }
                                                            }"""
                    draw_script(code,120)
                else:
                    draw_script(tab_axis_codes[i][2],120)
        with c2:
            for i in range(1, len(tab_axis_codes),4):
                st.write(f"##### {tab_axis_codes[i][0]}")
                st.info(tab_axis_codes[i][1])
                st.code(tab_axis_codes[i][2],language="javascript")
                draw_script(tab_axis_codes[i][2],120)
        with c3:
            for i in range(2, len(tab_axis_codes),4):
                st.write(f"##### {tab_axis_codes[i][0]}")
                st.info(tab_axis_codes[i][1])
                st.code(tab_axis_codes[i][2],language="javascript")
                draw_script(tab_axis_codes[i][2],120)
        with c4:
            for i in range(3, len(tab_axis_codes),4):
                st.write(f"##### {tab_axis_codes[i][0]}")
                st.info(tab_axis_codes[i][1])
                st.code(tab_axis_codes[i][2],language="javascript")
                draw_script(tab_axis_codes[i][2],120)
        
        
    with tab_color:
        # title, info, code
        tab_color_codes = [   
        ("填充颜色",
         "函数 fill 用于设置填充颜色，可用于图形、文本、背景色,常用参数可以是RGB值、RGBA、灰度值、16进制值 例如 fill(125,224,142)、fill(125,224,142,100)、fill(150)、fill('#7DE08E')",
         """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    fill(125,224,142);
    circle(100,120,100);
    fill(125,224,142,100);
    circle(300,120,100);
    fill(150);
    circle(100,280,100);
    fill('#7DE08E');
    circle(300,280,100);
}"""),
    ("无填充",
        "函数 noFill 用于取消填充",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    noFill();
    circle(200,200,100);
}"""),
    ("背景颜色",
         "函数 background 用于设置背景颜色，常用参数和fill相同 例如 background(125,224,142)、background(150)、background('#7DE08E')等",
         """function setup() {createCanvas(400, 400);}
function draw() {
    background(125,224,142);
    circle(200,200,100);
}"""),
    ("描边颜色",
     "函数 stroke 用于设置描边颜色，常用参数和fill相同 例如 stroke(255,0,0)、stroke(150)、stroke('#7DE08E')等",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    stroke(255,0,0);
    circle(100,120,100);
    stroke(150);
    circle(300,120,100);
    stroke('#7DE08E');
    circle(200,280,100);
}"""),
("渐变色",
        "函数 lerpColor(c1, c2, amt) 用于设置渐变色，c1,c2为颜色，amt为渐变比例",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    let c1 = color(125,224,142);
    let c2 = color(200,150,120);
    for(let i=0;i<height;i++){
        let c = lerpColor(c1,c2,i/height);
        stroke(c);
        line(0,i,400,i);
    }
}"""),   
("描边宽度",
     "函数 strokeWeight(w) 用于设置描边宽度",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    strokeWeight(5);
    circle(200,200,100);
}"""),
    ("描边端点类型",
        "函数 strokeCap 用于设置描边端点类型，常用参数有ROUND、SQUARE、PROJECT",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    strokeWeight(30);
    strokeCap(ROUND);
    line(100,100,300,100);
    strokeCap(SQUARE);
    line(100,200,300,200);
    strokeCap(PROJECT);
    line(100,300,300,300);
}"""),
    ("描边连接类型",
        "函数 strokeJoin 用于设置描边连接类型，常用参数有ROUND、BEVEL、MITER",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    noFill();
    strokeWeight(50);
    strokeJoin(ROUND);
    beginShape();
    vertex(100,70);
    vertex(200,90);
    vertex(300,70);
    endShape();
    strokeJoin(BEVEL);
    beginShape();
    vertex(100,170);
    vertex(200,190);
    vertex(300,170);
    endShape();
    strokeJoin(MITER);
    beginShape();
    vertex(100,270);
    vertex(200,290);
    vertex(300,270);
    endShape();
}"""),
    ("取消描边",
        "函数 noStroke 用于取消描边",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    noStroke();
    circle(200,200,100);
}"""),
]
        c1,c2,c3,c4 = st.columns(4)
        with c1:
            for i in range(0, len(tab_color_codes),4):
                st.write(f"##### {tab_color_codes[i][0]}")
                st.info(tab_color_codes[i][1])
                st.code(tab_color_codes[i][2],language="javascript")
                draw_script(tab_color_codes[i][2],120)
        with c2:
            for i in range(1, len(tab_color_codes),4):
                st.write(f"##### {tab_color_codes[i][0]}")
                st.info(tab_color_codes[i][1])
                st.code(tab_color_codes[i][2],language="javascript")
                draw_script(tab_color_codes[i][2],120)
        with c3:
            for i in range(2, len(tab_color_codes),4):
                st.write(f"##### {tab_color_codes[i][0]}")
                st.info(tab_color_codes[i][1])
                st.code(tab_color_codes[i][2],language="javascript")
                draw_script(tab_color_codes[i][2],120)
        with c4:
            for i in range(3, len(tab_color_codes),4):
                st.write(f"##### {tab_color_codes[i][0]}")
                st.info(tab_color_codes[i][1])
                st.code(tab_color_codes[i][2],language="javascript")
                draw_script(tab_color_codes[i][2],120)

    with tab_text:
        # title, info, code
        tab_text_codes = [
        ("文本内容",
         "函数 text(txt, x, y) 用于绘制文本，txt为文本内容，x,y为文本坐标",
         """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    textSize(60);
    text("Hello P5",50,200);
}"""),
        ("文本大小",
         "函数 textSize(size) 用于设置文本大小",
         """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    textSize(80);
    text("Hello P5",50,200);
}"""),
    ("文本样式",
     "函数 textStyle(style) 用于设置文本样式，style: NORMAL,ITALIC,BOLD",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    textSize(60);
    textStyle(NORMAL);
    text("Hello P5",50,100);
    textStyle(ITALIC);
    text("Hello P5",50,200);
    textStyle(BOLD);
    text("Hello P5",50,300);
}"""),
    ("文本对齐",
     "函数 textAlign(hor, ver) 用于设置文本对齐方式，hor: LEFT, CENTER, RIGHT ver: TOP, CENTER, BOTTOM ,默认位置为左下角",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    textSize(60);
    textAlign(CENTER,CENTER);
    text("Hello P5",200,200);
}"""),
    ("文本字体",
     "函数 textFont(font) 用于设置文本字体",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    textSize(50);
    textFont("Courier New");
    text("Courier New",10,100);
    textFont("Arial");
    text("Arial",10,200);
    textFont("Verdana");
    text("Verdana",10,300);
}"""),
    ("文本宽度",
     "函数 textWidth(txt) 用于获取文本宽度",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    textSize(60);
    let w = textWidth("Hello P5");
    text("Hello P5",50,200);
    text(w,50,300);
}"""),
    ("文本颜色",
     "函数 fill 用于设置文本颜色",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    fill(0,50,255);
    textSize(60);
    text("Hello P5",50,200);
}"""),
    ("文本变形",
     "使用 push() 和 pop() 函数创建临时坐标系，用于文本变形",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    push();
    scale(1,0.6);
    textSize(60);
    text("Hello P5",10,200);
    pop();
    push();
    scale(1.2,1);
    textSize(60);
    text("Hello P5",10,300);
    pop();
}"""),
        ]

        c1,c2,c3,c4 = st.columns(4)
        with c1:
            for i in range(0, len(tab_text_codes),4):
                st.write(f"##### {tab_text_codes[i][0]}")
                st.info(tab_text_codes[i][1])
                st.code(tab_text_codes[i][2],language="javascript")
                draw_script(tab_text_codes[i][2],120)
        with c2:
            for i in range(1, len(tab_text_codes),4):
                st.write(f"##### {tab_text_codes[i][0]}")
                st.info(tab_text_codes[i][1])
                st.code(tab_text_codes[i][2],language="javascript")
                draw_script(tab_text_codes[i][2],120)
        with c3:
            for i in range(2, len(tab_text_codes),4):
                st.write(f"##### {tab_text_codes[i][0]}")
                st.info(tab_text_codes[i][1])
                st.code(tab_text_codes[i][2],language="javascript")
                draw_script(tab_text_codes[i][2],120)
        with c4:
            for i in range(3, len(tab_text_codes),4):
                st.write(f"##### {tab_text_codes[i][0]}")
                st.info(tab_text_codes[i][1])
                st.code(tab_text_codes[i][2],language="javascript")
                draw_script(tab_text_codes[i][2],120)

    with tab_interaction:
        # title, info, code
        tab_interaction_codes = [
        ("获取鼠标位置",
         "函数 mouseX mouseY 用于获取鼠标位置",
         """function setup() {createCanvas(120, 120);}
function draw() {
    background(220);
    textSize(10);
    text("("+mouseX+","+mouseY+")",mouseX,mouseY);
}"""),
        ("获取鼠标按键状态",
         "函数 mouseIsPressed 用于获取鼠标按键状态",
         """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    textSize(40);
    text("点击鼠标: "+mouseIsPressed,50,200);
}"""),
    ("获取键盘按键状态",
     "函数 keyIsPressed 用于获取键盘按键状态",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    textSize(40);
    text("点击键盘: "+keyIsPressed,50,200);
}"""),
    ("获取键盘按键值",
     "函数 key 用于获取键盘按键",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    textSize(40);
    text("按键: "+key,50,200);
}"""),
    ("触发键盘事件",
     "函数 keyPressed() 用于键盘按下事件",
        """let drawCircle = false;
function setup() {createCanvas(400, 400);}
function draw() {
  background(220);
  if (drawCircle) {
    ellipse(200, 200, 100, 100);
  }
}
function keyPressed() {
  if (key === 'a') {
    drawCircle = true;
  }
}"""),
    ("鼠标拖拽",
        "函数 mouseDragged() 用于鼠标拖拽事件",
        """let x = 60;
let y = 60;
function setup() {createCanvas(120, 120);}
function draw() {
    background(220);
    ellipse(x, y, 20, 20);
}
function mouseDragged() {
    x = mouseX;
    y = mouseY;
}"""),
    ("鼠标按下与释放事件",
        "函数 mouseReleased() 用于鼠标释放事件",
        """let drawCircle = false;
function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    if (drawCircle) {
        ellipse(200, 200, 100, 100);
    }
}
function mousePressed() {
    drawCircle = true;
}
function mouseReleased() {
    drawCircle = false;
}"""),
    ("键盘按下与释放事件",
        "函数 keyReleased() 用于键盘释放事件",
        """let txt = "";
function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    textSize(80);
    text(txt,200,200);
}
function keyTyped() {
    txt += key;
}
function keyReleased() {
    txt = "";
}"""),
        
        ]

        c1,c2,c3,c4 = st.columns(4)
        with c1:
            for i in range(0, len(tab_interaction_codes),4):
                st.write(f"##### {tab_interaction_codes[i][0]}")
                st.info(tab_interaction_codes[i][1])
                st.code(tab_interaction_codes[i][2],language="javascript")
                draw_script(tab_interaction_codes[i][2],120)
        with c2:
            for i in range(1, len(tab_interaction_codes),4):
                st.write(f"##### {tab_interaction_codes[i][0]}")
                st.info(tab_interaction_codes[i][1])
                st.code(tab_interaction_codes[i][2],language="javascript")
                draw_script(tab_interaction_codes[i][2],120)
        with c3:
            for i in range(2, len(tab_interaction_codes),4):
                st.write(f"##### {tab_interaction_codes[i][0]}")
                st.info(tab_interaction_codes[i][1])
                st.code(tab_interaction_codes[i][2],language="javascript")
                draw_script(tab_interaction_codes[i][2],120)
        with c4:
            for i in range(3, len(tab_interaction_codes),4):
                st.write(f"##### {tab_interaction_codes[i][0]}")
                st.info(tab_interaction_codes[i][1])
                st.code(tab_interaction_codes[i][2],language="javascript")
                draw_script(tab_interaction_codes[i][2],120)

    with tab_animation:
        st.warning("编辑更新进行中...")
        # title, info, code
        tab_animation_codes = [
        ("动画效果",
         "默认情况下，draw()函数会不断重复执行，从而形成动画效果",
            """let x = 0;
function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    circle(x,200,100);
    x += 1;
}"""),
        ("帧率",
         "函数 frameRate(fps) 用于设置帧率，即每秒绘制的次数 默认为60",
            """let x = 0;
function setup() {createCanvas(400, 400);frameRate(10);}
function draw() {
    background(220);
    circle(x,200,100);
    x += 1;
}"""),
    ("帧数",
     "函数 frameCount 用于获取当前帧数 可用于动画控制",
        """function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    let x = frameCount % 200;
    circle(x,200,100);
}"""),
    ("动画暂停",
     "函数 noLoop() 用于暂停动画 loop() 用于恢复动画",
        """let x = 0;
function setup() {createCanvas(400, 400);}
function draw() {
    background(220);
    circle(x,200,100);
    x += 1;
}
function keyPressed() {
    if (key === 'p') {
        if (isLooping()) {
            noLoop();
        } else {
            loop();
        }
    }
}"""),
]
        c1,c2,c3,c4 = st.columns(4)
        with c1:
            for i in range(0, len(tab_animation_codes),4):
                st.write(f"##### {tab_animation_codes[i][0]}")
                st.info(tab_animation_codes[i][1])
                st.code(tab_animation_codes[i][2],language="javascript")
                draw_script(tab_animation_codes[i][2],120)
        with c2:
            for i in range(1, len(tab_animation_codes),4):
                st.write(f"##### {tab_animation_codes[i][0]}")
                st.info(tab_animation_codes[i][1])
                st.code(tab_animation_codes[i][2],language="javascript")
                draw_script(tab_animation_codes[i][2],120)
        with c3:
            for i in range(2, len(tab_animation_codes),4):
                st.write(f"##### {tab_animation_codes[i][0]}")
                st.info(tab_animation_codes[i][1])
                st.code(tab_animation_codes[i][2],language="javascript")
                draw_script(tab_animation_codes[i][2],120)
        with c4:
            for i in range(3, len(tab_animation_codes),4):
                st.write(f"##### {tab_animation_codes[i][0]}")
                st.info(tab_animation_codes[i][1])
                st.code(tab_animation_codes[i][2],language="javascript")
                draw_script(tab_animation_codes[i][2],120)