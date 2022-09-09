import numpy as np
from scipy import linalg

def ca(dt):
  """ CA function """

  dt = dt.loc[(dt!=0).any(1)]
  cp_dt = dt / np.sum(dt).sum()
  cd_dt = cp_dt - cp_dt.mean(axis=0)
  p = np.array(cp_dt)
  r = p@np.ones(shape=(p.shape[1]))
  c = p.T@np.ones(shape=(p.shape[0]))
  c_sq = np.diag(c ** 0.5).astype(np.float64)
  c_inv = np.diag(c ** -1).astype(np.float64)
  r_sq = np.diag(r ** 0.5).astype(np.float64)
  r_inv = np.diag(r ** -1).astype(np.float64)
  r_diag = np.diag(r).astype(np.float64)
  c_diag = np.diag(c).astype(np.float64)
  r_neg_sq = np.diag(r ** -0.5).astype(np.float64)
  c_neg_sq = np.diag(c ** -0.5).astype(np.float64)
  S = r_neg_sq@(p-np.outer(r,c))@c_neg_sq
  (U, s, Vh) = linalg.svd(S, full_matrices=False)
  e = np.diag(s).astype(np.float64)
  phi = (r_neg_sq @ U).astype(np.float64)
  gamma = (c_neg_sq @ Vh.T).astype(np.float64)
  F = (r_neg_sq @ U @ e).astype(np.float64)
  G = (c_neg_sq @ Vh.T @ e).astype(np.float64)
  lam_ = np.diag(s ** 2)
  lam_inv = np.diag(s ** -1)

  return F, G, cp_dt
