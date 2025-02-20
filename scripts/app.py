# import tkinter as tk
# from tkinter import ttk, filedialog, messagebox
# import pandas as pd
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# import os
# import traceback
# import logging
# import time
# import random
# from dotenv import load_dotenv

# class JobApplicationBot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Job Application Bot")
#         self.root.geometry("800x600")
        
#         self.create_widgets()
#         self.load_saved_data()
        
#     def create_widgets(self):
#         # Notebook for different sections
#         self.notebook = ttk.Notebook(self.root)
#         self.notebook.pack(fill='both', expand=True)

#         # User Details Tab
#         self.user_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.user_tab, text="User Details")
#         self.create_user_details_tab()

#         # Resume Management Tab
#         self.resume_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.resume_tab, text="Resumes")
#         self.create_resume_tab()

#         # Email Template Tab
#         self.email_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.email_tab, text="Email Template")
#         self.create_email_tab()

#         # Company Data Tab
#         self.company_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.company_tab, text="Company Data")
#         self.create_company_tab()

#         # Control Buttons
#         self.control_frame = ttk.Frame(self.root)
#         self.control_frame.pack(pady=10)
        
#         ttk.Button(self.control_frame, text="Send Applications", command=self.send_applications).pack(side=tk.LEFT, padx=5)
#         ttk.Button(self.control_frame, text="Save Configuration", command=self.save_config).pack(side=tk.LEFT, padx=5)

#     def create_user_details_tab(self):
#         # User details input fields
#         fields = [
#             ("Name:", "name"),
#             ("Email:", "email"),
#             ("App Password:", "app_password"),
#             ("Portfolio URL:", "portfolio"),
#             ("GitHub Profile:", "github"),
#             ("LinkedIn Profile:", "linkedin")
#         ]

#         for i, (label, var_name) in enumerate(fields):
#             frame = ttk.Frame(self.user_tab)
#             frame.pack(fill='x', padx=5, pady=5)
            
#             ttk.Label(frame, text=label).pack(side=tk.LEFT, padx=5)
#             entry = ttk.Entry(frame, width=40)
#             entry.pack(side=tk.RIGHT, expand=True, fill='x')
#             setattr(self, var_name, entry)

#     def create_resume_tab(self):
#         self.resumes = {
#             "Full Stack": None,
#             "Data Analyst": None,
#             "Testing": None
#         }

#         for role in self.resumes:
#             frame = ttk.Frame(self.resume_tab)
#             frame.pack(fill='x', padx=5, pady=5)
            
#             ttk.Label(frame, text=f"{role} Resume:").pack(side=tk.LEFT)
#             btn = ttk.Button(frame, text="Browse", 
#                            command=lambda r=role: self.browse_resume(r))
#             btn.pack(side=tk.RIGHT)
            
#             label = ttk.Label(frame, text="No file selected")
#             label.pack(side=tk.RIGHT, padx=5)
#             setattr(self, f"{role.lower().replace(' ', '_')}_label", label)

#     def browse_resume(self, role):
#         filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
#         if filepath:
#             self.resumes[role] = filepath
#             getattr(self, f"{role.lower().replace(' ', '_')}_label").config(text=filepath)

#     def create_email_tab(self):
#         self.email_template = tk.Text(self.email_tab, wrap=tk.WORD, height=20)
#         self.email_template.pack(fill='both', expand=True, padx=5, pady=5)
        
#         # Load default template
#         self.email_template.insert(tk.END, """Dear {hr_name},

# I am applying for the {job_role} position at {company_name}. 

# [Your custom message here]

# Portfolio: {},
# Linkedin: {},
# Github: {}                                                                    
                                                                      
# Best regards,
# {user_name}""")

#     def create_company_tab(self):
#         frame = ttk.Frame(self.company_tab)
#         frame.pack(pady=10)
        
#         ttk.Button(frame, text="Upload Company Data", command=self.load_company_data).pack()
#         self.company_data_label = ttk.Label(self.company_tab, text="No data loaded")
#         self.company_data_label.pack()

#     def load_company_data(self):
#         filepath = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xls"), ("CSV Files", "*.csv")])
#         if filepath:
#             try:
#                 if filepath.endswith('.csv'):
#                     self.df = pd.read_csv(filepath)
#                 else:
#                     self.df = pd.read_excel(filepath, engine='openpyxl')
#                 self.company_data_label.config(text=f"Loaded {len(self.df)} companies")
#             except Exception as e:
#                 messagebox.showerror("Error", f"Failed to load file: {str(e)}")

#     def save_config(self):
#         # Save user configuration to .env file
#         config = {
#             'NAME': self.name.get(),
#             'EMAIL': self.email.get(),
#             'APP_PASSWORD': self.app_password.get(),
#             'PORTFOLIO': self.portfolio.get(),
#             'GITHUB': self.github.get(),
#             'LINKEDIN': self.linkedin.get()
#         }
        
#         with open('.env', 'w') as f:
#             for key, value in config.items():
#                 f.write(f"{key}={value}\n")
        
#         messagebox.showinfo("Success", "Configuration saved successfully")

#     def load_saved_data(self):
#         if os.path.exists('.env'):
#             load_dotenv()
#             self.name.insert(0, os.getenv('NAME', ''))
#             self.email.insert(0, os.getenv('EMAIL', ''))
#             self.app_password.insert(0, os.getenv('APP_PASSWORD', ''))
#             self.portfolio.insert(0, os.getenv('PORTFOLIO', ''))
#             self.github.insert(0, os.getenv('GITHUB', ''))
#             self.linkedin.insert(0, os.getenv('LINKEDIN', ''))

#     def get_resume(self, job_role):
#         job_role = job_role.lower()
#         if any(kw in job_role for kw in ["frontend", "backend", "full stack", "software"]):
#             return self.resumes["Full Stack"]
#         elif any(kw in job_role for kw in ["data analyst", "data scientist"]):
#             return self.resumes["Data Analyst"]
#         elif any(kw in job_role for kw in ["testing", "qa", "quality assurance"]):
#             return self.resumes["Testing"]
#         return self.resumes["Full Stack"]

#     def generate_cover_letter(self, company_info):
#         template = self.email_template.get("1.0", tk.END)
#         return template.format(
#             hr_name=company_info['HRorHiringTeamName'],
#             company_name=company_info['companyName'],
#             job_role=company_info['jobRole'],
#             user_name=self.name.get(),
#             portfolio=self.portfolio.get(),
#             github=self.github.get(),
#             linkedin=self.linkedin.get()
#         )

#     def send_applications(self):
#         try:
#             server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#             server.login(self.email.get(), self.app_password.get())
            
#             for _, row in self.df.iterrows():
#                 resume_path = self.get_resume(row['jobRole'])
#                 if not resume_path or not os.path.exists(resume_path):
#                     continue
                
#                 msg = MIMEMultipart()
#                 msg['From'] = self.email.get()
#                 msg['To'] = row['companyEmail']
#                 msg['Subject'] = f"Ramesh Bellani - Application for {row['jobRole']}"
                
#                 body = self.generate_cover_letter(row)
#                 msg.attach(MIMEText(body, 'plain'))
                
#                 with open(resume_path, "rb") as f:
#                     part = MIMEApplication(f.read(), Name=os.path.basename(resume_path))
#                     part['Content-Disposition'] = f'attachment; filename="{os.path.basename(resume_path)}"'
#                     msg.attach(part)
                
#                 server.sendmail(self.email.get(), row['companyEmail'], msg.as_string())
#                 time.sleep(random.randint(30, 120))
            
#             server.quit()
#             messagebox.showinfo("Success", "Applications sent successfully!")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to send applications: {str(e)}")
#             logging.error(traceback.format_exc())

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = JobApplicationBot(root)
#     root.mainloop()



# import tkinter as tk
# from tkinter import ttk, filedialog, messagebox
# import pandas as pd
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# import os
# import traceback
# import logging
# import time
# import random
# from dotenv import load_dotenv

# class JobApplicationBot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Job Application Bot")
#         self.root.geometry("800x600")
#         self.root.configure(bg="#f0f0f0")
        
#         # Apply custom styles
#         self.apply_styles()
        
#         self.create_widgets()
#         self.load_saved_data()
        
#     def apply_styles(self):
#         style = ttk.Style()
#         style.theme_use("clam")
        
#         style.configure("TNotebook", background="#f0f0f0", borderwidth=0)
#         style.configure("TNotebook.Tab", font=("Arial", 12, "bold"), padding=[10, 5], foreground="black", background="#c5c5c5")
#         style.map("TNotebook.Tab", background=[("selected", "#007bff")], foreground=[("selected", "white")])

#         style.configure("TButton", font=("Arial", 12), padding=10, relief="flat", background="#007bff", foreground="white")
#         style.map("TButton", background=[("active", "#0056b3")], foreground=[("active", "white")])

#         style.configure("TEntry", font=("Arial", 12), padding=5)
#         style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
#         style.configure("TFrame", background="#f0f0f0")

#     def create_widgets(self):
#         self.notebook = ttk.Notebook(self.root)
#         self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

#         self.user_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.user_tab, text="User Details")
#         self.create_user_details_tab()

#         self.resume_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.resume_tab, text="Resumes")
#         self.create_resume_tab()

#         self.email_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.email_tab, text="Email Template")
#         self.create_email_tab()

#         self.company_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.company_tab, text="Company Data")
#         self.create_company_tab()

#         self.control_frame = ttk.Frame(self.root)
#         self.control_frame.pack(pady=10)
        
#         ttk.Button(self.control_frame, text="Send Applications", command=self.send_applications).pack(side=tk.LEFT, padx=10)
#         ttk.Button(self.control_frame, text="Save Configuration", command=self.save_config).pack(side=tk.LEFT, padx=10)

#     def create_user_details_tab(self):
#         fields = ["Name", "Email", "App Password", "Portfolio URL", "GitHub Profile", "LinkedIn Profile"]
#         self.entries = {}
#         for field in fields:
#             frame = ttk.Frame(self.user_tab)
#             frame.pack(fill='x', padx=5, pady=5)
#             ttk.Label(frame, text=f"{field}:").pack(side=tk.LEFT, padx=5)
#             entry = ttk.Entry(frame, width=40)
#             entry.pack(side=tk.RIGHT, expand=True, fill='x')
#             self.entries[field.lower().replace(" ", "_")] = entry

#     def create_resume_tab(self):
#         self.resumes = {}
#         for role in ["Full Stack", "Data Analyst", "Testing"]:
#             frame = ttk.Frame(self.resume_tab)
#             frame.pack(fill='x', padx=5, pady=5)
#             ttk.Label(frame, text=f"{role} Resume:").pack(side=tk.LEFT)
#             btn = ttk.Button(frame, text="Browse", command=lambda r=role: self.browse_resume(r))
#             btn.pack(side=tk.RIGHT)
#             label = ttk.Label(frame, text="No file selected")
#             label.pack(side=tk.RIGHT, padx=5)
#             self.resumes[role] = {'path': None, 'label': label}

#     def browse_resume(self, role):
#         filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
#         if filepath:
#             self.resumes[role]['path'] = filepath
#             self.resumes[role]['label'].config(text=os.path.basename(filepath))

#     def create_email_tab(self):
#         self.email_template = tk.Text(self.email_tab, wrap=tk.WORD, height=15, font=("Arial", 12))
#         self.email_template.pack(fill='both', expand=True, padx=5, pady=5)
#         self.email_template.insert(tk.END, """Dear {hr_name},\n\nI am applying for the {job_role} position at {company_name}.\n\n[Your custom message here]\n\nPortfolio: {portfolio}\nLinkedIn: {linkedin}\nGitHub: {github}\n\nBest regards,\n{user_name}""")

#     def create_company_tab(self):
#         frame = ttk.Frame(self.company_tab)
#         frame.pack(pady=10)
#         ttk.Button(frame, text="Upload Company Data", command=self.load_company_data).pack()
#         self.company_data_label = ttk.Label(self.company_tab, text="No data loaded")
#         self.company_data_label.pack()

#     def load_company_data(self):
#         filepath = filedialog.askopenfilename(filetypes=[("Excel/CSV", "*.xlsx *.xls *.csv")])
#         if filepath:
#             self.df = pd.read_csv(filepath) if filepath.endswith('.csv') else pd.read_excel(filepath)
#             self.company_data_label.config(text=f"Loaded {len(self.df)} companies")

#     def save_config(self):
#         with open('.env', 'w') as f:
#             for key, entry in self.entries.items():
#                 f.write(f"{key.upper()}={entry.get()}\n")
#         messagebox.showinfo("Success", "Configuration saved successfully")

#     def load_saved_data(self):
#         if os.path.exists('.env'):
#             load_dotenv()
#             for key, entry in self.entries.items():
#                 entry.insert(0, os.getenv(key.upper(), ""))

#     def send_applications(self):
#         try:
#             server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#             server.login(self.entries['email'].get(), self.entries['app_password'].get())
#             for _, row in self.df.iterrows():
#                 resume_path = self.resumes.get(row['jobRole'], {}).get('path')
#                 if not resume_path:
#                     continue
#                 msg = MIMEMultipart()
#                 msg['From'] = self.entries['email'].get()
#                 msg['To'] = row['companyEmail']
#                 msg['Subject'] = f"Application for {row['jobRole']}"
#                 body = self.email_template.get("1.0", tk.END)
#                 msg.attach(MIMEText(body, 'plain'))
#                 with open(resume_path, "rb") as f:
#                     msg.attach(MIMEApplication(f.read(), Name=os.path.basename(resume_path)))
#                 server.sendmail(msg['From'], msg['To'], msg.as_string())
#                 time.sleep(random.randint(30, 60))
#             server.quit()
#             messagebox.showinfo("Success", "Applications sent successfully!")
#             for entry in self.entries.values():
#                 entry.delete(0, tk.END)
#         except Exception:
#             messagebox.showerror("Error", traceback.format_exc())

# root = tk.Tk()
# app = JobApplicationBot(root)
# root.mainloop()




# import tkinter as tk
# from tkinter import ttk, filedialog, messagebox
# import pandas as pd
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# import os
# import traceback
# import logging
# import time
# import random
# from dotenv import load_dotenv

# class JobApplicationBot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Job Application Bot")
#         self.root.geometry("1000x700")
#         self.root.configure(bg="#2c3e50")
        
#         # Configure styles
#         self.apply_styles()
        
#         self.create_widgets()
#         self.load_saved_data()
        
#     def apply_styles(self):
#         style = ttk.Style()
#         style.theme_use('clam')
        
#         # Configure colors
#         bg_color = "#2c3e50"
#         fg_color = "#ecf0f1"
#         accent_color = "#3498db"
#         entry_bg = "#34495e"
        
#         style.configure(".", background=bg_color, foreground=fg_color)
#         style.configure("TNotebook", background=bg_color)
#         style.configure("TNotebook.Tab", background="#34495e", foreground=fg_color,
#                         padding=[15, 5], font=('Helvetica', 10, 'bold'))
#         style.map("TNotebook.Tab", background=[("selected", accent_color)])
        
#         style.configure("TFrame", background=bg_color)
#         style.configure("TLabel", background=bg_color, foreground=fg_color,
#                         font=('Helvetica', 10))
#         style.configure("TButton", background=accent_color, foreground=fg_color,
#                         font=('Helvetica', 10, 'bold'), borderwidth=0)
#         style.map("TButton", background=[("active", "#2980b9")])
        
#         style.configure("TEntry", fieldbackground=entry_bg, foreground=fg_color,
#                         insertcolor=fg_color, borderwidth=0)
        
#     def create_widgets(self):
#         # Main notebook
#         self.notebook = ttk.Notebook(self.root)
#         self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

#         # Create tabs
#         self.create_user_tab()
#         self.create_resume_tab()
#         self.create_email_tab()
#         self.create_company_tab()
        
#         # Control buttons
#         self.control_frame = ttk.Frame(self.root)
#         self.control_frame.pack(pady=20)
        
#         send_btn = ttk.Button(self.control_frame, text="Send Applications", 
#                             command=self.send_applications)
#         send_btn.pack(side=tk.LEFT, padx=10)
        
#         save_btn = ttk.Button(self.control_frame, text="Save Configuration", 
#                             command=self.save_config)
#         save_btn.pack(side=tk.LEFT, padx=10)

#     def create_user_tab(self):
#         self.user_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.user_tab, text="User Details")
        
#         fields = [
#             ("Name:", "name"),
#             ("Email:", "email"),
#             ("App Password:", "app_password"),
#             ("Portfolio URL:", "portfolio"),
#             ("GitHub Profile:", "github"),
#             ("LinkedIn Profile:", "linkedin")
#         ]
        
#         container = ttk.Frame(self.user_tab)
#         container.pack(padx=20, pady=20)
        
#         for i, (label, var_name) in enumerate(fields):
#             frame = ttk.Frame(container)
#             frame.pack(fill='x', pady=5)
            
#             lbl = ttk.Label(frame, text=label, width=15, anchor='w')
#             lbl.pack(side=tk.LEFT)
            
#             entry = ttk.Entry(frame, width=40)
#             entry.pack(side=tk.RIGHT, expand=True, fill='x', padx=10)
#             setattr(self, var_name, entry)

#     def create_resume_tab(self):
#         self.resume_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.resume_tab, text="Resumes")
        
#         self.resumes = {
#             "Full Stack": None,
#             "Data Analyst": None,
#             "Testing": None
#         }
        
#         container = ttk.Frame(self.resume_tab)
#         container.pack(padx=20, pady=20)
        
#         for role in self.resumes:
#             frame = ttk.Frame(container)
#             frame.pack(fill='x', pady=8)
            
#             lbl = ttk.Label(frame, text=f"{role} Resume:", width=15, anchor='w')
#             lbl.pack(side=tk.LEFT)
            
#             btn = ttk.Button(frame, text="Browse", 
#                            command=lambda r=role: self.browse_resume(r))
#             btn.pack(side=tk.RIGHT)
            
#             label = ttk.Label(frame, text="No file selected", width=40)
#             label.pack(side=tk.RIGHT, padx=10)
#             setattr(self, f"{role.lower().replace(' ', '_')}_label", label)

#     def create_email_tab(self):
#         self.email_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.email_tab, text="Email Template")
        
#         container = ttk.Frame(self.email_tab)
#         container.pack(fill='both', expand=True, padx=20, pady=20)
        
#         self.email_template = tk.Text(container, wrap=tk.WORD, height=20,
#                                     bg="#34495e", fg="#ecf0f1", insertbackground="white",
#                                     font=('Consolas', 10), padx=10, pady=10)
#         self.email_template.pack(fill='both', expand=True)
        
#         # Load default template
#         default_template = """Dear {hr_name},

# I am applying for the {job_role} position at {company_name}. 

# [Your custom message here]

# Portfolio: {portfolio}
# LinkedIn: {linkedin}
# GitHub: {github}                                                                    
                                                                      
# Best regards,
# {user_name}"""
#         self.email_template.insert(tk.END, default_template)

#     def create_company_tab(self):
#         self.company_tab = ttk.Frame(self.notebook)
#         self.notebook.add(self.company_tab, text="Company Data")
        
#         container = ttk.Frame(self.company_tab)
#         container.pack(pady=30)
        
#         btn = ttk.Button(container, text="Upload Company Data", 
#                         command=self.load_company_data)
#         btn.pack(pady=10)
        
#         self.company_data_label = ttk.Label(container, text="No data loaded")
#         self.company_data_label.pack()

#     def browse_resume(self, role):
#         filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
#         if filepath:
#             self.resumes[role] = filepath
#             label = getattr(self, f"{role.lower().replace(' ', '_')}_label")
#             label.config(text=os.path.basename(filepath))

#     def load_company_data(self):
#         filepath = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xls"), ("CSV Files", "*.csv")])
#         if filepath:
#             try:
#                 if filepath.endswith('.csv'):
#                     self.df = pd.read_csv(filepath)
#                 else:
#                     self.df = pd.read_excel(filepath, engine='openpyxl')
#                 self.company_data_label.config(text=f"Loaded {len(self.df)} companies")
#             except Exception as e:
#                 messagebox.showerror("Error", f"Failed to load file: {str(e)}")

#     def save_config(self):
#         config = {
#             'NAME': self.name.get(),
#             'EMAIL': self.email.get(),
#             'APP_PASSWORD': self.app_password.get(),
#             'PORTFOLIO': self.portfolio.get(),
#             'GITHUB': self.github.get(),
#             'LINKEDIN': self.linkedin.get()
#         }
        
#         with open('.env', 'w') as f:
#             for key, value in config.items():
#                 f.write(f"{key}={value}\n")
        
#         messagebox.showinfo("Success", "Configuration saved successfully")

#     def load_saved_data(self):
#         if os.path.exists('.env'):
#             load_dotenv()
#             self.name.insert(0, os.getenv('NAME', ''))
#             self.email.insert(0, os.getenv('EMAIL', ''))
#             self.app_password.insert(0, os.getenv('APP_PASSWORD', ''))
#             self.portfolio.insert(0, os.getenv('PORTFOLIO', ''))
#             self.github.insert(0, os.getenv('GITHUB', ''))
#             self.linkedin.insert(0, os.getenv('LINKEDIN', ''))

#     def clear_user_data(self):
#         # Clear entry fields
#         self.name.delete(0, tk.END)
#         self.email.delete(0, tk.END)
#         self.app_password.delete(0, tk.END)
#         self.portfolio.delete(0, tk.END)
#         self.github.delete(0, tk.END)
#         self.linkedin.delete(0, tk.END)
        
#         # Clear resume selections
#         for role in self.resumes:
#             getattr(self, f"{role.lower().replace(' ', '_')}_label").config(text="No file selected")
#             self.resumes[role] = None
        
#         # Clear company data
#         self.df = pd.DataFrame()
#         self.company_data_label.config(text="No data loaded")

#     def send_applications(self):
#         try:
#             server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#             server.login(self.email.get(), self.app_password.get())
            
#             for _, row in self.df.iterrows():
#                 resume_path = self.get_resume(row['jobRole'])
#                 if not resume_path or not os.path.exists(resume_path):
#                     continue
                
#                 msg = MIMEMultipart()
#                 msg['From'] = self.email.get()
#                 msg['To'] = row['companyEmail']
#                 msg['Subject'] = f"Application for {row['jobRole']}"
                
#                 body = self.generate_cover_letter(row)
#                 msg.attach(MIMEText(body, 'plain'))
                
#                 with open(resume_path, "rb") as f:
#                     part = MIMEApplication(f.read(), Name=os.path.basename(resume_path))
#                     part['Content-Disposition'] = f'attachment; filename="{os.path.basename(resume_path)}"'
#                     msg.attach(part)
                
#                 server.sendmail(self.email.get(), row['companyEmail'], msg.as_string())
#                 time.sleep(random.randint(30, 120))
            
#             server.quit()
#             self.clear_user_data()
#             messagebox.showinfo("Success", "Applications sent successfully!\nAll fields have been reset.")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to send applications: {str(e)}")
#             logging.error(traceback.format_exc())

#     def get_resume(self, job_role):
#         job_role = job_role.lower()
#         if any(kw in job_role for kw in ["frontend", "backend", "full stack", "software"]):
#             return self.resumes["Full Stack"]
#         elif any(kw in job_role for kw in ["data analyst", "data scientist"]):
#             return self.resumes["Data Analyst"]
#         elif any(kw in job_role for kw in ["testing", "qa", "quality assurance"]):
#             return self.resumes["Testing"]
#         return self.resumes["Full Stack"]

#     def generate_cover_letter(self, company_info):
#         template = self.email_template.get("1.0", tk.END)
#         return template.format(
#             hr_name=company_info['HRorHiringTeamName'],
#             company_name=company_info['companyName'],
#             job_role=company_info['jobRole'],
#             user_name=self.name.get(),
#             portfolio=self.portfolio.get(),
#             github=self.github.get(),
#             linkedin=self.linkedin.get()
#         )

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = JobApplicationBot(root)
#     root.mainloop()






import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import traceback
import logging
import time
import random
from dotenv import load_dotenv

class JobApplicationBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Application Bot")
        self.root.geometry("1000x700")
        self.root.configure(bg="#2c3e50")
        
        # Configure styles
        self.apply_styles()
        
        self.create_widgets()
        self.load_saved_data()
        
    def apply_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        bg_color = "#2c3e50"
        fg_color = "#ecf0f1"
        accent_color = "#3498db"
        entry_bg = "#34495e"
        button_hover = "#2980b9"
        
        style.configure(".", background=bg_color, foreground=fg_color, font=('Helvetica', 10))
        style.configure("TNotebook", background=bg_color)
        style.configure("TNotebook.Tab", background="#34495e", foreground=fg_color,
                        padding=[15, 5], font=('Helvetica', 12, 'bold'))
        style.map("TNotebook.Tab", background=[("selected", accent_color)])
        
        style.configure("TFrame", background=bg_color)
        style.configure("TLabel", background=bg_color, foreground=fg_color,
                        font=('Helvetica', 12))
        style.configure("TButton", background=accent_color, foreground=fg_color,
                        font=('Helvetica', 12, 'bold'), borderwidth=0, padding=10)
        style.map("TButton", background=[("active", button_hover)])
        
        style.configure("TEntry", fieldbackground=entry_bg, foreground=fg_color,
                        insertcolor=fg_color, borderwidth=0, font=('Helvetica', 12))
        
        style.configure("TText", background=entry_bg, foreground=fg_color,
                        insertbackground=fg_color, font=('Consolas', 10))
        
    def create_widgets(self):
        # Main notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Create tabs
        self.create_user_tab()
        self.create_resume_tab()
        self.create_email_tab()
        self.create_company_tab()
        
        # Control buttons
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(pady=20)
        
        send_btn = ttk.Button(self.control_frame, text="Send Applications", 
                            command=self.send_applications)
        send_btn.pack(side=tk.LEFT, padx=10)
        
        save_btn = ttk.Button(self.control_frame, text="Save Configuration", 
                            command=self.save_config)
        save_btn.pack(side=tk.LEFT, padx=10)

    def create_user_tab(self):
        self.user_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.user_tab, text="User Details")
        
        fields = [
            ("Name:", "name"),
            ("Email:", "email"),
            ("App Password:", "app_password"),
            ("Portfolio URL:", "portfolio"),
            ("GitHub Profile:", "github"),
            ("LinkedIn Profile:", "linkedin")
        ]
        
        container = ttk.Frame(self.user_tab)
        container.pack(padx=20, pady=20)
        
        for i, (label, var_name) in enumerate(fields):
            frame = ttk.Frame(container)
            frame.pack(fill='x', pady=10)
            
            lbl = ttk.Label(frame, text=label, width=15, anchor='w')
            lbl.pack(side=tk.LEFT, padx=10)
            
            entry = ttk.Entry(frame, width=40)
            entry.pack(side=tk.RIGHT, expand=True, fill='x', padx=10)
            setattr(self, var_name, entry)

    def create_resume_tab(self):
        self.resume_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.resume_tab, text="Resumes")
        
        self.resumes = {
            "Full Stack": None,
            "Data Analyst": None,
            "Testing": None
        }
        
        container = ttk.Frame(self.resume_tab)
        container.pack(padx=20, pady=20)
        
        for role in self.resumes:
            frame = ttk.Frame(container)
            frame.pack(fill='x', pady=10)
            
            lbl = ttk.Label(frame, text=f"{role} Resume:", width=15, anchor='w')
            lbl.pack(side=tk.LEFT, padx=10)
            
            btn = ttk.Button(frame, text="Browse", 
                           command=lambda r=role: self.browse_resume(r))
            btn.pack(side=tk.RIGHT)
            
            label = ttk.Label(frame, text="No file selected", width=40)
            label.pack(side=tk.RIGHT, padx=10)
            setattr(self, f"{role.lower().replace(' ', '_')}_label", label)

    def create_email_tab(self):
        self.email_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.email_tab, text="Email Template")
        
        container = ttk.Frame(self.email_tab)
        container.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.email_template = tk.Text(container, wrap=tk.WORD, height=20,
                                    bg="#34495e", fg="#ecf0f1", insertbackground="white",
                                    font=('Consolas', 10), padx=10, pady=10)
        self.email_template.pack(fill='both', expand=True)
        
        # Load default template
        default_template = """Dear {hr_name},

I am applying for the {job_role} position at {company_name}. 

[Your custom message here]

Portfolio: {portfolio}
LinkedIn: {linkedin}
GitHub: {github}                                                                    
                                                                      
Best regards,
{user_name}"""
        self.email_template.insert(tk.END, default_template)

    def create_company_tab(self):
        self.company_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.company_tab, text="Company Data")
        
        container = ttk.Frame(self.company_tab)
        container.pack(pady=30)
        
        btn = ttk.Button(container, text="Upload Company Data", 
                        command=self.load_company_data)
        btn.pack(pady=10)
        
        self.company_data_label = ttk.Label(container, text="No data loaded")
        self.company_data_label.pack()

    def browse_resume(self, role):
        filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if filepath:
            self.resumes[role] = filepath
            label = getattr(self, f"{role.lower().replace(' ', '_')}_label")
            label.config(text=os.path.basename(filepath))

    def load_company_data(self):
        filepath = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xls"), ("CSV Files", "*.csv")])
        if filepath:
            try:
                if filepath.endswith('.csv'):
                    self.df = pd.read_csv(filepath)
                else:
                    self.df = pd.read_excel(filepath, engine='openpyxl')
                self.company_data_label.config(text=f"Loaded {len(self.df)} companies")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {str(e)}")

    def save_config(self):
        config = {
            'NAME': self.name.get(),
            'EMAIL': self.email.get(),
            'APP_PASSWORD': self.app_password.get(),
            'PORTFOLIO': self.portfolio.get(),
            'GITHUB': self.github.get(),
            'LINKEDIN': self.linkedin.get()
        }
        
        with open('.env', 'w') as f:
            for key, value in config.items():
                f.write(f"{key}={value}\n")
        
        messagebox.showinfo("Success", "Configuration saved successfully")

    def load_saved_data(self):
        if os.path.exists('.env'):
            load_dotenv()
            self.name.insert(0, os.getenv('NAME', ''))
            self.email.insert(0, os.getenv('EMAIL', ''))
            self.app_password.insert(0, os.getenv('APP_PASSWORD', ''))
            self.portfolio.insert(0, os.getenv('PORTFOLIO', ''))
            self.github.insert(0, os.getenv('GITHUB', ''))
            self.linkedin.insert(0, os.getenv('LINKEDIN', ''))

    def clear_user_data(self):
        # Clear entry fields
        self.name.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.app_password.delete(0, tk.END)
        self.portfolio.delete(0, tk.END)
        self.github.delete(0, tk.END)
        self.linkedin.delete(0, tk.END)
        
        # Clear resume selections
        for role in self.resumes:
            getattr(self, f"{role.lower().replace(' ', '_')}_label").config(text="No file selected")
            self.resumes[role] = None
        
        # Clear company data
        self.df = pd.DataFrame()
        self.company_data_label.config(text="No data loaded")

    def send_applications(self):
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(self.email.get(), self.app_password.get())
            
            for _, row in self.df.iterrows():
                resume_path = self.get_resume(row['jobRole'])
                if not resume_path or not os.path.exists(resume_path):
                    continue
                
                msg = MIMEMultipart()
                msg['From'] = self.email.get()
                msg['To'] = row['companyEmail']
                msg['Subject'] = f"Application for {row['jobRole']}"
                
                body = self.generate_cover_letter(row)
                msg.attach(MIMEText(body, 'plain'))
                
                with open(resume_path, "rb") as f:
                    part = MIMEApplication(f.read(), Name=os.path.basename(resume_path))
                    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(resume_path)}"'
                    msg.attach(part)
                
                server.sendmail(self.email.get(), row['companyEmail'], msg.as_string())
                time.sleep(random.randint(30, 120))
            
            server.quit()
            self.clear_user_data()
            messagebox.showinfo("Success", "Applications sent successfully!\nAll fields have been reset.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send applications: {str(e)}")
            logging.error(traceback.format_exc())

    def get_resume(self, job_role):
        job_role = job_role.lower()
        if any(kw in job_role for kw in ["frontend", "backend", "full stack", "software"]):
            return self.resumes["Full Stack"]
        elif any(kw in job_role for kw in ["data analyst", "data scientist"]):
            return self.resumes["Data Analyst"]
        elif any(kw in job_role for kw in ["testing", "qa", "quality assurance"]):
            return self.resumes["Testing"]
        return self.resumes["Full Stack"]

    def generate_cover_letter(self, company_info):
        template = self.email_template.get("1.0", tk.END)
        return template.format(
            hr_name=company_info['HRorHiringTeamName'],
            company_name=company_info['companyName'],
            job_role=company_info['jobRole'],
            user_name=self.name.get(),
            portfolio=self.portfolio.get(),
            github=self.github.get(),
            linkedin=self.linkedin.get()
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = JobApplicationBot(root)
    root.mainloop()