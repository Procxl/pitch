{{left_sidebar_enabled,right_sidebar_enabled=False,('message' in globals())}}
{{extend 'layout.html'}}
{{if 'content' in globals():}}
{{=grid}}
{{else:}}
{{=BEAUTIFY(response._vars)}}
{{pass}}
