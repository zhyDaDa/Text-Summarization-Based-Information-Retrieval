$(function () {
  var data = {};
  var myChart = null;
  $('.searchbox').submit(function (e) {
    e.preventDefault()
    var searchTerm = $('input[name = "neo4jSearch"]').val();
    $.ajax({
      url: '/neo4j/', // The URL to send the POST request to
      type: 'POST',
      data: { neo4jSearch: searchTerm }, // Data to send
      success: function (response) {
        // 假设 response 是一个包含多个对象的数组，每个对象都有 nodes 和 edges
        var data = response.map(function (item) {
          // 直接返回新的结构
          return buildGraph(item);
        });
        data = { value: 0, children: data }
        data = {
          value: 0,
          children: [
            // 症状
            {
              name: "症状",
              children: [
                {
                  name: "结节",
                  link: ["堪萨斯分枝杆菌感染", "结节性脆发病", "结节性筋膜炎"],
                  value: 1
                },
                {
                  name: "肉芽肿",
                  link: ["堪萨斯分枝杆菌感染"],
                  value: 1
                },
                {
                  name: "鳞屑",
                  link: ["结节性脆发病"],
                  value: 1
                },
                {
                  name: "低分子蛋白尿",
                  link: ["结节性脆发病"],
                  value: 1
                },
                {
                  name: "肝脾肿大",
                  link: ["结节病"],
                  value: 1
                },
                {
                  name: "呼吸困难",
                  link: ["结节病"],
                  value: 1
                },
                {
                  name: "肝肿大",
                  link: ["结节病"],
                  value: 1
                },
                {
                  name: "眼部烧伤感",
                  link: ["白内障"],
                  value: 1
                },
                {
                  name: "先天性无虹膜",
                  link: ["白内障"],
                  value: 1
                },
                {
                  name: "视力常呈雾状模糊感",
                  link: ["白内障"],
                  value: 1
                },
                {
                  name: "虹膜异色",
                  link: ["小儿颈交感神经麻痹综合征"],
                  value: 1
                },
                {
                  name: "眼球内陷",
                  link: ["小儿颈交感神经麻痹综合征"],
                  value: 1
                },
                {
                  name: "眼睑下垂",
                  link: ["小儿颈交感神经麻痹综合征"],
                  value: 1
                },
                {
                  name: "视力障碍",
                  link: ["风湿性疾病"],
                  value: 1
                },
                {
                  name: "胃肠道出血",
                  link: ["风湿性疾病"],
                  value: 1
                },
                {
                  name: "眼干",
                  link: ["风湿性疾病"],
                  value: 1
                },
              ]

            },
            //疾病
            {
              name: "堪萨斯分枝杆菌感染",
              children: [
                {
                  name: "血液科",
                  value: 1
                },
                {
                  name: "血液分析仪检查",
                  value: 1
                },

                {
                  name: "血液检查",
                  value: 1
                },
              ]
            },
            {
              name: "结节性脆发病",
              link: ["结节病"],
              children: [
                {
                  name: "血常规",
                  value: 1
                },
                {
                  name: "	尿常规",
                  value: 1
                },
                {
                  name: "	皮肤涂片显微镜检查",
                  value: 1
                },
                {
                  name: "皮肤科",
                  value: 1
                }
              ]
            },
            {
              name: "结节病",
              link: ["妊娠合并白血病", "	白内障", "恶性蓝痣",],
              children: [
                {
                  name: "血常规",
                  value: 1
                },
                {
                  name: "CT检查",
                  value: 1
                },
                {
                  name: "体层摄影",
                  value: 1
                },
                {
                  name: "肌电图",
                  value: 1
                },
                {
                  name: "皮内试验",
                  value: 1
                },
              ]
            },
            {
              name: "结节性筋膜炎",
              children: [
                {
                  name: "皮肤科",
                  value: 1
                },
                {
                  name: "皮肤涂片显微镜检查",
                  value: 1
                },
              ]
            },
            {
              name: "白内障",
              link: ["小儿颈交感神经麻痹综合征", "风湿性疾病", "内分泌性高血压"],
              children: [
                {
                  name: "眼底检查",
                  value: 1
                },
                {
                  name: "眼科",
                  value: 1
                },
                {
                  name: "视力",
                  value: 1
                },
              ]
            },
            {
              name: "妊娠合并白血病",
              children: [
                {
                  name: "白细胞数",
                  value: 1
                },
                {
                  name: "肾功能检查",
                  value: 1
                },
                {
                  name: "	醋酸AS-D茶酚脂酶染色",
                  value: 1
                },
                {
                  name: "有核红细胞",
                  value: 1
                },
                {
                  name: "核磁共振成像(MRI)",
                  value: 1
                },
                {
                  name: "产科",
                  value: 1
                },
              ]
            },
            {
              name: "恶性蓝痣",
              link: ["结节病", "结节"],
              children: [
                {
                  name: "	皮肤科",
                  value: 1
                },
                {
                  name: "	血常规",
                  value: 1
                },
                {
                  name: "免疫病理检查",
                  value: 1
                },
                {
                  name: "皮损",
                  value: 1
                },
                {
                  name: "细胞组织化学染色",
                  value: 1
                },
              ]
            },
            {
              name: "小儿颈交感神经麻痹综合征",
              link: ["白内障"],
              children: [
                {
                  name: "儿科综合",
                  value: 1
                },
                {
                  name: "脑电图检查",
                  value: 1
                },
                {
                  name: "CT检查",
                  value: 1
                },
                {
                  name: "心电图",
                  value: 1
                },
                {
                  name: "血常规",
                  value: 1
                },
              ]
            },
            {
              name: "风湿性疾病",
              link: ["白内障"],
              children: [
                {
                  name: "风湿免疫科",
                  value: 1
                },
                {
                  name: "免疫学检测",
                  value: 1
                },
                {
                  name: "血常规",
                  value: 1
                },
                {
                  name: "血沉方程K值",
                  value: 1
                },
                {
                  name: "类风湿因子",
                  value: 1
                },
              ]
            },
            {
              name: "内分泌性高血压",
              link: ["白内障"],
              children: [
                {
                  name: "尿17-羟皮质类固醇",
                  value: 1
                },
                {
                  name: "促肾上腺皮质激素（ACTH）",
                  value: 1
                },
                {
                  name: "	血液电解质检查",
                  value: 1
                },
                {
                  name: "血液生化六项检查",
                  value: 1
                },
                {
                  name: "血浆醛固酮",
                  value: 1
                },
              ]
            },
          ]
        };

        console.log(data);
        data = JSON.stringify(data);
        updateGraph(data);  // 更新图表的函数调用，假设它接受整理好的数据
        console.log(data);
        //$('#results').html(JSON.stringify(data)); // 如果你想在页面上显示结果
      },
      // error: function (xhr, status, error) {
      //   // Handle errors here
      //   console.log("Error: " + error);
      //   $('#results').html("Failed to retrieve results.");
      // }
    });
  })
  function buildGraph(response) {
    var nodes = response.data.nodes;
    //console.log(nodes);
    var edges = response.data.edges;
    //console.log(edges);
    //let nodeName = nodes.map(node => node.name);
    let disease_name = nodes.filter(node => node.data.label === 'Disease')[0].data.name;
    nodes = nodes.filter(node => node.data.label !== 'Disease');
    let disease = {
      name: disease_name,
      children: nodes.map(disease => ({
        name: disease.data.name,
        value: 1
      }))
    }

    //console.log(nodes);
    let results = {
      // value: 0,
      children: [],
      link: nodes.map(node => node.data.name),
      name: ""
    };

    results.children = (disease.children);
    results.name = disease.name;
    return results;
  }

  function initializeGraph() {
    var root = am5.Root.new("neo4jAmchart");
    root.setThemes([am5themes_Animated.new(root)]);

    var zoomableContainer = root.container.children.push(
      am5.ZoomableContainer.new(root, {
        width: am5.p100,
        height: am5.p100,
        pinchZoom: true
      })
    );

    myChart = zoomableContainer.contents.children.push(
      am5hierarchy.ForceDirected.new(root, {
        singleBranchOnly: false,
        downDepth: 2,
        topDepth: 1,
        initialDepth: 1,
        valueField: "value",
        categoryField: "name",
        childDataField: "children",
        idField: "name",
        linkWithField: "link",
        manyBodyStrength: -10,
        centerStrength: 0.8
      })
    );

    myChart.get("colors").setAll({ step: 2 });
    myChart.links.template.set("strength", 0.5);
    myChart.labels.template.set("minScale", 0);
  }

  function updateGraph(data) {
    if (!myChart) {
      initializeGraph(); // 如果图表未初始化，先初始化
    }

    // 更新数据
    myChart.data.setAll(data);
    myChart.set("selectedDataItem", myChart.dataItems[0]);

    // 动画
    myChart.appear(1000, 100);
  }



  // Data



  // Create series
  // https://www.amcharts.com/docs/v5/charts/hierarchy/#Adding

})