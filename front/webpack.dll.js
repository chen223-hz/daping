const webpack = require('webpack');

const vendors = [
  'vue',
  'vue-router',
  'vue-echarts-v3',
  'vue-baidu-map'
];

module.exports = {
  output: {
    path: '../webapp/static/',
    filename: '[name].[chunkhash].js',
    library: '[name]_[chunkhash]',
  },
  entry: {
    vendor: vendors,
  },
  plugins: [
    new webpack.DllPlugin({
      path: 'manifest.json',
      name: '[name]_[chunkhash]',
      context: __dirname,
    }),
    new webpack.DefinePlugin({
        'process.env': {
            NODE_ENV: '"production"'
        }
    }),
    new webpack.optimize.UglifyJsPlugin({ //压缩代码
        compress: {
            warnings: false
        }
    }),
  ],
}
