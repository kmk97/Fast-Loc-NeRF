import rospy
import numpy as np
import warnings
from full_filter import NeRF
import yaml
 # Base class to handle loading params from yaml.

class NavigatorBase:
    def __init__(self, img_num=0, dataset_name=None):
        # extract params
        param_file = rospy.get_param('parameter_file')

        # 로드한 파라미터 딕셔너리
        with open(param_file, 'r') as file:
            params = yaml.safe_load(file)
        
        for key, value in params.items():
            setattr(self, key, value)
        # just used for Nerf-Navigation comparison
        self.model_ngp = None
        self.ngp_opt = None

        if dataset_name is not None:
            self.model_name = dataset_name
        else:
            self.model_name = rospy.get_param('model_name')
        self.data_dir = rospy.get_param('data_dir') + "/" + self.model_name
        self.ckpt_dir = rospy.get_param('ckpt_dir') + "/" + self.model_name     

        self.obs_img_num = img_num

        # TODO these don't individually need to be part of the navigator class
        nerf_params = {'near':self.near, 'far':self.far, 'course_samples':self.course_samples, 'fine_samples':self.fine_samples,
                       'batch_size':self.batch_size, 'factor':self.factor, 'focal':self.focal, 'H':self.H, 'W':self.W, 'dataset_type':self.dataset_type,
                       'obs_img_num':self.obs_img_num, 'kernel_size':self.kernel_size, 'lrate':self.lrate, 'sampling_strategy':self.sampling_strategy,
                       'model_name':self.model_name, 'data_dir':self.data_dir, 'no_ndc':self.no_ndc, 'dil_iter':self.dil_iter,
                       'multires':self.multires, 'multires_views':self.multires_views, 'i_embed':self.i_embed, 'netwidth':self.netwidth, 'netdepth':self.netdepth,
                       'netdepth_fine':self.netdepth_fine, 'netwidth_fine':self.netwidth_fine, 'use_viewdirs':self.use_viewdirs, 'ckpt_dir':self.ckpt_dir,
                       'perturb':self.perturb, 'white_bkgd':self.white_bkgd, 'raw_noise_std':self.raw_noise_std, 'lindisp':self.lindisp,
                       'netchunk':self.netchunk, 'chunk':self.chunk, 'bd_factor':self.bd_factor}
        self.nerf = NeRF(nerf_params)
        
        self.image = None
        self.rgb_input_count = 0
        self.num_updates = 0
        
        self.previous_vio_pose = None
        self.nerf_pose = None
        self.all_pose_est = [] # plus 1 since we put in the initial pose before the first update
        self.img_msg = None
        
        # for now only have gt pose for llff dataset for inerf comparison and nerf-nav comparison
        self.gt_pose = None
        if not self.use_received_image:
            self.gt_pose = np.copy(self.nerf.obs_img_pose)
        
        self.check_params()
        if self.ours:
            self.refinement_used = False 
            self._num_particles = self.num_particles
            self._resolution = self.resolution
            self.resolution = self.init_resolution

    def check_params(self):
        """
        Useful helper function to check if suspicious or invalid params are being used.
        TODO: Not all bad combinations of params are currently checked here.
        """

        if self.alpha_super_refine > self.alpha_refine:
            warnings.warn("alpha_super_refine is larger than alpha_refine, code will run but they are probably flipped by the user")
        
        if self.sampling_strategy != "random":
            warnings.warn("did not enter a valid sampling strategy. Currently the following are supported: random")

        if self.photometric_loss != "rgb":
            warnings.warn("did not enter a valid photometric loss. Currently the following are supported: rgb")