// purgecss.config.js
module.exports = {
    content: [
      './templates/**/*.html',
      './static/**/*.js',
    ],
    css: [
      './static/**/*.css',
    ],
    defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || [],
  }
  