"""The KE_info page."""

from practice.templates import template

import reflex as rx



@template(route="/ke/info", title="K-SADS-E Personal Info")
def ke_info() -> rx.Component:

    return rx.flex(
        rx.flex(rx.text("K-SADS-E Interview DSM-5 Version", size="7", weight="light"),
                rx.text("中文版DSM-5兒童青少年精神疾病流行病學診斷會談工具", size="5"),
                direction="column",
                align="center",
                width="100%",
        ),
        rx.flex(
            rx.flex(
                rx.text("受訪者編碼"),
                rx.input(type="text", width="175px"),
                justify="between", 
                width="100%",
                margin= "20px 0 0 0",
            ),
            # rx.flex(
            #     rx.text("受訪者日期"),
            #     rx.input(type="text")
            # ),
            rx.flex(
                rx.text("受訪者姓名"),
                rx.input(type="text", width="175px"),
                justify="between", 
                width="100%",
                margin= "20px 0 0 0",
            ),
            rx.flex(
                rx.text("生理性別"),
                rx.select(
                    ["男", "女"],
                    placeholder="生理性別",
                    radius="medium",
                    width="175px",
                    is_require="True"),
                justify="between", 
                width="100%",
                margin= "20px 0 0 0",
            ),        
            rx.flex(
                rx.text("出生日期"),
                rx.input(type="date", width="175px"),
                justify="between", 
                width="100%",
                margin= "20px 0 0 0",
            ),                
            rx.flex(
                rx.text("學校名稱／年級"),
                rx.input(type="text", width="175px"),
                rx.input(type="text", width="175px"),
                direction="column",
                margin= "20px 0 0 0",
            ),
            rx.flex(
                rx.text("教育程度"),
                rx.text("最高學歷"),
                rx.input(type="text", width="175px"),
                rx.text("教育年數"),
                rx.input(type="text", width="175px"),
                rx.text("職業"),
                rx.input(type="text"),
                direction="column",
                margin= "20px 0 0 0",
            ),
            rx.flex(
                rx.text("父親教育程度"),
                rx.text("最高學歷"),
                rx.input(type="text"),
                rx.text("教育年數"),
                rx.input(type="text"),
                rx.text("職業"),
                rx.input(type="text"),
                direction="column",
                margin= "20px 0 0 0",
            ),
            rx.flex(
                rx.text("母親教育程度"),
                rx.text("最高學歷"),
                rx.input(type="text"),
                rx.text("教育年數"),
                rx.input(type="text"),
                rx.text("職業"),
                rx.input(type="text"),
                direction="column",
                margin= "20px 0 0 0",
            ),
            direction="column",
            width = "500px",
            margin="20px"
        ),
        rx.link(rx.button("開始訪談"), href="/ke/menu"),
        width="100%",
        direction="column",
        align="center",
    )


@template(route="/ke/menu", title="K-SADS-E Menu")
def ke_menu() -> rx.Component:

    return rx.flex(
        rx.flex(
            rx.text("K-SADS-E Interview DSM-5 Version", size="7", weight="light"),
            rx.text("中文版DSM-5兒童青少年精神疾病流行病學診斷會談工具", size="5"),
            rx.flex(
                rx.link(rx.button("修改基本資料"), href="/ke/info"),
            ),     
            direction="column", 
            align="center",
            width="100%",
            margin="0 0 30px 0",
        ),
        rx.flex(
            rx.text("訪談目錄", size="5", weight="light"),
            width="100%",
            align="center",
            justify="center",
            margin="0 0 30px 0",
        ),
        # rx.flex(
        #     rx.flex(
        #         rx.text("障礙症"),
                
        #         rx.text("篩檢量表"),
              
        #         rx.text("完整量表"),
        #         width="100%",
        #         align="center",
        #         justify="between",
        #         padding="5px",
        #         height="32px",
        #     ),
        #     rx.flex(
        #         rx.text("社交溝通障礙／自閉症類群障礙症"),
               
        #         rx.link(rx.button("未完成"), href="/"),
        #         rx.link(rx.button("未完成"), href="/"),
        #         width="100%",
        #         align="center",
        #         justify="between",
        #         padding="5px",
        #         height="32px",
        #     ),
        #     rx.flex(
        #         rx.text("注意力不足／過動症"),
                
        #         rx.link(rx.button("未完成"), href="/"),
        #         rx.link(rx.button("未完成"), href="/"),
        #         width="100%",
        #         align="center",
        #         justify="between",
        #         padding="5px",
        #         height="32px",
        #     ),
        #     direction="column",
        #     width="100%",
        #     justify="between",
        #     align="center",
        # ),

        rx.flex(
            rx.grid(
                    # 社交溝通障礙／自閉症類群障礙症 Social Communication Disorder / Autism Spectrum Disorder
                    # 注意力不足／過動症 Attention Deficit / Hyperactivity Disorder
                    # 抽搐症 Tic Disorders
                    # 對立反抗症 Oppositional Defiant Disorder
                    # 間歇暴怒障礙症 Intermittent Explosive Disorder
                    # 行為規範障礙症 Conduct Disorder
                    # 憂鬱症 Depressive Disorders
                    # 侵擾性情緒失調症 Disruptive Mood Dysregulation Disorder
                    # 雙相情緒及其相關障礙症 Bipolar and Related Disorders
                    # 自殺行為疾患 Suicidal Behavior Disorder
                    # 自傷行為 Non-Suicidal Self-Injury
                    # 分離焦慮症 Separation Anxiety Disorder
                    # 特定畏懼症 Specific Phobia
                    # 特定場所畏懼症 Agoraphobia
                    # 社交畏懼症 Social Phobia
                    # 恐慌症 Panic Disorder
                    # 廣泛性焦慮症 Generalized Anxiety Disorder
                    # 強迫症 Obsessive-Compulsive Disorder
                    # 迴避/節制型攝食症 Avoidant/Restrictive Food Intake Disorder
                    # 厭食症 Anorexia Nervosa
                    # 暴食症 Bulimia Nervosa
                    # 性別不安 Gender Dysphoria
                    # 反應性依附障礙症 Reactive Attachment Disorder
                    # 創傷後壓力症 Posttraumatic Stress Disorder
                    # 解離性身分障礙症 Dissociative Identity Disorder
                    # 失自我感／失現實感障礙症 Depersonalization / Derealization Disorder
                    # 身體症狀障礙症 Somatic Symptom Disorder
                    # 睡醒障礙症 Sleep-Wake Disorders
                    # 精神病症 Psychotic Disorders
                    # 菸草相關障礙症 Tobacco-Related Disorders
                    # 酒精相關障礙症 Alcohol-Related Disorders
                    # 檳榔相關障礙症 Betel-Nut Related Disorders
                    # 藥物相關障礙症 Substance Use Disorders
            rx.text("障礙症"),  
            rx.text("篩檢量表"),
            rx.text("完整量表"),
            rx.text("社交溝通障礙／自閉症類群障礙症 Social Communication Disorder / Autism Spectrum Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("注意力不足／過動症 Attention Deficit / Hyperactivity Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("抽搐症 Tic Disorders"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("對立反抗症 Oppositional Defiant Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("間歇暴怒障礙症 Intermittent Explosive Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("行為規範障礙症 Conduct Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("憂鬱症 Depressive Disorders"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("侵擾性情緒失調症 Disruptive Mood Dysregulation Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("雙相情緒及其相關障礙症 Bipolar and Related Disorders"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("自殺行為疾患 Suicidal Behavior Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("自傷行為 Non-Suicidal Self-Injury"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("分離焦慮症 Separation Anxiety Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("特定畏懼症 Specific Phobia"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("特定場所畏懼症 Agoraphobia"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("社交畏懼症 Social Phobia"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("恐慌症 Panic Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("廣泛性焦慮症 Generalized Anxiety Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("強迫症 Obsessive-Compulsive Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("迴避/節制型攝食症 Avoidant/Restrictive Food Intake Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("厭食症 Anorexia Nervosa"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("暴食症 Bulimia Nervosa"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("性別不安 Gender Dysphoria"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("反應性依附障礙症 Reactive Attachment Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("創傷後壓力症 Posttraumatic Stress Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("解離性身分障礙症 Dissociative Identity Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("失自我感／失現實感障礙症 Depersonalization / Derealization Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("身體症狀障礙症 Somatic Symptom Disorder"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("睡醒障礙症 Sleep-Wake Disorders"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("精神病症 Psychotic Disorders"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("菸草相關障礙症 Tobacco-Related Disorders"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("酒精相關障礙症 Alcohol-Related Disorders"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("檳榔相關障礙症 Betel-Nut Related Disorders"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            rx.text("藥物相關障礙症 Substance Use Disorders"),
            rx.link(rx.button("未完成"), href="/"),
            rx.link(rx.button("未完成"), href="/"),
            columns="3",
            spacing="5",
            ),
            justify="center",
        ),
        direction="column",
        width="750px",
    )