#SelectorScreen Original
#inputLabel: inputLabel
#    inputBox: inputBox
    
#	BoxLayout:
#        orientation: 'vertical'
#		padding: root.width*0.02, root.height*0.02
#        WrappedLabel:
#            id: inputLabel
#            text: 'Text Input'
#            font_size: min(root.height, root.width) / 10
#        BoxLayout: 
#            orientation: 'horizontal' 
#            size_hint_y: None
#            WrappedLabel:
#                id: inputBox
#                text: ''
#                font_size: min(root.height, root.width) / 10
#            Button:
#                id: clearn_btn
#                text: '[b]Clear[/b]'
#                markup: True
#                size_hint: 0.3, None
#                height: inputLabel.texture_size[1]
#                on_release: inputBox.text = ''  