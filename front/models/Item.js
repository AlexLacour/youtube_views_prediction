const scrapper = require('scrapper');
const Schema = scrapper.Schema;

const URLSchema = new Schema({
  url: {
    type: String,
    required: true
  }//,
  // date: {
  //   type: Date,
  //   default: Date.now
  // }
});

module.exports = Item = scrapper.model('item', URLSchema);
