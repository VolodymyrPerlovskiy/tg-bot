from health_check import drift

def set_marks():
    content = tuple(drift.current_status())
    if len(content) != 0 and content[1] == True:
        marker="✅"
    if len(content) != 0 and content[1] == False:
        marker="❌"

    return marker

def set_icons():
    content = tuple(drift.current_status())
    if len(content) != 0 and content[1] == 'True':
        icon="✅"
    if len(content) !=0 and content[1] == 'False':
        icon="❌"
    
    return icon
