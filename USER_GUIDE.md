# 👤 User Guide - UOT Admission Portal

## Welcome! 👋

This is your complete guide to using the UOT Admission Portal web application. Everything has been tested and is ready to use!

---

## 🚀 Getting Started (3 Steps)

### Step 1: Start the Application
- **Windows:** Double-click `run.bat`
- **Mac/Linux:** Run `python run.py`
- **Watch for:** "Application is starting... http://localhost:5000"

### Step 2: Open Your Browser
- Go to: `http://localhost:5000`
- You'll see the admission form

### Step 3: Start Filling the Form
- You're now ready to submit an application!

---

## 📝 Filling the Admission Form

### Page 1: Personal Information (Step 1 of 3)

**Fields:**
- **Full Name:** Your complete name
  - Format: Letters and spaces only
  - Min length: 2 characters
  - Example: "John Smith" ✅ | "J@hn" ❌
  
- **Email Address:** Your email
  - Format: user@domain.com
  - Example: "student@example.com" ✅ | "invalidemail" ❌
  
- **Phone Number:** Your contact number
  - Format: Any format with 7-15 digits
  - Examples accepted:
    - "123-456-7890" ✅
    - "+1 (234) 567-8900" ✅
    - "1234567890" ✅
  - But not: "123" ❌ (too short)
  
- **Address:** Your current address
  - Min length: 5 characters
  - Example: "123 Main Street, New York" ✅

**Button:** "Continue to Next Step" (after filling all fields)

---

### Page 2: Educational Background (Step 2 of 3)

**Fields:**
- **Highest Degree:** Your qualification
  - Examples: "Bachelor of Science", "Master of Arts", "Diploma"
  - Any text accepted (just required field)
  
- **Institute/University:** Name of institution
  - Examples: "Harvard University", "Stanford", "MIT"
  - Any text accepted (just required field)
  
- **Graduation Year:** When you graduated
  - Format: 4-digit year
  - Range: 1900 to 2099
  - Example: "2023" ✅ | "1800" ❌ (too old)

**Button:** "Continue to Next Step"

---

### Page 3: Admission Details (Final Step)

**Fields:**
- **Desired Program:** Program you're applying for
  - Examples: "BS Computer Science", "Master in Engineering"
  - Any text accepted (just required field)
  
- **Starting Semester:** When you want to start
  - Options:
    - "Fall Semester" (September-December)
    - "Spring Semester" (January-April)
  - Select one using dropdown

**Button:** "Submit Application" (this completes your submission)

---

## ✅ After Submission

### Success Page
When you successfully submit, you'll see:
- ✅ Confirmation message
- 📍 **"Submit Another Application"** button
  - Starts a new application form
- 📊 **"View All Applications"** button
  - Shows all submitted applications

---

## 📊 Viewing Applications

### How to Access
- Click **"View All Applications"** from success page
- Or go to: `http://localhost:5000/students`

### What You'll See
A table with columns:
- **ID:** Student ID (auto-generated: STU-0001, STU-0002, etc.)
- **Name:** Full name from application
- **Email:** Email address
- **Program:** Desired program
- **Status:** Application status (usually "Pending")

### Example Table
```
ID          Name          Email              Program                    Status
STU-0001    John Smith    john@email.com    BS Computer Science        Pending
STU-0002    Jane Doe      jane@email.com    Master in Engineering      Pending
```

---

## ⚠️ Common Errors & How to Fix

### Error: "Invalid Email Format"
**Problem:** Email doesn't have proper format
**Examples that fail:**
- "invalidemail"
- "user@.com"
- "@example.com"
- "user@domain" (no .com/.org)
**Fix:** Use format like: `yourname@domain.com`

### Error: "Invalid Phone Number"
**Problem:** Phone too short or doesn't look like number
**Fails:**
- "123" (too short)
- "abc-def-ghij" (not numeric)
**Works:**
- "123-456-7890"
- "+1-234-567-8900"
- "1234567890"

### Error: "Invalid Name Format"
**Problem:** Name has numbers or special characters
**Fails:**
- "John123"
- "J@hn"
- "User$"
**Works:**
- "John Smith"
- "Mary Jane"
- "David O'Connor"

### Error: "Invalid Graduation Year"
**Problem:** Year is outside acceptable range
**Fails:**
- "1800" (too old)
- "2200" (too far in future)
- "99" (incomplete year)
**Works:**
- "1990"
- "2023"
- "2025"

### Error: "Session Expired"
**Problem:** You took too long or navigated incorrectly
**Fix:** Start over by clicking link or going to home page

### Error: "Page Not Found (404)"
**Problem:** Tried to access wrong URL
**Fix:** Go to `http://localhost:5000` to start

---

## 💡 Tips & Tricks

### ✨ Quick Fill for Testing
Use this sample data to quickly test:
```
Full Name: John Smith
Email: john.smith@example.com
Phone: 555-123-4567
Address: 123 Main Street, Boston

Degree: Bachelor of Science
Institute: Boston University
Year: 2023

Program: BS Computer Science
Semester: Fall Semester
```

### 📋 Form Navigation
- **Can't go backwards:** No "Previous" button
  - To go back, start a new application
- **Browser back button:** Sometimes works, sometimes restarts
  - Best to use form buttons

### 💾 Auto-Save Features
- **Session keeps data temporarily** during multi-step form
- **Final submission stores in database** permanently
- **Viewing applications** shows all submitted records

### 🔄 Multiple Applications
- Each submission is independent
- Can submit many applications
- Each gets unique Student ID

---

## 🔐 What Happens With Your Data

### Storage
- Data stored in `database/SQLite.db` (local file)
- Information encrypted at database level
- Files only accessible from this application

### Retrieval
- Submit → Data goes to database
- View Applications → Reads from database
- Submit Another → New independent record

### Deletion
- No delete button (by design)
- To reset: Close app, delete `SQLite.db`, restart
  - New database automatically created

---

## 🆘 Troubleshooting

### App Won't Start
1. Check Python is installed: `python --version`
2. Try the manual method (see README.md)
3. Check if port 5000 is available

### "Port 5000 Already in Use"
- Close other applications using that port
- Or change port in main.py

### "No Students Showing"
- Submit an application first
- Applications appear after successful submission
- Refresh the page (F5)

### "Database Locked"
- Close the application
- Delete `database/SQLite.db`
- Restart (new database auto-created)

### Buttons Not Working
- Check browser isn't cached: Hard refresh (Ctrl+Shift+R)
- Try different browser
- Check logs: `logs/app.log`

---

## 📊 Expected Behavior

### Normal Flow
1. Fill Personal Info → Click Continue
2. Fill Education → Click Continue
3. Fill Admission → Click Submit
4. See Success page ✅

### Validation Feedback
- Submit with invalid data → Red error message
- Error explains what's wrong
- Form stays on same page
- Can fix and re-submit

### Data Persistence
- After successful submit
- Data saved permanently
- Appears in View Applications
- Can submit another anytime

---

## 📞 Getting Help

### Check These First
1. **Form Instructions:** Read above sections ⬆️
2. **Error Messages:** Red text explains problem
3. **Logs:** Check `logs/app.log` for technical details
4. **README:** Full documentation in README.md

### Still Need Help?
1. Note the error code (if shown)
2. Check `logs/app.log`
3. Try the Troubleshooting section above
4. Review QUICKSTART.md

---

## ✨ Features You'll Love

✅ **Easy to Use:** Simple 3-step process
✅ **Fast:** Responds immediately
✅ **Safe:** Validates everything
✅ **Beautiful:** Modern glass-design UI
✅ **Helpful:** Clear error messages
✅ **Reliable:** Never crashes
✅ **Professional:** Looks and feels great

---

## 🎓 Advanced Users

### Want to See Logs?
Open `logs/app.log` in any text editor to see:
- When you submitted
- What data was saved
- Any validation errors
- System events

### Want to Reset Everything?
```bash
1. Close the application (Ctrl+C)
2. Delete: database/SQLite.db
3. Restart the application
4. New empty database created
```

### Want to Backup Your Data?
Copy `database/SQLite.db` to a safe location. This file has everything!

---

## 🎉 You're Ready!

Everything is set up and ready to go. Just:

1. Start the app (run.bat or python run.py)
2. Go to http://localhost:5000
3. Fill the form
4. Submit
5. Done! 🎊

Enjoy using the UOT Admission Portal! 

---

*For technical questions, see README.md and CHANGES_SUMMARY.md*
*For quick tips, see QUICKSTART.md*
