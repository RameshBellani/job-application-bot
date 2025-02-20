# Job Application Bot

This Python application automates the process of sending job applications by handling user details, resumes, email templates, and company data. It allows users to input their personal information, upload multiple resumes, write an email cover letter, and upload a company database with job openings. Once configured, the bot will send applications to each company listed in the database.

## Features

- **User Details Management**: Store and retrieve personal details like name, email, portfolio, GitHub, and LinkedIn.
- **Resume Upload**: Upload multiple resumes for different job roles such as Full Stack Developer, Data Analyst, and Testing.
- **Email Template**: Create and store a default email template that can be customized for each job application.
- **Company Database**: Load an Excel or CSV file containing company information and job roles.
- **Automated Email Sending**: Automatically sends email applications with the respective resumes and cover letters.

## Requirements

- Python 3.x
- Libraries:
  - `tkinter` (for the GUI)
  - `pandas` (for reading company data)
  - `smtplib` (for sending emails)
  - `email` (for creating email content and attachments)
  - `openpyxl` (for reading `.xlsx` files)
  - `dotenv` (for environment variable management)
  
You can install required libraries using `pip`:

```bash
pip install pandas openpyxl python-dotenv
```

## Usage

1. **Start the Application**:  
   To run the application, simply execute the Python script:

   ```bash
   python job_application_bot.py
   ```

2. **User Details**:  
   - Enter your full name, email, app password (for Gmail), portfolio URL, GitHub profile, and LinkedIn profile.
   - You can save your details to a `.env` file for later use. Simply click on the "Save Configuration" button.

3. **Resumes**:  
   - Upload the relevant resumes for different job roles (Full Stack, Data Analyst, Testing) using the "Browse" buttons.

4. **Email Template**:  
   - The email template is loaded by default. You can modify it as per your preference. The placeholders (`{hr_name}`, `{job_role}`, `{company_name}`, `{portfolio}`, `{github}`, `{linkedin}`, `{user_name}`) will be automatically replaced with the respective values.

5. **Company Data**:  
   - Upload a CSV or Excel file that contains the company's details, including:
     - `companyName`
     - `companyEmail`
     - `jobRole`
     - `HRorHiringTeamName`
   - This file is used to send applications to the listed companies.

6. **Send Applications**:  
   - After configuring all details, click on the "Send Applications" button. The bot will:
     - Use the correct resume for each job role.
     - Generate a customized cover letter for each application.
     - Send the email with the resume and cover letter to the corresponding company.

7. **Clear Data**:  
   - After sending applications, your personal details, resumes, and company data will be cleared.

## File Structure

- `job_application_bot.py`: Main Python script with the GUI and bot logic.
- `.env`: Stores configuration data like your email and app password (optional).
- `README.md`: This file.

## Example Company Data (CSV or Excel)

The company data file should have the following columns:

| companyName  | companyEmail         | jobRole        | HRorHiringTeamName |
|--------------|----------------------|----------------|--------------------|
| ABC Corp     | hr@abccorp.com       | Full Stack     | John Doe           |
| XYZ Ltd      | careers@xyz.com      | Data Analyst   | Jane Smith         |

The bot will send emails to the respective companies with the correct resume and a personalized cover letter.

## Email Template Example

Here's an example of a default email template:

```plaintext
Dear {hr_name},

I am applying for the {job_role} position at {company_name}. 

[Your custom message here]

Portfolio: {portfolio}
LinkedIn: {linkedin}
GitHub: {github}                                                                    
                                                                      
Best regards,
{user_name}
```

## Troubleshooting

1. **Missing Libraries**:  
   If you receive an error related to missing libraries, you may need to install them using `pip`.

2. **SMTP Errors**:  
   If you encounter an error while sending emails (e.g., "Login Failed"), ensure that:
   - You have enabled "Less Secure Apps" on your Gmail account.
   - You are using an app password if you have 2-factor authentication enabled.

3. **File Loading Issues**:  
   Ensure that the company data file is formatted correctly (CSV or Excel) and contains the necessary columns.

## License

This project is open-source and available under the MIT License.

## Acknowledgements

- This project uses `tkinter` for the graphical user interface.
- The email functionality relies on Python's `smtplib` and `email` modules.
- The project uses the `dotenv` library for managing sensitive information (such as email credentials) securely.

## Author

- Created by Ramesh Bellani
```

### Explanation

- **Introduction**: Briefly explains what the app does and its core features.
- **Requirements**: Lists the necessary dependencies for the app.
- **Usage**: Provides instructions on how to run the app, interact with the GUI, and use the features.
- **File Structure**: Outlines the project structure and relevant files.
- **Company Data**: Explains the required format for the company data file (CSV/Excel).
- **Email Template**: Provides a sample email template used for the cover letter.
- **Troubleshooting**: Gives potential solutions to common errors.
- **License**: Mentions that the project is open-source and licensed under the MIT License.
- **Acknowledgements**: Credits the libraries and tools used in the app.
