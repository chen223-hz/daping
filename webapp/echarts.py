#coding:utf-8

def target_url(target):
    url = ''
    if target == 'bar':
        url = "http://hiyoutest.doublecom.net/daping/getPhone/"
    elif target == 'area':
        url = "http://hiyoutest.doublecom.net/daping/getArea/"
    elif target == 'network':
        url = "http://hiyoutest.doublecom.net/daping/getNew/"
    elif target == 'network2':
        url = "http://hiyoutest.doublecom.net/daping/getSex/"
    elif target == 'tags':
        url = "http://hiyoutest.doublecom.net/daping/getVisitor/"
    elif target == 'num':
        url = "http://hiyoutest.doublecom.net/daping/getNum/"
    return url

def parse_echarts(target, body):
    if target == 'bar':
        data = {
            'tooltip': {
            'trigger': 'item',
            'formatter': "{a} <br/>{b}: {c} ({d}%)"
        },
        'color':['#a84f5c','#884750','#2c8acb','#1b9cc3','#7773c2','ffffff','#c23531','#1a3d75'],
        #   'color':['#04342d','#0b6154','#167f70','#44a295','#68baae','99d4cc','#34f4da','#8aefe1'],
        'series': [
            {
                'name':'访问来源',
                'type':'pie',
                'selectedMode': 'single',
                'radius': [0, '30%'],
                'center' : ['50%', '60%'],
                'label': {
                    'normal': {
                        'position': 'inner'
                    }
                },
                'labelLine': {
                    'normal': {
                        'show':'false'
                    }
                },
                'data':[
                    {'value':335, 'name':'其他', 'selected':'true'},
                    {'value':679, 'name':'ios'},
                    {'value':1548, 'name':'android'}
                ]
            },
            {
                'name':'访问来源',
                'type':'pie',
                'radius': ['40%', '60%'],
                'center' : ['50%', '60%'],
                'label': {
                    'normal': {
                        'rich': {
                            'a': {
                                'color': '#999',
                                'lineHeight': 22,
                                'align': 'center'
                            },
                            'hr': {
                                'borderColor': '#aaa',
                                'width': '100%',
                                'borderWidth': 0.5,
                                'height': 0
                            },
                            'b': {
                                'fontSize': 16,
                                'lineHeight': 33
                            },
                            'per': {
                                'color': '#eee',
                                'backgroundColor': '#334455',
                                'padding': [2, 4],
                                'borderRadius': 2
                            }
                        }
                    }
                },
                'data':[
                    {'value':body[0]['apple'], 'name':'苹果'},
                    {'value':body[0]['huawei'], 'name':'华为'},
                    {'value':body[0]['oppo'], 'name':'OPPO'},
                    {'value':body[0]['samsung'], 'name':'三星'},
                    {'value':body[0]['vivo'], 'name':'VIVO'},
                    {'value':body[0]['other'], 'name':'其他'}
                ]
            }
        ]
            }
    if target == 'area':
        data = {}
        data['data'] = body
    if target == 'network':
        data = {
        'tooltip': {
              'trigger': 'item',
              'formatter': "{a} <br/>{b}: {c} ({d}%)"
          },
          'series': [
              {
                  'name':'访问来源',
                  'type':'pie',
                  'selectedMode': 'single',
                  'radius': [0, '30%'],
                  'center' : ['50%', '55%'],
                  'label': {
                      'normal': {
                          'position': 'inner'
                      }
                  },
                  'labelLine': {
                      'normal': {
                          'show': 'false'
                      }
                  },
                  'data':[
                      {'value':679, 'name':'男游客'},
                      {'value':1548, 'name':'女游客'}
                  ],
                  'color':['#3daafc','#207dde']
                  #color:['#167f70','#44a295']
              },
              {
                  'name':'访问来源',
                  'type':'pie',
                  'radius': ['40%', '60%'],
                  'center' : ['50%', '55%'],
                  'label': {
                      'normal': {
                         
                          'rich': {
                              'a': {
                                  'color': '#999',
                                  'lineHeight': 22,
                                  'align': 'center'
                              },
                              'hr': {
                                  'borderColor': '#aaa',
                                  'width': '100%',
                                  'borderWidth': 0.5,
                                  'height': 0
                              },
                              'b': {
                                  'fontSize': 16,
                                  'lineHeight': 33
                              },
                              'per': {
                                  'color': '#eee',
                                  'backgroundColor': '#334455',
                                  'padding': [2, 4],
                                  'borderRadius': 2
                              }
                          }
                      }
                  },
                  'data':[
                      {'value':body['new'], 'name':'新游客'},
                      {'value':body['old'], 'name':'老游客'}
                  ],
                  'color':['#fff','#207dde']
                  #color:['#fff','#167f70']
                  }
          ]
        }
    if target == 'network2':
        data = {
          # 'title': {
          #     'text': '游客性别占比',
          #     'left':'center',
          #     'top':'15%',
          #     'textStyle':{
          #             'fontWeight':'normal',
          #             'color':'#fff'
          #     }
          # },
          # 'tooltip' : {
          # 'trigger': 'item',
          # 'formatter': "{a} <br/>{b} : {c} ({d}%)"
          # },
          # # 'color':['#c23531','#ffffff'],
          # 'color':['#167f70','#ffffff'],

          # 'calculable' : 'true',
          # 'series' : [
          # {
          #         'name':'面积模式',
          #         'type':'pie',
          #         'radius' : ['45%', '65%'],
          #         'center' : ['50%', '65%'],
          #         'roseType' : 'area',
          #         'data':[
          #             {'value':body['woman'], 'name':'女游客'},
          #             {'value':body['man'], 'name':'男游客'}
          #         ]
          #     }
          # ]
          
    }
    if target == 'tags':
        date = []
        num = []
        for obj in body:
            date.append(obj['date'])
            num.append(obj['num'])
        data = {
        'tooltip' : {
              'trigger': 'axis',
              'axisPointer': {
                  'type': 'cross',
                  'label': {
                      'backgroundColor': '#207dde'
                  }
              }
          },
          'grid': {
              'left': '5%',
              'right': '8%',
              'top':'13%',
              'bottom':'2%',
              'containLabel': 'true'
          },
          'xAxis' : [
              {
                  'type' : 'category',
                  'boundaryGap' : 'false',
                  'axisLine':{
                      'lineStyle':{
                          'color':'#fff'
                      }
                  },
                  'data' : date
              }
          ],
          'yAxis' : [
              {
                  'type' : 'value',
                  'axisLine':{
                      'lineStyle':{
                          'color':'#fff'
                      }
                  }
              }
          ],
          'series' : [
              {
                  'type':'line',
                  'stack': '总量',
                  'areaStyle': {'normal': {
                      'color':'#207dde'
                      #color:'#167f70'
                  }},
                  'itemStyle' : {  
                              'normal' : {  
                                  'lineStyle':{  
                                      'color':'#1a73d0'
                                       #color:'#167f70'  
                                  }  
                              }  
                          }, 
                  'data':num
              },
          ],
          'items':[]
        }
    if target == 'num':
      data = body

    return data
