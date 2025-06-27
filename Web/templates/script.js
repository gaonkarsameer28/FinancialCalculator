// script.js

    function calculateTimeToRetire() {
        // Retrieve input values
        const currentAge = parseInt(document.getElementById('currentAge').value);
        const retirementAge = parseInt(document.getElementById('retirementAge').value);

        // Calculate remaining time to retire
        const remainingYears = retirementAge - currentAge;

        // Display result
        const resultContainer = document.getElementById('result');
        resultContainer.innerHTML = `<h2>Remaining Time to Retire</h2>`;
        resultContainer.innerHTML += `<p>You have ${remainingYears} years remaining until your desired retirement age.</p>`;
    }

   function addLoanRow() {
    const loanTable = document.getElementById('loanTable').getElementsByTagName('tbody')[0];
    const newRow = loanTable.insertRow(-1);
    newRow.classList.add('loan-row');

    newRow.innerHTML = `
        <td><input type="text" class="loanType" required></td>
        <td><input type="number" class="loanEMI" required></td>
        <td><input type="number" class="loanLength" required></td>
        <td><input type="number" class="loanEMI" required></td>
        <td><span class="delete-btn" onclick="deleteRow(this)">&#10006;</span></td>`;
}

    function addInvestmentRow() {
        const loanTable = document.getElementById('InvestmentTable');
        const newRow = loanTable.insertRow(-1);
        newRow.classList.add('loan-row');
        newRow.innerHTML = `
            <td><input type="text" class="loanType" required></td>
            <td><input type="number" class="loanEMI" required></td>
            <td><input type="number" class="loanLength" required></td>
            <td><input type="number" class="loanEMI" required></td>
            <td><span class="delete-btn" onclick="deleteRow(this)">&#10006;</span></td>`;
    }

    function addFuturePlanRow() {
        const loanTable = document.getElementById('FuturePlans');
        const newRow = loanTable.insertRow(-1);
        newRow.classList.add('loan-row');
        newRow.innerHTML = `
            <td><input type="text" class="loanType" required></td>
            <td><input type="number" class="loanEMI" required></td>
            <td><input type="number" class="loanLength" required></td>
            <td><span class="delete-btn" onclick="deleteRow(this)">&#10006;</span></td>`;
    }

    function addInsuranceRow() {
        const loanTable = document.getElementById('tblInsurance');
        const newRow = loanTable.insertRow(-1);
        newRow.classList.add('loan-row');
        newRow.innerHTML = `
            <td><input type="text" class="loanType" required></td>
            <td><input type="number" class="loanEMI" required></td>
            <td><input type="number" class="loanLength" required></td>
            <td><input type="number" class="loanEMI" required></td>
            <td><span class="delete-btn" onclick="deleteRow(this)">&#10006;</span></td>`;
    }

    function deleteRow(btn) {
    const row = btn.closest('tr');
    row.remove();
}


    function calculateLoanDetails() {
        const loanDetailsResultContainer = document.getElementById('loanDetailsResult');
        loanDetailsResultContainer.innerHTML = ''; // Clear previous results

        const loanRows = document.querySelectorAll('.loan-row');
        loanDetailsResultContainer.innerHTML = '<h2>Loan Details</h2>';

        loanRows.forEach((row, index) => {
            const loanType = row.querySelector('.loanType').value;
            const loanEMI = parseFloat(row.querySelector('.loanEMI').value);
            const loanLength = parseInt(row.querySelector('.loanLength').value);

            let remainingLoan = loanEMI * 12 * loanLength;
            loanDetailsResultContainer.innerHTML += `<h3>${loanType} Loan Details</h3>`;
            loanDetailsResultContainer.innerHTML += '<table>';
            loanDetailsResultContainer.innerHTML += '<tr><th>Year</th><th>Loan Paid</th><th>Remaining Balance</th></tr>';

            for (let year = 1; year <= loanLength; year++) {
                const loanPaid = loanEMI * 12 * year;
                remainingLoan -= loanEMI * 12;
                loanDetailsResultContainer.innerHTML += `<tr><td>${year}</td><td>${loanPaid.toFixed(2)}</td><td>${remainingLoan.toFixed(2)}</td></tr>`;
            }

            loanDetailsResultContainer.innerHTML += '</table>';
var myTextbox = document.getElementById('myTextbox');

    // Set the text of the textbox
    myTextbox.value = loanDetailsResultContainer.innerHTML;

        });
    }

document.getElementById('exportBtn').addEventListener('click', function () {
    const element = document.getElementById('pdfcontent');

    html2pdf()
      .set({
        margin:       [10, 10],
        filename:     'report.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  {
          scale: 2,    // High DPI for quality
          scrollY: 0,  // Prevents vertical offset
          useCORS: true
        },
        jsPDF:        { unit: 'pt', format: 'a4', orientation: 'portrait' }
      })
      .from(element)
      .save();
  });