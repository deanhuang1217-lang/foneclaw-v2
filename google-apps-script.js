// ============================================
// FoneClaw Early Access Form - Google Apps Script
// ============================================
// 部署步骤：
// 1. 打开 https://sheets.google.com ，新建一个空白表格
// 2. 点击 扩展程序 → Apps Script
// 3. 删除默认代码，粘贴下面的代码
// 4. 点击 保存（💾图标）
// 5. 点击 部署 → 新建部署 → 类型选"网页应用"
//    - 执行身份：我
//    - 谁可以访问：任何人
// 6. 点击"部署"，复制生成的网址
// 7. 把网址填到 early-access.html 的 FORM_ENDPOINT 变量里
// ============================================

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);

    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

    // 如果表头不存在，先写入表头
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(['Timestamp', 'Name', 'Email', 'Social Media', 'Source']);
    }

    // 写入数据
    sheet.appendRow([
      new Date().toISOString(),
      data.name || '',
      data.email || '',
      data.social || '',
      data._source || 'early-access.html'
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ success: true }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ success: false, error: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// 测试用：在浏览器打开部署网址时显示提示
function doGet(e) {
  return ContentService
    .createTextOutput('FoneClaw form endpoint is running. Use POST to submit data.')
    .setMimeType(ContentService.MimeType.TEXT);
}
