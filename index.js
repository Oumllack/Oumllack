const { promises: fs } = require('fs');
const readme = require('./readme');

const msInOneDay = 1000 * 60 * 60 * 24;
const today = new Date();

function generateNewREADME() {
  const readmeRow = readme.split('\n');

  function updateIdentifier(identifier, replaceText) {
    const identifierIndex = findIdentifierIndex(readmeRow, identifier);
    if (!readmeRow[identifierIndex]) return;
    readmeRow[identifierIndex] = readmeRow[identifierIndex].replace(
      `<#${identifier}>`,
      replaceText
    );
  }

  const identifierToUpdate = {
    day_before_new_years: getDBNWSentence(),
    today_date: getTodayDate(),
    bot_signing: getBotSigning(),
  };

  Object.entries(identifierToUpdate).forEach(([key, value]) => {
    updateIdentifier(key, value);
  });

  return readmeRow.join('\n');
}

const moodByDay = {
  1: 'passion',
  2: 'determination',
  3: 'creativity',
  4: 'innovation',
  5: 'excellence',
  6: 'expertise',
  7: 'excellence',
};

function getBotSigning() {
  const mood = moodByDay[today.getDay() + 1];
  return `🤖 This README is updated with ${mood}, by Oumllack ❤️`;
}

function getTodayDate() {
  return today.toDateString();
}

function getDBNWSentence() {
  const nextYear = today.getFullYear() + 1;
  const nextYearDate = new Date(String(nextYear));

  const timeUntilNewYear = nextYearDate.getTime() - today.getTime();
  const dayUntilNewYear = Math.round(timeUntilNewYear / msInOneDay);

  return `**${dayUntilNewYear} days before ${nextYear} ⏱**`;
}

const findIdentifierIndex = (rows, identifier) =>
  rows.findIndex((r) => Boolean(r.match(new RegExp(`<#${identifier}>`, 'i'))));

const updateREADMEFile = (text) => fs.writeFile('./README.md', text);

function main() {
  const newREADME = generateNewREADME();
  console.log(newREADME);
  updateREADMEFile(newREADME);
}
main(); 