import jinja2
from dataclasses import dataclass
from typing import List
import os
import shutil

title = 'Xiaoyang Guo - CUHK'
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
        if author_name[-1] in ["†", "‡"]:
            author_name = author_name[:-1] + f"<sup>{author_name[-1]}</sup>"
        authors.append(Author(
            name=author_name,
            url=url
        ))
    return authors


def get_papers():
    papers = []
    papers.append(Paper(
        tag="rad",
        title="Rad: Training an End-to-end Driving Policy via Large-scale 3dgs-based Reinforcement Learning",
        short_title="RAD",
        conference="Preprint",
        conference_short="Arxiv'25",
        year=2025,
        authors=gen_author_list("Hao Gao, Shaoyu Chen, Bo Jiang, Bencheng Liao, Yiang Shi, Xiaoyang Guo, Yuechuan Pu, Haoran Yin, Xiangyu Li, Xinbang Zhang, Ying Zhang, Wenyu Liu, Qian Zhang, Xinggang Wang"),
        url="https://arxiv.org/abs/2502.13144",
        url_arxiv="https://arxiv.org/abs/2502.13144",
        url_project_page="https://hgao-cv.github.io/RAD/",
        image="./images/rad.png",
    ))
    papers.append(Paper(
        tag="synthdrive",
        title="SynthDrive: Scalable Real2Sim2Real Sensor Simulation Pipeline for High-Fidelity Asset Generation and Driving Data Synthesis",
        short_title="SynthDrive",
        conference="International Conference on Intelligent Robots and Systems",
        conference_short="IROS'25",
        year=2025,
        authors=gen_author_list("ZhengQing Chen", "Ruohong Mei", "Xiaoyang Guo†", "Qingjie Wang", "Yubin Hu", "Wei Yin", "Weiqiang Ren", "Qian Zhang"),
        url="",
        url_paper="./papers/iros25_synthdrive.pdf",
        url_arxiv="",
        url_project_page="",
        image="./images/synthdrive.png",
        video_after="./images/synthdrive.mp4",
        url_video="https://www.youtube.com/watch?v=WM4dR1b3uAQ",
    ))
    papers.append(Paper(
        tag="calib",
        title="Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration",
        short_title="DM-Calib",
        conference="International Conference on Computer Vision",
        conference_short="ICCV'25",
        year=2025,
        authors=gen_author_list("Junyuan Deng", "Wei Yin", "Xiaoyang Guo‡", "Qian Zhang", "Xiaotao Hu", "Weiqiang Ren", "Xiao-Xiao Long", "Ping Tan†"),
        url="https://arxiv.org/pdf/2411.17240",
        url_arxiv="https://arxiv.org/pdf/2411.17240",
        url_code="https://github.com/JunyuanDeng/DM-Calib",
        image="./images/dm-calib.png",
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
        tag="stabledepth",
        title="StableDepth: Scene-Consistent and Scale-Invariant Monocular Depth",
        short_title="StableDepth",
        conference="International Conference on Computer Vision",
        conference_short="ICCV'25",
        year=2025,
        authors=gen_author_list("Zheng Zhang, Lihe Yang, Tianyu Yang, Chaohui Yu, Xiaoyang Guo, Yixing Lao, Hengshuang Zhao"),
        url="",
        url_arxiv="",
        special_honor="Spotlight",
        image="./images/stabledepth.png",
    ))
    papers.append(Paper(
        tag="ngprt",
        title="NGP-RT: Fusing Multi-Level Hash Features with Lightweight Attention for Real-Time Novel View Synthesis",
        short_title="NGP-RT",
        conference="European Conference on Computer Vision",
        conference_short="ECCV'24",
        year=2025,
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
        title="SS3DM: Self-Supervised 3D Reconstruction from Monocular Videos",
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
        url_arxiv="",
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
        # url_supp="https://openaccess.thecvf.com/content/ICCV2021/supplemental/Guo_LIGA-Stereo_Learning_LiDAR_ICCV_2021_supplemental.pdf",
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

def get_exp():
    exp = []
    exp.append(Experience(
        title="Researcher, Oct 2021 - Present, Huawei Inc.",
        description="Working on large-scale MVS, NeRF."
    ))
    exp.append(Experience(
        title="Researcn Intern, June 2019 - Oct 2019, Google, Seattle",
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
        # experience=get_exp()
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