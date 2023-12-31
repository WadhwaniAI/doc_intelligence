import gradio as gr
from doc_intelligence.transform.doc_pre_processor import Doc_Preprocessor

def image_processor(image, processing_technique):

    image.save("./data/deskew/temp.png")

    obj = Doc_Preprocessor()

    if processing_technique == "deskew": 
        processed_image = obj.deskew_image('./data/deskew/temp.png')
        return processed_image, round(obj.angle_correction, 4)
    elif processing_technique == "shadow remover": 
        processed_image = obj.shadow_remove('./data/deskew/temp.png')
        return processed_image, ""
    elif processing_technique == "line remover": 
        processed_image = obj.remove_horz_verti_lines('./data/deskew/temp.png', True)
        processed_image.save('./data/line_remover/result.png')
        return processed_image, ""
    else: 
        processed_image = image

    return None, None

demo = gr.Interface(fn=image_processor, 
            inputs=[gr.Image(type="pil"), gr.Dropdown(
            ["deskew", "dewarp", "line remover", "shadow remover"], label="Pre-Processing Techniques", info="Apply any doc-processing techniques you want!!"
            )], 
            outputs=[gr.Image(label="Processed Image"), gr.Textbox(label="Skew Angle Corrected")],
            examples=[
                ["./data/deskew/img4.jpg"],
                ["./data/deskew/img8.jpg"],
                ["./data/deskew/Blood_report_1.png"],
                ["./data/shadow_remover/test_image_1.png"],
                ["./data/line_remover/test_img_2.png"]
            ])
demo.launch()