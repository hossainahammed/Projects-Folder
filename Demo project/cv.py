import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors




def generate_cover_page():
    query_result = query_var.get()
    user_name = name_entry.get()
    user_id = id_entry.get()
    course_code = course_code_entry.get()
    course_title = course_title_entry.get()
    topic_title = topic_title_entry.get()
    teacher_name = teacher_name_entry.get()
    teacher_designation = teacher_designation_entry.get()
    submission_date = submission_date_entry.get()

    # Create PDF canvas
    c = canvas.Canvas("Cover_Page.pdf", pagesize=letter)

    # Write cover page content
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(300, 700, query_result + " Cover Page")

    # Course Information
    c.setFont("Helvetica", 12)
    c.drawString(50, 600, "Course Code: " + course_code)
    c.drawString(50, 580, "Course Title: " + course_title)
    c.drawString(50, 560, "Topic Title: " + topic_title)

    # Draw a line to separate sections
    c.line(50, 550, 550, 550)

    # Calculate the height of the footer section
    footer_height = 100

    # Move the cursor to the footer section
    c.translate(0, footer_height)

    # Teacher and Submission Information
    c.drawString(50, 50, "Teacher:")
    c.drawString(50, 30, teacher_name)
    c.drawString(50, 10, teacher_designation)
    c.drawString(400, 50, "Submission:")
    c.drawString(400, 30, "Name: " + user_name)
    c.drawString(400, 10, "ID: " + user_id)

    # Table Data
    table_data = [
        ["Course Title:", course_title],
        ["Topic Title:", topic_title],
        ["Course Code:", course_code]
    ]

    # Create Table
    table = Table(table_data, colWidths=[150, 350])

    # Add Style to Table
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black),
                               ('TOPPADDING', (0, 0), (-1, -1), 5),
                               ('LEFTPADDING', (0, 0), (-1, -1), 5),
                               ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                               ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)]))

    # Draw Table on Canvas
    table.wrapOn(c, 200, 400)
    table.drawOn(c, 50, 500)  # Adjust position as necessary

    # Teacher and Submission Information Table Data
    teacher_submission_data = [
        ["Teacher:", teacher_name],
        ["", teacher_designation],
        ["Submission:", ""],
        ["", "Name: " + user_name],
        ["", "ID: " + user_id]
    ]

    # Create Teacher and Submission Information Table
    teacher_submission_table = Table(teacher_submission_data, colWidths=[150, 350])

    # Add Style to Teacher and Submission Information Table
    teacher_submission_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black),
                               ('TOPPADDING', (0, 0), (-1, -1), 5),
                               ('LEFTPADDING', (0, 0), (-1, -1), 5),
                               ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                               ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)]))

    # Draw Teacher and Submission Information Table on Canvas
    teacher_submission_table.wrapOn(c, 200, 400)
    teacher_submission_table.drawOn(c, 50, 50)  # Adjust position as necessary

    # Group Information
    if group_checkbox_value.get():
        group_name = group_name_entry.get()
        c.drawString(400, -10, "Group Name: " + group_name)
        c.drawString(400, -30, "Group Members:")
        y_coordinate = -50
        for i, (name, _id) in enumerate(group_members.values(), start=1):
            c.drawString(400, y_coordinate - i * 20, f"Name: {name}, ID: {_id}")
            if i >= 5:
                break

        # Submission Date after group member info
        c.drawString(400, y_coordinate - (i + 1) * 20, "Submission Date: " + submission_date)
    else:
        # Submission Date for individual project
        c.drawString(400, -10, "Submission Date: " + submission_date)

    # Save the canvas
    c.save()
    messagebox.showinfo("Cover Page Generated", "Cover Page generated successfully as Cover_Page.pdf")








def add_member_info():
    global current_member
    member_name = member_name_entry.get()
    member_id = member_id_entry.get()
    group_members[current_member] = (member_name, member_id)
    current_member += 1
    if current_member < group_quantity:
        member_name_label.config(text=f"Member {current_member + 1} Name:")
        member_name_entry.delete(0, tk.END)
        member_id_entry.delete(0, tk.END)
    else:
        group_members_frame.destroy()


def group_members_input():
    global group_members_frame
    global current_member
    global group_quantity

    group_quantity_str = group_members_entry.get()
    if group_quantity_str.strip():  # Check if input is not empty
        group_quantity = int(group_quantity_str)
        if group_quantity > 0:
            group_members_frame = tk.Frame(root)
            group_members_frame.grid(row=12, column=0, columnspan=2, padx=10, pady=10)
            current_member = 0

            member_name_label.grid(row=current_member, column=0, padx=10, pady=5)
            member_name_entry.grid(row=current_member, column=1, padx=10, pady=5)

            member_id_label.grid(row=current_member + 1, column=0, padx=10, pady=5)
            member_id_entry.grid(row=current_member + 1, column=1, padx=10, pady=5)

            add_member_button.grid(row=current_member + 2, column=0, columnspan=2, padx=10, pady=5)
        else:
            messagebox.showerror("Error", "Please enter a valid quantity of group members.")
    else:
        messagebox.showerror("Error", "Please enter the quantity of group members.")


# GUI setup
root = tk.Tk()
root.title("Cover Page Generator")

query_var = tk.StringVar(root)
query_var.set("Select Cover Page Type")
query_options = ["Lab Report", "Assignment", "Research Paper", "Project"]
query_dropdown = tk.OptionMenu(root, query_var, *query_options)
query_dropdown.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10)

id_label = tk.Label(root, text="ID:")
id_label.grid(row=2, column=0, padx=10, pady=10)
id_entry = tk.Entry(root)
id_entry.grid(row=2, column=1, padx=10, pady=10)

course_code_label = tk.Label(root, text="Course Code:")
course_code_label.grid(row=3, column=0, padx=10, pady=10)
course_code_entry = tk.Entry(root)
course_code_entry.grid(row=3, column=1, padx=10, pady=10)

course_title_label = tk.Label(root, text="Course Title:")
course_title_label.grid(row=4, column=0, padx=10, pady=10)
course_title_entry = tk.Entry(root)
course_title_entry.grid(row=4, column=1, padx=10, pady=10)

topic_title_label = tk.Label(root, text="Topic Title:")
topic_title_label.grid(row=5, column=0, padx=10, pady=10)
topic_title_entry = tk.Entry(root)
topic_title_entry.grid(row=5, column=1, padx=10, pady=10)

teacher_name_label = tk.Label(root, text="Teacher Name:")
teacher_name_label.grid(row=6, column=0, padx=10, pady=10)
teacher_name_entry = tk.Entry(root)
teacher_name_entry.grid(row=6, column=1, padx=10, pady=10)

teacher_designation_label = tk.Label(root, text="Teacher Designation:")
teacher_designation_label.grid(row=7, column=0, padx=10, pady=10)
teacher_designation_entry = tk.Entry(root)
teacher_designation_entry.grid(row=7, column=1, padx=10, pady=10)

submission_date_label = tk.Label(root, text="Submission Date:")
submission_date_label.grid(row=8, column=0, padx=10, pady=10)
submission_date_entry = tk.Entry(root)
submission_date_entry.grid(row=8, column=1, padx=10, pady=10)

group_checkbox_value = tk.BooleanVar(root)
group_checkbox = tk.Checkbutton(root, text="Group Project", variable=group_checkbox_value, command=group_members_input)
group_checkbox.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

group_name_label = tk.Label(root, text="Group Name:")
group_name_label.grid(row=10, column=0, padx=10, pady=10)
group_name_entry = tk.Entry(root)
group_name_entry.grid(row=10, column=1, padx=10, pady=10)

group_members_label = tk.Label(root, text="Group Members Quantity:")
group_members_label.grid(row=11, column=0, padx=10, pady=10)
group_members_entry = tk.Entry(root)
group_members_entry.grid(row=11, column=1, padx=10, pady=10)

member_name_label = tk.Label(root, text="Member 1 Name:")
member_name_entry = tk.Entry(root)
member_id_label = tk.Label(root, text="Member 1 ID:")
member_id_entry = tk.Entry(root)
add_member_button = tk.Button(root, text="Add Member", command=add_member_info)

generate_button = tk.Button(root, text="Generate Cover Page", command=generate_cover_page)
generate_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10)

group_members = {}
group_members_frame = None
current_member = 0
group_quantity = 0

root.mainloop()
