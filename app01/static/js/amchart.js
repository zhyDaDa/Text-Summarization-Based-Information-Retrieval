var root = am5.Root.new("chartdiv");

// Set themes
// https://www.amcharts.com/docs/v5/concepts/themes/
root.setThemes([
  am5themes_Animated.new(root)
]);


// Set up zooming
// https://www.amcharts.com/docs/v5/concepts/common-elements/containers/#Zoomable_container
var zoomableContainer = root.container.children.push(
  am5.ZoomableContainer.new(root, {
    width: am5.p100,
    height: am5.p100,
    pinchZoom: true
  })
);

var zoomTools = zoomableContainer.children.push(am5.ZoomTools.new(root, {
  target: zoomableContainer
}));


// Data
var data = {
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

// Create series
// https://www.amcharts.com/docs/v5/charts/hierarchy/#Adding
var series = zoomableContainer.contents.children.push(am5hierarchy.ForceDirected.new(root, {
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
}));

series.get("colors").setAll({
  step: 2
});


series.links.template.set("strength", 0.5);

series.labels.template.set("minScale", 0);

series.data.setAll([data]);

series.set("selectedDataItem", series.dataItems[0]);


// Make stuff animate on load
series.appear(1000, 100);