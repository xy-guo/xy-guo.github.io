import jinja2
from dataclasses import dataclass
from typing import List
import os
import shutil

title = 'Xiaoyang Guo'
name = 'Xiaoyang Guo'

author_links = {
    "Xiaoyang Guo": "https://xy-guo.github.io/",
    "Yubin Hu": "https://scholar.google.com/citations?user=swN2J1QAAAAJ&hl=en",
    "Shaoshuai Shi": "https://shishaoshuai.com/",
    "Hongsheng Li": "https://www.ee.cuhk.edu.hk/~hsli/",
    "Xiaogang Wang": "https://www.ee.cuhk.edu.hk/~xgwang/",
    "Kai Yang": "https://scholar.google.com/citations?user=s5Z6X0cAAAAJ&hl=en",
    "Hongyang Li": "https://lihongyang.info/",
    "Bo Dai": "https://daibo.info/",
    "Wanli Ouyang": "https://wlouyang.github.io/",
    "Shuai Yi": "https://scholar.google.com/citations?user=afbbNmwAAAAJ&hl=zh-CN",
    "Jimmy Ren": "http://www.jimmyren.com/",
    "Jingwei Huang": "https://stanford.edu/~jingweih/",
    "Yong-Jin Liu": "https://cg.cs.tsinghua.edu.cn/people/~Yongjin/Yongjin.htm",
    "Hengshuang Zhao": "https://i.cs.hku.hk/~hszhao/",
    "Lihe Yang": "https://liheyoung.github.io/",
    "Xingang Pan": "https://xingangpan.github.io/",
    "Wei Yin": "https://yvanyin.xyz/",
    "Li Yi": "https://ericyi.github.io/",
    "Zheng Zhang": "https://zhengzhang01.github.io/",
    "Kaiwen Zhang": "https://kevin-thu.github.io/homepage/",
    "Yuan Liu": "https://liuyuan-pal.github.io/",
    "Xiaoxiao Long": "https://www.xxlong.site/",
    "Xiao-Xiao Long": "https://www.xxlong.site/",
    "Xinggang Wang": "https://xwcv.github.io/",
    "Bencheng Liao": "https://scholar.google.com/citations?user=rUBdh_sAAAAJ&hl=zh-CN",
    "Shaoyu Chen": "https://scholar.google.com/citations?user=PIeNN2gAAAAJ&hl=en",
    "Songyou Peng": "https://pengsongyou.github.io/",
    "Sida Peng": "https://pengsida.net/",
    "Xiaowei Zhou": "https://xzhou.me/",
    "Ping Tan": "https://facultyprofiles.hkust.edu.hk/profiles.php?profile=ping-tan-pingtan",
    "Chi-Wing Fu": "https://www.cse.cuhk.edu.hk/~cwfu/",
    "Pheng-Ann Heng": "https://www.cse.cuhk.edu.hk/~pheng/",
    "Yao Yao": "https://yanyt.github.io/",
    "Xun Cao": "https://cite.nju.edu.cn/People/Full_time_Faculty/20190621/i5054.html",
    "Hao Gao": "https://hgao-cv.github.io/",
    "Yifan Zhan": "https://yifever20002.github.io/",
    "Yinqiang Zheng": "https://scholar.google.com/citations?user=qMrRe2wAAAAJ",
    "Hao Wang": "https://scholar.google.com/citations?user=pVWBU7YAAAAJ",
}


@dataclass
class Author:
    name: str
    url: str


@dataclass
class Paper:
    tag: str
    title: str
    short_title: str
    conference: str
    conference_short: str
    year: int
    authors: List[Author]
    url: str
    url_arxiv: str
    url_project_page: str = None
    url_paper: str = None
    url_supp: str = None
    url_video: str = None
    url_poster: str = None
    url_code: str = None
    url_dataset: str = None
    description: str = None
    image: str = None
    image_after: str = None
    video_after: str = None
    special_honor: str = None
    yellow_highlight: bool = False
    abstract: str = None
    affiliation: str = None
    bib: str = None

@dataclass
class Experience:
    title: str
    description: str



def gen_author_list(*author_names):
    if len(author_names) == 1 and ',' in author_names[0]:
        author_names = author_names[0].split(',')
    author_names = [name.strip() for name in author_names]
    authors = []
    for author_name in author_names:
        url = None
        for name, link in author_links.items():
            if author_name.startswith(name):
                url = link
                break
        if author_name[-1] in ["†", "‡", "*"]:
            author_name = author_name[:-1] + f"<sup>{author_name[-1]}</sup>"
        authors.append(Author(
            name=author_name,
            url=url
        ))
    return authors


def get_papers():
    papers = []
    papers.append(Paper(
        tag="scope",
        title="SCOPE: Scale-Consistent One-Pass Estimation of 3D Geometry",
        short_title="SCOPE",
        conference="Preprint",
        conference_short="Arxiv'26",
        year=2026,
        authors=gen_author_list("Zheng Zhang, Lihe Yang, Tianyu Yang, Chaohui Yu, Yixing Lao, Xiaoyang Guo, Biao Gong, Fan Wang, Hengshuang Zhao"),
        url="https://arxiv.org/abs/2606.21300",
        url_arxiv="https://arxiv.org/abs/2606.21300",
        image="./images/scope.png",
    ))
    papers.append(Paper(
        tag="eps3d",
        title="EPS3D: End-to-End Feed-Forward 3D Panoptic Segmentation",
        short_title="EPS3D",
        conference="International Conference on Machine Learning",
        conference_short="ICML'26",
        year=2026,
        authors=gen_author_list("Runsong Zhu, Jiaxin Guo, Xiaoyang Guo†, Zhengzhe Liu, Ka-Hei Hui, Wei Yin, Kai Chen, Wei Chen, Weiqiang Ren, Yunhui Liu, Pheng-Ann Heng, Chi-Wing Fu"),
        url="https://arxiv.org/abs/2606.08980",
        url_arxiv="https://arxiv.org/abs/2606.08980",
        url_code="https://github.com/Runsong123/EPS3D",
        image="./images/eps3d.png",
    ))
    papers.append(Paper(
        tag="horizonstream",
        title="HorizonStream: Long-Horizon Attention for Streaming 3D Reconstruction",
        short_title="HorizonStream",
        conference="Preprint",
        conference_short="Arxiv'26",
        year=2026,
        authors=gen_author_list("Chong Cheng, Peilin Tao, Nanjie Yao, Guanzhi Ding, Xianda Chen, Yuansen Du, Xiaoyang Guo, Wei Yin, Weiqiang Ren, Qian Zhang, Zhengqing Chen, Hao Wang"),
        url="https://arxiv.org/abs/2605.23889",
        url_arxiv="https://arxiv.org/abs/2605.23889",
        image="./images/horizonstream.png",
    ))
    papers.append(Paper(
        tag="horizondrive",
        title="HorizonDrive: Self-Corrective Autoregressive World Model for Long-horizon Driving Simulation",
        short_title="HorizonDrive",
        conference="Preprint",
        conference_short="Arxiv'26",
        year=2026,
        authors=gen_author_list("Conglang Zhang, Yifan Zhan, Qingjie Wang, Zhanpeng Ouyang, Yu Li, Zihao Yang, Xiaoyang Guo, Weiqiang Ren, Qian Zhang, Zhen Dong, Yinqiang Zheng, Wei Yin, Zhengqing Chen"),
        url="https://arxiv.org/abs/2605.11596",
        url_arxiv="https://arxiv.org/abs/2605.11596",
        image="./images/horizondrive.png",
    ))
    papers.append(Paper(
        tag="composia",
        title="Composing Driving Worlds through Disentangled Control for Adversarial Scenario Generation",
        short_title="CompoSIA",
        conference="European Conference on Computer Vision",
        conference_short="ECCV'26",
        year=2026,
        authors=gen_author_list("Yifan Zhan, Zhengqing Chen, Qingjie Wang, Zhuo He, Muyao Niu, Xiaoyang Guo, Wei Yin, Weiqiang Ren, Qian Zhang, Yinqiang Zheng"),
        url="https://arxiv.org/abs/2603.12864",
        url_arxiv="https://arxiv.org/abs/2603.12864",
        url_project_page="https://yifever20002.github.io/CompoSIA/",
        url_code="https://github.com/Yifever20002/CompoSIA",
        image="./images/composia.png",
    ))
    papers.append(Paper(
        tag="scal3r",
        title="Scal3R: Scalable Test-Time Training for Large-Scale 3D Reconstruction",
        short_title="Scal3R",
        conference="Conference on Computer Vision and Pattern Recognition",
        conference_short="CVPR'26",
        year=2026,
        authors=gen_author_list("Tao Xie, Peishan Yang, Yudong Jin, Yingfeng Cai, Wei Yin, Weiqiang Ren, Qian Zhang, Wei Hua, Sida Peng, Xiaoyang Guo†, Xiaowei Zhou†"),
        url="https://arxiv.org/abs/2604.08542",
        url_arxiv="https://arxiv.org/abs/2604.08542",
        url_project_page="https://zju3dv.github.io/scal3r/",
        url_code="https://github.com/zju3dv/Scal3R",
        image="./images/scal3r.png",
        special_honor="Highlight",
    ))
    papers.append(Paper(
        tag="longstream",
        title="LongStream: Long-Sequence Streaming Autoregressive Visual Geometry",
        short_title="LongStream",
        conference="Conference on Computer Vision and Pattern Recognition",
        conference_short="CVPR'26",
        year=2026,
        authors=gen_author_list("Chong Cheng, Xianda Chen, Tao Xie, Wei Yin, Weiqiang Ren, Qian Zhang, Xiaoyang Guo†, Hao Wang"),
        url="https://arxiv.org/abs/2602.13172",
        url_arxiv="https://arxiv.org/abs/2602.13172",
        url_project_page="https://3dagentworld.github.io/longstream/",
        image="./images/longstream.png",
    ))
    papers.append(Paper(
        tag="litevggt",
        title="LiteVGGT: Boosting Vanilla VGGT via Geometry-Aware Cached Token Merging",
        short_title="LiteVGGT",
        conference="Conference on Computer Vision and Pattern Recognition",
        conference_short="CVPR'26",
        year=2026,
        authors=gen_author_list("Zhijian Shu, Cheng Lin, Tao Xie, Wei Yin, Ben Li, Zhiyuan Pu, Weize Li, Yao Yao, Xun Cao, Xiaoyang Guo, Xiao-Xiao Long"),
        url="https://arxiv.org/abs/2512.04939",
        url_arxiv="https://arxiv.org/abs/2512.04939",
        url_project_page="https://garlicba.github.io/LiteVGGT/",
        image="./images/litevggt.png",
    ))
    papers.append(Paper(
        tag="vggt4d",
        title="VGGT4D: Mining Motion Cues in Visual Geometry Transformers for 4D Scene Reconstruction",
        short_title="VGGT4D",
        conference="Conference on Computer Vision and Pattern Recognition",
        conference_short="CVPR'26",
        year=2026,
        authors=gen_author_list("Yu Hu*, Chong Cheng*, Sicheng Yu*, Xiaoyang Guo, Hao Wang"),
        url="https://arxiv.org/abs/2511.19971",
        url_arxiv="https://arxiv.org/abs/2511.19971",
        url_project_page="https://3dagentworld.github.io/vggt4d/",
        url_code="https://github.com/3DAgentWorld/VGGT4D",
        image="./images/vggt4d.png",
    ))
    papers.append(Paper(
        tag="synthdrive",
        title="SynthDrive: Scalable Real2Sim2Real Sensor Simulation Pipeline for High-Fidelity Asset Generation and Driving Data Synthesis",
        short_title="SynthDrive",
        conference="International Conference on Intelligent Robots and Systems",
        conference_short="IROS'25",
        year=2025,
        authors=gen_author_list("Zhengqing Chen", "Ruohong Mei", "Xiaoyang Guo†", "Qingjie Wang", "Yubin Hu", "Wei Yin", "Weiqiang Ren", "Qian Zhang"),
        url="./files/iros25_synthdrive.pdf",
        url_arxiv=None,
        url_paper="./files/iros25_synthdrive.pdf",
        image="./images/synthdrive.png",
        url_video="https://www.youtube.com/watch?v=WM4dR1b3uAQ",
    ))
    papers.append(Paper(
        tag="comdrive",
        title="ComDrive: Comfort-Oriented End-to-End Autonomous Driving",
        short_title="ComDrive",
        conference="International Conference on Intelligent Robots and Systems",
        conference_short="IROS'25",
        year=2025,
        authors=gen_author_list("Junming Wang, Xingyu Zhang, Zebin Xing, Songen Gu, Xiaoyang Guo, Yang Hu, Ziying Song, Qian Zhang, Xiaoxiao Long, Wei Yin"),
        url="https://arxiv.org/abs/2410.05051",
        url_arxiv="https://arxiv.org/abs/2410.05051",
        url_project_page="https://jmwang0117.github.io/ComDrive/",
        image="./images/comdrive.png",
    ))
    papers.append(Paper(
        tag="sailrecon",
        title="SAIL-Recon: Large SfM by Augmenting Scene Regression with Localization",
        short_title="SAIL-Recon",
        conference="International Conference on 3D Vision",
        conference_short="3DV'26",
        year=2026,
        authors=gen_author_list("Junyuan Deng, Heng Li, Tao Xie, Weiqiang Ren, Qian Zhang, Ping Tan, Xiaoyang Guo†"),
        url="https://arxiv.org/abs/2508.17972",
        url_arxiv="https://arxiv.org/abs/2508.17972",
        url_project_page="https://hkust-sail.github.io/sail-recon/",
        url_code="https://github.com/HKUST-SAIL/sail-recon",
        image="./images/sailrecon.png",
        special_honor="Oral",
    ))
    papers.append(Paper(
        tag="rad",
        title="RAD: Training an End-to-End Driving Policy via Large-Scale 3DGS-Based Reinforcement Learning",
        short_title="RAD",
        conference="Advances in Neural Information Processing Systems",
        conference_short="NeurIPS'25",
        year=2025,
        authors=gen_author_list("Hao Gao, Shaoyu Chen, Bo Jiang, Bencheng Liao, Yiang Shi, Xiaoyang Guo, Yuechuan Pu, Haoran Yin, Xiangyu Li, Xinbang Zhang, Ying Zhang, Wenyu Liu, Qian Zhang, Xinggang Wang"),
        url="https://arxiv.org/abs/2502.13144",
        url_arxiv="https://arxiv.org/abs/2502.13144",
        url_project_page="https://hgao-cv.github.io/RAD/",
        image="./images/rad.png",
    ))
    papers.append(Paper(
        tag="epona",
        title="Epona: Autoregressive Diffusion World Model for Autonomous Driving",
        short_title="Epona",
        conference="International Conference on Computer Vision",
        conference_short="ICCV'25",
        year=2025,
        authors=gen_author_list("Kaiwen Zhang, Zhenyu Tang, Xiaotao Hu, Xingang Pan, Xiaoyang Guo, Yuan Liu, Jingwei Huang, Li Yuan, Qian Zhang, Xiaoxiao Long, Xun Cao, Wei Yin"),
        url="https://arxiv.org/pdf/2506.24113",
        url_arxiv="https://arxiv.org/abs/2506.24113",
        url_project_page="https://kevin-thu.github.io/Epona/",
        url_code="https://kevin-thu.github.io/Epona/",
        image="./images/epona.png",
    ))
    papers.append(Paper(
        tag="calib",
        title="Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration",
        short_title="DM-Calib",
        conference="International Conference on Computer Vision",
        conference_short="ICCV'25",
        year=2025,
        authors=gen_author_list("Junyuan Deng", "Wei Yin", "Xiaoyang Guo†", "Qian Zhang", "Xiaotao Hu", "Weiqiang Ren", "Xiao-Xiao Long", "Ping Tan"),
        url="https://arxiv.org/pdf/2411.17240",
        url_arxiv="https://arxiv.org/abs/2411.17240",
        url_code="https://github.com/JunyuanDeng/DM-Calib",
        image="./images/dm-calib.png",
    ))
    papers.append(Paper(
        tag="drivingworld",
        title="DrivingWorld: Constructing World Model for Autonomous Driving via Video GPT",
        short_title="DrivingWorld",
        conference="Preprint",
        conference_short="Arxiv'24",
        year=2024,
        authors=gen_author_list("Xiaotao Hu, Wei Yin, Mingkai Jia, Junyuan Deng, Xiaoyang Guo, Qian Zhang, Xiaoxiao Long, Ping Tan"),
        url="https://arxiv.org/abs/2412.19505",
        url_arxiv="https://arxiv.org/abs/2412.19505",
        image="./images/drivingworld.png",
    ))
    papers.append(Paper(
        tag="stabledepth",
        title="StableDepth: Scene-Consistent and Scale-Invariant Monocular Depth",
        short_title="StableDepth",
        conference="International Conference on Computer Vision",
        conference_short="ICCV'25",
        year=2025,
        authors=gen_author_list("Zheng Zhang, Lihe Yang, Tianyu Yang, Chaohui Yu, Xiaoyang Guo, Yixing Lao, Hengshuang Zhao"),
        url="https://stabledepth.github.io/",
        url_arxiv=None,
        url_project_page="https://stabledepth.github.io/",
        url_paper="https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_StableDepth_Scene-Consistent_and_Scale-Invariant_Monocular_Depth_ICCV_2025_paper.html",
        special_honor="Highlight",
        image="./images/stabledepth.png",
    ))
    papers.append(Paper(
        tag="ngprt",
        title="NGP-RT: Fusing Multi-Level Hash Features with Lightweight Attention for Real-Time Novel View Synthesis",
        short_title="NGP-RT",
        conference="European Conference on Computer Vision",
        conference_short="ECCV'24",
        year=2024,
        authors=gen_author_list("Yubin Hu*", "Xiaoyang Guo*", "Yang Xiao", "Jingwei Huang", "Yong-Jin Liu"),
        url="https://link.springer.com/chapter/10.1007/978-3-031-72670-5_9",
        url_paper="https://link.springer.com/chapter/10.1007/978-3-031-72670-5_9",
        url_arxiv="https://arxiv.org/abs/2407.10482",
        image="./images/ngprt.png",
        special_honor="Realtime streamed on Petal Map App",
        video_after="./images/ngp_rt_shitang.mp4"
    ))
    papers.append(Paper(
        tag="ss3dm",
        title="SS3DM: Benchmarking Street-View Surface Reconstruction with a Synthetic 3D Mesh Dataset",
        short_title="SS3DM",
        conference="Advances in Neural Information Processing Systems",
        conference_short="NeurIPS'24 (DB Track)",
        year=2024,
        authors=gen_author_list("Yubin Hu", "Kairui Wen", "Heng Zhou", "Xiaoyang Guo", "Yong-Jin Liu"),
        url="https://proceedings.neurips.cc/paper_files/paper/2024/hash/c11767cd469b8d8bd7f168e61b3cc8bc-Abstract-Datasets_and_Benchmarks_Track.html",
        url_arxiv="https://arxiv.org/abs/2410.21739",
        url_project_page="https://github.com/THU-LYJ-Lab/SS3DM-Exporter",
        url_dataset="https://huggingface.co/datasets/SS3DM/SS3DM-Dataset/tree/main",
        image="./images/ss3dm-after.png",
        image_after="./images/ss3dm.png",
    ))
    papers.append(Paper(
        tag="arrangement",
        title="ArrangementNet: Learning Scene Arrangements for Vectorized Indoor Scene Modeling",
        short_title="ArrangementNet",
        conference="ACM Transactions on Graphics (TOG) ",
        conference_short="TOG'23",
        year=2023,
        authors=gen_author_list("Jingwei Huang", "Shanshan Zhang", "Bo Duan", "Xiaoyang Guo", "Minwei Sun", "Li Yi"),
        url="https://dl.acm.org/doi/10.1145/3592122",
        image="./images/arrangementnet.png",
        video_after="./images/arrangementnet.mp4",
        url_arxiv=None,
        url_paper="https://dl.acm.org/doi/10.1145/3592122",
        special_honor="Journal Track"
    ))
    papers.append(Paper(
        tag="liga",
        title="LIGA-Stereo: Learning Lidar Geometry aware Representations for Stereo-based 3d Detector",
        short_title="LIGA-Stereo",
        conference="International Conference on Computer Vision)",
        conference_short="ICCV'21",
        year=2021,
        authors=gen_author_list("Xiaoyang Guo", "Shaoshuai Shi", "Xiaogang Wang", "Hongsheng Li"),
        url="https://openaccess.thecvf.com/content/ICCV2021/html/Guo_LIGA-Stereo_Learning_LiDAR_Geometry_Aware_Representations_for_Stereo-Based_3D_Detector_ICCV_2021_paper.html",
        url_arxiv="https://arxiv.org/abs/2108.08258",
        url_paper="https://openaccess.thecvf.com/content/ICCV2021/html/Guo_LIGA-Stereo_Learning_LiDAR_Geometry_Aware_Representations_for_Stereo-Based_3D_Detector_ICCV_2021_paper.html",
        url_poster=None,
        url_code="https://github.com/xy-guo/LIGA-Stereo",
        url_project_page="/liga",
        image="./images/liga.png",
        image_after="./images/liga-det.png",
        special_honor="Ranked 1st place among stereo-based 3D detection methods on KITTI (July 2021), refer to <a href=\"https://www.cvlibs.net/datasets/kitti/eval_object_detail.php?&result=d5d1938b704537150df7f8403d173aa16fe9ba17\">here</a>.",
        abstract="Stereo-based 3D detection aims at detecting 3D object bounding boxes from stereo images using intermediate depth maps or implicit 3D geometry representations, which provides a low-cost solution for 3D perception. However, its performance is still inferior compared with LiDAR-based detection algorithms. To detect and localize accurate 3D bounding boxes, LiDAR-based models can encode accurate object boundaries and surface normal directions from LiDAR point clouds. However, the detection results of stereo-based detectors are easily affected by the erroneous depth features due to the limitation of stereo matching. To solve the problem, we propose LIGA-Stereo (LiDAR Geometry Aware Stereo Detector) to learn stereo-based 3D detectors under the guidance of high-level geometry-aware representations of LiDAR-based detection models. In addition, we found existing voxel-based stereo detectors failed to learn semantic features effectively from indirect 3D supervisions. We attach an auxiliary 2D detection head to provide direct 2D semantic supervisions. Experiment results show that the above two strategies improved the geometric and semantic representation capabilities. Compared with the state-of-the-art stereo detector, our method has improved the 3D detection performance of cars, pedestrians, cyclists by <strong>10.44%, 5.69%, 5.97%</strong> mAP respectively on the official KITTI benchmark. ",
        affiliation="CUHK-SenseTime Joint Laboratory, The Chinese University of Hong Kong",
        bib="""@InProceedings{Guo_2021_ICCV,
    author = {Guo, Xiaoyang and Shi, Shaoshuai and Wang, Xiaogang and Li, Hongsheng},
    title = {LIGA-Stereo: Learning LiDAR Geometry Aware Representations for Stereo-based 3D Detector},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    month = {October},
    year = {2021}
}
        """
    ))
    papers.append(Paper(
        tag="gwcnet",
        title="Group-wise Correlation Stereo Network",
        short_title="GwcNet",
        conference="Conference on Computer Vision and Pattern Recognition",
        conference_short="CVPR'19",
        year=2019,
        authors=gen_author_list("Xiaoyang Guo", "Kai Yang", "Wukui Yang", "Xiaogang Wang", "Hongsheng Li"),
        url="https://openaccess.thecvf.com/content_CVPR_2019/html/Guo_Group-Wise_Correlation_Stereo_Network_CVPR_2019_paper.html",
        url_arxiv="https://arxiv.org/abs/1903.04025",
        url_paper="https://openaccess.thecvf.com/content_CVPR_2019/html/Guo_Group-Wise_Correlation_Stereo_Network_CVPR_2019_paper.html",
        url_poster=None,
        url_code="https://github.com/xy-guo/GwcNet",
        image="./images/gwcnet.jpg",
    ))
    papers.append(Paper(
        tag="unsupstereo",
        title="Unsupervised Cross-Spectral Stereo Matching by Learning to Synthesize",
        short_title=None,
        conference="AAAI",
        conference_short="AAAI'19",
        year=2019,
        authors=gen_author_list("Xiaoyang Guo*", "Mingyang Liang*", "Hongsheng Li", "Xiaogang Wang", "You Song"),
        url="https://ojs.aaai.org/index.php/AAAI/article/view/4894",
        url_arxiv="https://arxiv.org/abs/1903.01078",
        url_paper="https://ojs.aaai.org/index.php/AAAI/article/view/4894",
        image="./images/cs-stereo.jpg",
        special_honor="Oral Presentation"
    ))
    papers.append(Paper(
        tag="distillmono",
        title="Learning Monocular Depth by Distilling Cross-domain Stereo Networks",
        short_title=None,
        conference="European Conference on Computer Vision",
        conference_short="ECCV'18",
        year=2018,
        authors=gen_author_list("Xiaoyang Guo", "Hongsheng Li", "Shuai Yi", "Jimmy Ren", "Xiaogang Wang"),
        url="https://openaccess.thecvf.com/content_ECCV_2018/html/Xiaoyang_Guo_Learning_Monocular_Depth_ECCV_2018_paper.html",
        url_arxiv="https://arxiv.org/abs/1808.06586",
        url_paper="https://openaccess.thecvf.com/content_ECCV_2018/html/Xiaoyang_Guo_Learning_Monocular_Depth_ECCV_2018_paper.html",
        url_poster=None,
        url_video="https://www.youtube.com/watch?v=QAcuYT7q_gY",
        url_code="https://github.com/xy-guo/Learning-Monocular-Depth-by-Stereo",
        image="./images/mono.jpg",
    ))
    papers.append(Paper(
        tag="encap",
        title="Neural Network Encapsulation",
        short_title="Encap",
        conference="European Conference on Computer Vision",
        conference_short="ECCV'18",
        year=2018,
        authors=gen_author_list("Hongyang Li", "Xiaoyang Guo", "Bo Dai", "Wanli Ouyang", "Xiaogang Wang"),
        url="https://openaccess.thecvf.com/content_ECCV_2018/html/Hongyang_Li_Neural_Network_Encapsulation_ECCV_2018_paper.html",
        url_arxiv="https://arxiv.org/abs/1808.03749",
        url_paper="https://openaccess.thecvf.com/content_ECCV_2018/html/Hongyang_Li_Neural_Network_Encapsulation_ECCV_2018_paper.html",
        url_poster=None,
        image="./images/encap.png",
    ))

    return papers

def get_news():
    return [
        dict(date="2026.06", text='One paper accepted to <strong>ICML 2026</strong> (EPS3D). SCOPE released on arXiv.'),
        dict(date="2026.04", text='Four papers accepted to <strong>CVPR 2026</strong>: Scal3R (<strong>Highlight</strong>), LongStream, LiteVGGT, and VGGT4D.'),
        dict(date="2026.03", text='CompoSIA accepted to <strong>ECCV 2026</strong>. Started working on embodied foundation models.'),
        dict(date="2026.02", text='SAIL-Recon accepted as an <strong>Oral</strong> at <strong>3DV 2026</strong>.'),
        dict(date="2025.10", text='Three papers at <strong>ICCV 2025</strong> (Epona, DM-Calib, StableDepth <strong>Highlight</strong>); RAD at <strong>NeurIPS 2025</strong>; SynthDrive and ComDrive at <strong>IROS 2025</strong>.'),
    ]


def get_exp():
    exp = []
    exp.append(Experience(
        title="World Model & Embodied Foundation Model, Mar 2026 - Present",
        description="Leading world-model research; training an embodied foundation model unifying understanding, simulation, and action."
    ))
    exp.append(Experience(
        title="Principal Researcher, Oct 2023 - Feb 2026, Horizon Robotics",
        description="3D reconstruction (Deep-MVS & VGGT), AI digital twin & simulation (3DGS), video diffusion for interactive driving simulation."
    ))
    exp.append(Experience(
        title="Principal Engineer, Oct 2021 - Oct 2023, Huawei Inc.",
        description="Indoor CAD-from-images; large-scale NeRF library."
    ))
    exp.append(Experience(
        title="Research Intern, June 2019 - Oct 2019, Google, Seattle",
        description="Advised by Raviteja Vemulapalli."
    ))
    return exp


def find_paper(startswith) -> Paper:
    papers = get_papers()
    for paper in papers:
        if paper.title.startswith(startswith):
            return paper
    return None


def render_index(filename="index.jinja"):
    render_data = dict(
        title=title,
        name=name,
        papers=get_papers(),
        news=get_news(),
    )
    subs = jinja2.Environment(
        loader=jinja2.FileSystemLoader('./')
    ).get_template(filename).render(**render_data)
    lines = subs.split("\n")
    lines = [line for line in lines if len(line.strip()) > 0]
    subs = '\n'.join(lines)

    with open(filename.replace(".jinja", ".html"), 'w') as f:
        f.write(subs)


@dataclass
class Project:
    link: str
    short_name: str
    title: str
    abstract: str
    image: str
    video: str
    paper: Paper
    pre_html: str = ""
    extra_html: str = ""


# def render_project_pages(filename="project.jinja"):
#     projects = []

#     liga_paper = find_paper("LIGA")
#     projects.append(
#         Project(
#             link="liga",
#             short_name=liga_paper.short_title,
#             title=liga_paper.title,
#             abstract=liga_paper.abstract,
#             image=None,
#             video=liga_paper.url_video,
#             paper=liga_paper,
#             pre_html="""
#                 <center>
#                     <img src="/images/liga.png" alt="..." width="60%" />
#                 </center>
#             """,
#             extra_html="""
#                 <h4>Results<h4>
#                 <p>
#                     <center>
#                         <img src="/images/liga-demo.png" alt="..." width="100%" />
#                     </center>
#                 </p>        
#                 <h4>KITTI Benchmark<h4>
#                 <p>
#                     <center>
#                         <img src="/images/liga-kitti.png" alt="..." width="80%" />
#                     </center>
#                 </p>
#             """
#         )
#     )

#     for proj in projects:
#         render_data = dict(
#             project=proj,
#             paper=proj.paper,
#         )
#         subs = jinja2.Environment(
#             loader=jinja2.FileSystemLoader('./')
#         ).get_template(filename).render(**render_data)

#         dump_path = proj.link
#         if not os.path.isdir(dump_path):
#             os.mkdir(dump_path)
#         dump_file = os.path.join(dump_path, "index.html")
#         print("saving to", dump_file)
#         with open(dump_file, 'w') as f:
#             f.write(subs)


if __name__ == "__main__":
    render_index()
    # render_project_pages()