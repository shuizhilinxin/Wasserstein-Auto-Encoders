import wae
import argparse
import config

parser = argparse.ArgumentParser()
parser.add_argument("--experiment",
                    help='Default experiment configs to use: dsprites/fading_squares/celebA_mini/celebA_random/celebA_deterministic')
parser.add_argument("--dataset",
                    help='Dataset to train on: dsprites/celebA/celebA_mini/fading_squares')
parser.add_argument("--z_dim", help='latent space dimensionality', type=int)
parser.add_argument("--lambda_imq", help='Lambda for WAE penalty', type=float)
parser.add_argument("--experiment_path",
                    help="Relative path to where this experiment should save results")
parser.add_argument("--encoder_distribution",
                    help="Encoder distribution: deterministic/gaussian/uniform")
parser.add_argument("--z_prior",
                    help="Prior distribution over latent space: gaussian/uniform")
parser.add_argument("--loss_reconstruction",
                    help="Image reconstruction loss: bernoulli/L2_squared")
parser.add_argument("--loss_regulariser",
                    help="Model type: VAE/beta_VAE/WAE_MMD")
parser.add_argument("--beta", type=float,
                    help="beta parameter for beta_VAE")
parser.add_argument("--disentanglement_metric", type=bool,
                    help="Calculate disentanglement metric")
parser.add_argument("--make_pictures_every", type=int,
                    help="How often to plot random samples and reconstructions")
parser.add_argument("--save_every", type=int,
                    help="How often to save the model")
parser.add_argument("--batch_size", type=int,
                    help="Batch size. Default 100")
parser.add_argument("--encoder_architecture",
                    help="Architecture of encoder: FC_dsprites/small_convolutional_celebA")
parser.add_argument("--decoder_architecture",
                    help="Architecture of decoder: FC_dsprites/small_convolutional_celebA")
parser.add_argument("--z_logvar_regularisation",
                    help="Regularisation on log-variances: None/L1/L2_squared")
parser.add_argument("--lambda_logvar_regularisation", type=float,
                    help="Coefficient of logvariance regularisation")
parser.add_argument("--plot_losses",
                    help="Plot losses and least-gaussian-subspace: True/False:")
parser.add_argument("--adversarial_cost_n_filters", type=int,
                    help="Number of convolutional filters to use for adversarial cost")

FLAGS = parser.parse_args()

if __name__ == "__main__":
    if FLAGS.experiment == 'dsprites':
        opts = config.dsprites_opts
    elif FLAGS.experiment == 'fading_squares':
        opts = config.fading_squares_opts
    elif FLAGS.experiment == 'celebA_random':
        opts = config.celebA_random_opts
    elif FLAGS.experiment == 'celebA_deterministic':
        opts = config.celebA_deterministic_opts
    elif FLAGS.experiment == 'celebA_mini':
        opts = config.celebA_mini_opts
    elif FLAGS.experiment == 'celebA_dcgan_deterministic':
        opts = config.celebA_dcgan_deterministic_opts
    elif FLAGS.experiment == 'grassli_VAE':
        opts = config.grassli_VAE_opts
    elif FLAGS.experiment == 'grassli_WAE':
        opts = config.grassli_WAE_opts
    elif FLAGS.experiment == 'celebA_dcgan_adv':
        opts = config.celebA_dcgan_adv_cost_opts
    else:
        assert False, "Invalid experiment defaults"

    if FLAGS.dataset:
        opts['dataset'] = FLAGS.dataset
    if FLAGS.z_dim:
        opts['z_dim'] = FLAGS.z_dim
    if FLAGS.lambda_imq:
        opts['lambda_imq'] = FLAGS.lambda_imq
    if FLAGS.experiment_path:
        opts['experiment_path'] = FLAGS.experiment_path
    if FLAGS.encoder_distribution:
        opts['encoder_distribution'] = FLAGS.encoder_distribution
    if FLAGS.z_prior:
        opts['z_prior'] = FLAGS.z_prior
    if FLAGS.loss_reconstruction:
        opts['loss_reconstruction'] = FLAGS.loss_reconstruction
    if FLAGS.disentanglement_metric:
        opts['disentanglement_metric'] = FLAGS.disentanglement_metric
    if FLAGS.make_pictures_every:
        opts['make_pictures_every'] = FLAGS.make_pictures_every
    if FLAGS.save_every:
        opts['save_every'] = FLAGS.save_every
    if FLAGS.batch_size:
        opts['batch_size'] = FLAGS.batch_size
    if FLAGS.encoder_architecture:
        opts['encoder_architecture'] = FLAGS.encoder_architecture
    if FLAGS.decoder_architecture:
        opts['decoder_architecture'] = FLAGS.decoder_architecture
    if FLAGS.z_logvar_regularisation:
        if FLAGS.z_logvar_regularisation == "None":
            opts['z_logvar_regularisation'] = None
        else:
            opts['z_logvar_regularisation'] = FLAGS.z_logvar_regularisation
    if FLAGS.lambda_logvar_regularisation:
        opts['lambda_logvar_regularisation'] = FLAGS.lambda_logvar_regularisation
    if FLAGS.loss_regulariser:
        opts['loss_regulariser'] = FLAGS.loss_regulariser
    if FLAGS.beta:
        opts['beta'] = FLAGS.beta
    if FLAGS.plot_losses:
        if FLAGS.plot_losses == "True":
            opts['plot_losses'] = True
        elif FLAGS.plot_losses == "False":
            opts['plot_losses'] = False
    if FLAGS.adversarial_cost_n_filters:
        opts['adversarial_cost_n_filters'] = FLAGS.adversarial_cost_n_filters


    model = wae.Model(opts)
    model.train()
