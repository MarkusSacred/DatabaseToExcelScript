# Automated Query from Database to CSV/TXT to Excel File

This script aims to create an automated report with the help of Python Script

Pre-requisite:
![SQL Server Developer](https://www.microsoft.com/en-us/sql-server/developer-tools)
![VS Studio Code SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads?msockid=255b760893ae6f862b47600292af6e07)
![SQL Command Utility](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility?view=sql-server-ver16&tabs=odbc%2Cwindows%2Cwindows-support&pivots=cs1-cmd#download-and-install)

Packages:
```
import pandas
from io import StringIO
```

---

# SQL Command Code:
```
sqlcmd -S YourServerName -d YourDatabase -E -Q "YourQuery" -o "/path" -s " " -W -h -1

-s - Server name
-d - Database name
-e - Windows authentication
-q - Your statement query
-o - Destination / Output path
-s - Separator Tab, comma, backslash etc.
-W - Remove Trailing Spaces
-h - Header (-h -1 hide header), (-h 1 print header every row)
```

---

# Process

**Step 1:** Now that we have your we have your query now, you can use with the file path of the SQL or the Query it self. 

## Your Query

```
sqlcmd -S YourServerName -d YourDatabase -E -Q "YourQuery" -o "/path" -s " " -W -h -1
```
## Your SQL

```
sqlcmd -S YourServerName -d YourDatabase -E -i "Your SQL file path" -o "/path" -s " " -W -h -1
```

**Step 2:**

You can run your script using the Task scheduler in your windows. 

![Create Task](/images/CreateBasicTask.png)
![Basic Task](/images/basicTask.png)
![Frequency](/images/frequency.png)
![Perform Task](/images/perform.png)
![Script Upload](/images/scriptUpload.png)
---

## ▶️ Usage

Run the project:

```bash
npm start
```

Example code usage:

```js
import { myFunction } from 'my-library';

myFunction();
```

---

## 📸 Screenshots

Here’s what it looks like:

![Screenshot](screenshot.png)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repo
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👤 Author

**Your Name**  
[GitHub](https://github.com/yourusername)  
[Email](mailto:your.email@example.com)

---

> Made with ❤️ by Your Name
